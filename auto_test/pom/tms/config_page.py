"""POM for TMS runtime parameter configuration.

Parameter effects must follow the knowledge documents routed by
``knowledge/KNOWLEDGE_INDEX.md``; this class only exposes atomic UI actions.
"""

from playwright.sync_api import Locator

from auto_test.core.base_page import BasePage


class TmsConfigPage(BasePage):
    PATH = "/tms-config/tmsConfigList"

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="提交", exact=True)

    @property
    def reset_button(self) -> Locator:
        return self.page.get_by_role("button", name="重置", exact=True)

    def open(self, path: str = PATH) -> None:
        super().open(path)
        self.wait_until_enabled(self.submit_button)
        self.wait_until_enabled(self.reset_button)

    def select_option(self, option_text: str) -> None:
        self.click(self.page.get_by_text(option_text, exact=True))

    def fill_cancel_hours(self, hours: str) -> None:
        self.fill(
            self.page.get_by_placeholder("取消的需求时间(小时以前)", exact=True),
            hours,
        )

    def click_submit(self) -> None:
        self.click(self.submit_button)

    def click_reset(self) -> None:
        self.click(self.reset_button)
