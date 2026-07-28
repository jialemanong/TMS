"""Shared list-page primitives for human-maintained TMS page objects.

Locator rules follow ``knowledge/06_auto_test_spec/ui_code_spec.md``.
"""

from __future__ import annotations

from playwright.sync_api import Locator

from auto_test.core.base_page import BasePage


class TmsListPage(BasePage):
    """Provide atomic operations shared by inspected TMS table pages."""

    PATH = ""

    @property
    def result_table(self) -> Locator:
        return self.page.get_by_role("table")

    @property
    def data_rows(self) -> Locator:
        return self.result_table.locator("tbody tr.ant-table-row")

    def open(self, path: str = "") -> None:
        super().open(path or self.PATH)
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.wait_until_visible(self.result_table)

    def fill_labeled_input(self, label: str, value: str) -> None:
        self.fill(self.page.get_by_label(label, exact=True), value)

    def select_labeled_option(self, label: str, option_text: str) -> None:
        form_item = self.page.locator(".ant-form-item").filter(
            has=self.page.get_by_text(label, exact=True)
        )
        self.click(form_item.get_by_role("combobox"))
        self.click(self.page.get_by_role("option", name=option_text, exact=True))

    def click_query(self) -> None:
        self.click(self.page.get_by_role("button", name="查询", exact=True))
        self.wait_until_visible(self.result_table)

    def click_reset(self) -> None:
        self.click(self.page.get_by_role("button", name="重置", exact=True))

    def click_add(self) -> None:
        self.click(self.page.get_by_role("button", name="新增", exact=True))

    def get_row_count(self) -> int:
        return self.data_rows.count()

    def get_row_text(self, unique_text: str) -> str:
        row = self._row(unique_text)
        self.wait_until_visible(row)
        return self.get_text(row)

    def click_row_action(self, unique_text: str, action_name: str) -> None:
        row = self._row(unique_text)
        self.wait_until_visible(row)
        self.click(row.get_by_role("button", name=action_name, exact=True))

    def _row(self, unique_text: str) -> Locator:
        return self.data_rows.filter(has_text=unique_text)
