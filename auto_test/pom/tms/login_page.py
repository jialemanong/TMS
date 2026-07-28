"""TMS login page object.

Locator ownership follows ``knowledge/06_auto_test_spec/ui_code_spec.md``.
Credentials and captcha values must be supplied by fixtures or callers.
"""

from playwright.sync_api import Locator, expect

from auto_test.core.base_page import BasePage


class TmsLoginPage(BasePage):
    """Expose atomic operations for the TMS login page."""

    PATH = "/login"

    @property
    def username_input(self) -> Locator:
        return self.page.get_by_placeholder("账号", exact=True).filter(visible=True)

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_placeholder("密码", exact=True).filter(visible=True)

    @property
    def captcha_input(self) -> Locator:
        return self.page.get_by_placeholder("验证码", exact=True).filter(visible=True)

    @property
    def captcha_image(self) -> Locator:
        return self.page.locator('img[src^="data:image/"]').filter(visible=True)

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="登 录", exact=True)

    def open(self, path: str = PATH) -> None:
        super().open(path)
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.wait_until_visible(self.username_input)
        self.wait_until_visible(self.password_input)
        self.wait_until_visible(self.captcha_input)
        self.wait_until_visible(self.captcha_image)
        self.wait_until_enabled(self.login_button)

    def fill_username(self, username: str) -> None:
        self.fill(self.username_input, username)

    def fill_password(self, password: str) -> None:
        self.fill(self.password_input, password)

    def fill_captcha(self, captcha: str) -> None:
        self.fill(self.captcha_input, captcha)

    def capture_captcha(self) -> bytes:
        self.wait_until_visible(self.captcha_image)
        return self.captcha_image.screenshot(
            timeout=self.DEFAULT_TIMEOUT_MS,
            animations="disabled",
        )

    def refresh_captcha(self) -> None:
        current_source = self.captcha_image.get_attribute("src")
        self.click(self.captcha_image)
        if current_source:
            expect(self.captcha_image).not_to_have_attribute(
                "src",
                current_source,
                timeout=self.DEFAULT_TIMEOUT_MS,
            )

    def click_login(self) -> None:
        self.click(self.login_button)
