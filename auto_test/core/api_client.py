"""Unified requests client.

Business request behavior must follow ``knowledge/06_auto_test_spec/api_code_spec.md``.
Tests must use the fixture-provided client instead of importing requests directly.
"""

from __future__ import annotations

import json
import time
from collections.abc import Callable, Mapping
from typing import Any, Optional, Union
from urllib.parse import urljoin

import requests
from requests import Response, Session
from requests.exceptions import RequestException

from auto_test.utils.logger import get_logger, redact_mapping

Timeout = Union[float, tuple[float, float]]
TokenProvider = Callable[[], Optional[str]]
TokenRefresher = Callable[[], Optional[str]]


class ApiClientError(RuntimeError):
    """Base error raised by the unified API client."""


class ApiRequestError(ApiClientError):
    """Network or protocol failure with request context."""

    def __init__(
        self,
        message: str,
        *,
        method: str,
        url: str,
        response: Optional[Response] = None,
    ) -> None:
        super().__init__(message)
        self.method = method
        self.url = url
        self.response = response


class ApiResponseDecodeError(ApiClientError):
    """Raised when a response expected to be JSON cannot be decoded."""


class ApiClient:
    """requests.Session wrapper with auth, retries, timeout, and safe logging."""

    def __init__(
        self,
        base_url: str,
        *,
        session: Optional[Session] = None,
        timeout: Timeout = (5.0, 30.0),
        verify_ssl: bool = True,
        token_provider: Optional[TokenProvider] = None,
        token_refresher: Optional[TokenRefresher] = None,
        logger=None,
    ) -> None:
        if not base_url:
            raise ValueError("API base_url is required; configure it in config/env.yaml or environment variables")
        self.base_url = base_url.rstrip("/") + "/"
        self.session = session or requests.Session()
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.token_provider = token_provider
        self.token_refresher = token_refresher
        self.logger = logger or get_logger("tms.api")

    def close(self) -> None:
        self.session.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        retry_on_unauthorized: bool = True,
        **kwargs: Any,
    ) -> Response:
        """Send one request and optionally refresh the token once after HTTP 401."""
        method = method.upper()
        url = self._build_url(path)
        headers = dict(kwargs.pop("headers", {}) or {})
        token = self.token_provider() if self.token_provider else None
        if token and "X-Access-Token" not in headers:
            headers["X-Access-Token"] = token

        timeout = kwargs.pop("timeout", self.timeout)
        verify = kwargs.pop("verify", self.verify_ssl)
        started = time.perf_counter()
        self._log_request(method, url, headers, kwargs)

        try:
            response = self.session.request(
                method,
                url,
                headers=headers,
                timeout=timeout,
                verify=verify,
                **kwargs,
            )
        except RequestException as exc:
            elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
            self.logger.exception(
                "api_request_failed",
                extra={
                    "event_data": {
                        "method": method,
                        "url": url,
                        "elapsed_ms": elapsed_ms,
                        "error": str(exc),
                    }
                },
            )
            raise ApiRequestError(
                f"{method} {url} failed: {exc}",
                method=method,
                url=url,
            ) from exc

        elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
        self._log_response(method, url, response, elapsed_ms)

        if (
            response.status_code == 401
            and retry_on_unauthorized
            and self.token_refresher is not None
        ):
            refreshed_token = self.token_refresher()
            if refreshed_token:
                retry_headers = dict(headers)
                retry_headers["X-Access-Token"] = refreshed_token
                return self.request(
                    method,
                    path,
                    headers=retry_headers,
                    retry_on_unauthorized=False,
                    timeout=timeout,
                    verify=verify,
                    **kwargs,
                )
        return response

    def get(self, path: str, **kwargs: Any) -> Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Response:
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Response:
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Response:
        return self.request("DELETE", path, **kwargs)

    @staticmethod
    def json(response: Response) -> Any:
        """Decode JSON with an explicit, diagnosable failure."""
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as exc:
            preview = response.text[:500]
            raise ApiResponseDecodeError(
                f"Response is not valid JSON (status={response.status_code}): {preview}"
            ) from exc

    def _build_url(self, path: str) -> str:
        if path.startswith(("http://", "https://")):
            return path
        return urljoin(self.base_url, path.lstrip("/"))

    def _log_request(
        self,
        method: str,
        url: str,
        headers: Mapping[str, Any],
        kwargs: Mapping[str, Any],
    ) -> None:
        payload = kwargs.get("json", kwargs.get("data"))
        self.logger.info(
            "api_request",
            extra={
                "event_data": {
                    "method": method,
                    "url": url,
                    "headers": redact_mapping(headers),
                    "params": redact_mapping(kwargs.get("params", {})),
                    "payload": redact_mapping(payload) if isinstance(payload, Mapping) else payload,
                }
            },
        )

    def _log_response(
        self,
        method: str,
        url: str,
        response: Response,
        elapsed_ms: float,
    ) -> None:
        try:
            body: Any = response.json()
        except ValueError:
            body = response.text[:2000]
        if isinstance(body, Mapping):
            body = redact_mapping(body)
        self.logger.info(
            "api_response",
            extra={
                "event_data": {
                    "method": method,
                    "url": url,
                    "status_code": response.status_code,
                    "elapsed_ms": elapsed_ms,
                    "body": body,
                }
            },
        )
