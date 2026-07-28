"""Shared base class for human-maintained TMS page objects.

POM ownership and locator rules:
``knowledge/06_auto_test_spec/ui_code_spec.md``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from playwright.sync_api import Locator, Page, expect

from auto_test.core.browser_base import BrowserBase


class BasePage:
    """Provide locator-agnostic atomic operations for TMS page objects."""

    DEFAULT_TIMEOUT_MS = 30_000

    def __init__(self, browser: BrowserBase) -> None:
        self.browser = browser
        self.page: Page = browser.page

    def open(self, path: str = "") -> None:
        """Open a configured TMS path and wait for the document."""
        self.browser.goto(path)
        self.wait_until_ready()

    def wait_until_ready(self, *, timeout: Optional[float] = None) -> None:
        """Wait until the current document is ready for page-level checks."""
        self.browser.wait_for_ready(timeout=timeout)

    def capture_screenshot(self, name: str, *, full_page: bool = True) -> Path:
        """Capture a page artifact through the shared browser foundation."""
        return self.browser.capture_screenshot(name, full_page=full_page)

    @staticmethod
    def _timeout(timeout: Optional[float]) -> float:
        return timeout if timeout is not None else BasePage.DEFAULT_TIMEOUT_MS

    @staticmethod
    def wait_until_visible(locator: Locator, *, timeout: Optional[float] = None) -> None:
        """Wait until one page element is visible."""
        expect(locator).to_be_visible(timeout=BasePage._timeout(timeout))

    @staticmethod
    def wait_until_hidden(locator: Locator, *, timeout: Optional[float] = None) -> None:
        """Wait until one page element is hidden."""
        expect(locator).to_be_hidden(timeout=BasePage._timeout(timeout))

    @staticmethod
    def wait_until_enabled(locator: Locator, *, timeout: Optional[float] = None) -> None:
        """Wait until one page control can be operated."""
        expect(locator).to_be_enabled(timeout=BasePage._timeout(timeout))

    def click(self, locator: Locator, *, timeout: Optional[float] = None) -> None:
        """Wait for and click one page control."""
        self.wait_until_visible(locator, timeout=timeout)
        self.wait_until_enabled(locator, timeout=timeout)
        locator.click(timeout=self._timeout(timeout))

    def fill(self, locator: Locator, value: str, *, timeout: Optional[float] = None) -> None:
        """Wait for and replace the value of one input."""
        self.wait_until_visible(locator, timeout=timeout)
        self.wait_until_enabled(locator, timeout=timeout)
        locator.fill(value, timeout=self._timeout(timeout))

    def clear(self, locator: Locator, *, timeout: Optional[float] = None) -> None:
        """Clear one input using Playwright's fill semantics."""
        self.fill(locator, "", timeout=timeout)

    def select_option(
        self,
        locator: Locator,
        value: str,
        *,
        timeout: Optional[float] = None,
    ) -> None:
        """Select one option from a native select element."""
        self.wait_until_visible(locator, timeout=timeout)
        self.wait_until_enabled(locator, timeout=timeout)
        locator.select_option(value=value, timeout=self._timeout(timeout))

    @staticmethod
    def get_text(locator: Locator, *, timeout: Optional[float] = None) -> str:
        """Return normalized visible text from one element."""
        resolved_timeout = BasePage._timeout(timeout)
        expect(locator).to_be_visible(timeout=resolved_timeout)
        return locator.inner_text(timeout=resolved_timeout).strip()

    @staticmethod
    def get_value(locator: Locator, *, timeout: Optional[float] = None) -> str:
        """Return the current value of one form control."""
        resolved_timeout = BasePage._timeout(timeout)
        expect(locator).to_be_visible(timeout=resolved_timeout)
        return locator.input_value(timeout=resolved_timeout)
