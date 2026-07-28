"""Technical smoke test for BrowserBase; contains no page model or business flow."""

import pytest

from auto_test.core.browser_base import BrowserBase


@pytest.mark.ui_foundation
@pytest.mark.smoke
def test_browser_base_foundation_smoke(browser_base: BrowserBase):
    """Verify fixture-managed Playwright page and screenshot infrastructure."""
    browser_base.page.set_content("<main><h1>TMS automation foundation</h1></main>")

    assert "TMS automation foundation" in browser_base.page.content()
    assert browser_base.capture_screenshot("browser-foundation-smoke").exists()
