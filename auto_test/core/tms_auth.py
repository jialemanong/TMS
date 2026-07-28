"""Reusable authentication coordinator for the TMS test environment."""

from __future__ import annotations

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from auto_test.core.captcha_recognizer import (
    CaptchaRecognitionError,
    CaptchaRecognizer,
)
from auto_test.pom.tms.login_page import TmsLoginPage
from auto_test.utils.logger import get_logger


class TmsLoginError(RuntimeError):
    """Raised when TMS login cannot complete within the configured retries."""


class TmsAuthenticator:
    """Coordinate credential filling and OCR retries outside the POM layer."""

    def __init__(
        self,
        login_page: TmsLoginPage,
        recognizer: CaptchaRecognizer,
        *,
        max_attempts: int = 3,
        login_timeout_ms: int = 15_000,
    ) -> None:
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        self.login_page = login_page
        self.recognizer = recognizer
        self.max_attempts = max_attempts
        self.login_timeout_ms = login_timeout_ms
        self.logger = get_logger("tms.auth")

    def login(self, username: str, password: str) -> None:
        """Log in with a freshly refreshed captcha and bounded OCR retries."""
        if not username or not password:
            raise TmsLoginError(
                "TMS_UI_USERNAME and TMS_UI_PASSWORD must be configured"
            )

        self.login_page.open()
        last_error = ""
        for attempt in range(1, self.max_attempts + 1):
            try:
                self.login_page.refresh_captcha()
                captcha = self.recognizer.recognize(
                    self.login_page.capture_captcha()
                )
                self.login_page.fill_username(username)
                self.login_page.fill_password(password)
                self.login_page.fill_captcha(captcha)
                self.login_page.click_login()
                self.login_page.page.wait_for_url(
                    lambda url: "/login" not in url,
                    timeout=self.login_timeout_ms,
                    wait_until="domcontentloaded",
                )
                self.logger.info(
                    "tms_login_succeeded",
                    extra={"event_data": {"attempt": attempt}},
                )
                return
            except (CaptchaRecognitionError, PlaywrightTimeoutError) as exc:
                last_error = str(exc)
                self.logger.warning(
                    "tms_login_retry",
                    extra={
                        "event_data": {
                            "attempt": attempt,
                            "max_attempts": self.max_attempts,
                        }
                    },
                )

        raise TmsLoginError(
            f"TMS login failed after {self.max_attempts} attempts: {last_error}"
        )
