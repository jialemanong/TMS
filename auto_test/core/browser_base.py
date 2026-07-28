"""Playwright browser foundation without business page locators.

POM and UI scripts must follow ``knowledge/06_auto_test_spec/ui_code_spec.md``.
This class intentionally provides infrastructure operations only.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from playwright.sync_api import Page

from auto_test.utils.logger import get_logger


class BrowserBase:
    """Infrastructure wrapper around a fixture-managed Playwright page."""

    def __init__(self, page: Page, artifact_dir: Path, base_url: str = "") -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.artifact_dir = Path(artifact_dir)
        self.screenshot_dir = self.artifact_dir / "screenshots"
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        self.logger = get_logger("tms.browser")

    def goto(self, path: str = "", *, wait_until: str = "domcontentloaded") -> None:
        """Navigate using the configured UI base URL or an explicit absolute URL."""
        url = self._build_url(path)
        self.logger.info("browser_goto", extra={"event_data": {"url": url}})
        self.page.goto(url, wait_until=wait_until)

    def wait_for_ready(self, *, timeout: Optional[float] = None) -> None:
        """Wait for the document to reach DOM content loaded state."""
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)

    def capture_screenshot(self, name: str, *, full_page: bool = True) -> Path:
        """Capture a named PNG artifact and return its path."""
        safe_name = "".join(character if character.isalnum() or character in "-_" else "_" for character in name)
        screenshot_path = self.screenshot_dir / f"{safe_name}.png"
        self.page.screenshot(path=str(screenshot_path), full_page=full_page)
        self.logger.info(
            "browser_screenshot",
            extra={"event_data": {"path": str(screenshot_path)}},
        )
        return screenshot_path

    def _build_url(self, path: str) -> str:
        if path.startswith(("http://", "https://", "data:", "about:")):
            return path
        if not self.base_url:
            raise ValueError("UI base_url is required for relative navigation")
        return f"{self.base_url}/{path.lstrip('/')}"
