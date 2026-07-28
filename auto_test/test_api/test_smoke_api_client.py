"""Technical smoke test for ApiClient; contains no TMS business behavior."""

import pytest
from requests import Response

from auto_test.core.api_client import ApiClient


class FakeSession:
    def __init__(self) -> None:
        self.last_request = {}
        self.closed = False

    def request(self, method, url, **kwargs):
        self.last_request = {"method": method, "url": url, **kwargs}
        response = Response()
        response.status_code = 200
        response.url = url
        response.headers["Content-Type"] = "application/json"
        response._content = b'{"success": true, "component": "api_client"}'
        return response

    def close(self):
        self.closed = True


@pytest.mark.api_foundation
@pytest.mark.smoke
def test_api_client_foundation_smoke(api_client: ApiClient):
    """Verify URL joining, fixture injection, JSON decoding, and session reuse."""
    fake_session = FakeSession()
    api_client.session = fake_session

    response = api_client.get("/foundation/health")

    assert response.status_code == 200
    assert api_client.json(response)["component"] == "api_client"
    assert fake_session.last_request["method"] == "GET"
    assert fake_session.last_request["url"].endswith("/foundation/health")
