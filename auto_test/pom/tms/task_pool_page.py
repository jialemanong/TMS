"""Page objects for the TMS container and vehicle task pools.

Business terminology and states are defined by:
``knowledge/01_business_domain/bill_definition.md``,
``knowledge/02_state_machine/container_task_flow.md`` and
``knowledge/02_state_machine/vehicle_task_flow.md``.

This module contains locators and atomic page operations only. It intentionally
does not encode task creation, dispatch, completion, cancellation, or any other
cross-page business flow.
"""

from __future__ import annotations

from playwright.sync_api import Locator, expect

from auto_test.core.base_page import BasePage


class TaskPoolPage(BasePage):
    """Shared atomic operations exposed by TMS task-pool pages."""

    PATH = ""
    PAGE_TITLE = ""
    STATUS_LABEL = ""

    @property
    def task_code_input(self) -> Locator:
        return self.page.get_by_label("任务编号", exact=True)

    @property
    def container_code_input(self) -> Locator:
        return self.page.get_by_label("容器编码", exact=True)

    @property
    def start_area_input(self) -> Locator:
        return self.page.get_by_label("起始储区名称", exact=True)

    @property
    def start_location_input(self) -> Locator:
        return self.page.get_by_label("起始储位编码", exact=True)

    @property
    def end_area_input(self) -> Locator:
        return self.page.get_by_label("终点储区名称", exact=True)

    @property
    def end_location_input(self) -> Locator:
        return self.page.get_by_label("终点储位编码", exact=True)

    @property
    def query_button(self) -> Locator:
        return self.page.get_by_role("button", name="查询", exact=True)

    @property
    def reset_button(self) -> Locator:
        return self.page.get_by_role("button", name="重置", exact=True)

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
        """Wait for the stable query controls and result table."""
        self.wait_until_visible(
            self.page.locator(".jeecg-basic-table-title").get_by_text(
                self.PAGE_TITLE,
                exact=True,
            )
        )
        self.wait_until_enabled(self.query_button)
        self.wait_until_enabled(self.reset_button)
        self.wait_until_visible(self.result_table)

    def fill_task_code(self, task_code: str) -> None:
        self.fill(self.task_code_input, task_code)

    def fill_container_code(self, container_code: str) -> None:
        self.fill(self.container_code_input, container_code)

    def fill_start_area(self, area_name: str) -> None:
        self.fill(self.start_area_input, area_name)

    def fill_start_location(self, location_code: str) -> None:
        self.fill(self.start_location_input, location_code)

    def fill_end_area(self, area_name: str) -> None:
        self.fill(self.end_area_input, area_name)

    def fill_end_location(self, location_code: str) -> None:
        self.fill(self.end_location_input, location_code)

    def select_condition_group(self, condition_group: str) -> None:
        self._select_ant_option("关联条件组编码", condition_group)

    def select_status(self, status: str) -> None:
        self._select_ant_option(self.STATUS_LABEL, status)

    def click_query(self) -> None:
        self.click(self.query_button)
        self.wait_until_visible(self.result_table)

    def click_reset(self) -> None:
        self.click(self.reset_button)
        expect(self.task_code_input).to_have_value("")
        expect(self.container_code_input).to_have_value("")

    def get_task_row_text(self, task_code: str) -> str:
        row = self._task_row(task_code)
        self.wait_until_visible(row)
        return self.get_text(row)

    def get_task_count(self) -> int:
        return self.data_rows.count()

    def _task_row(self, task_code: str) -> Locator:
        return self.data_rows.filter(has_text=task_code)

    def _select_ant_option(self, field_label: str, option_text: str) -> None:
        """Select one option from the inspected Ant Design form control."""
        form_item = self.page.locator(".ant-form-item").filter(
            has=self.page.get_by_text(field_label, exact=True)
        )
        combobox = form_item.get_by_role("combobox")
        self.click(combobox)
        option = self.page.get_by_role("option", name=option_text, exact=True)
        self.click(option)


class ContainerTaskPoolPage(TaskPoolPage):
    """Atomic page object for the TMS container task pool."""

    PATH = "/task_pool/tmsTaskPollList"
    PAGE_TITLE = "容器任务池管理"
    STATUS_LABEL = "任务状态"


class VehicleTaskPoolPage(TaskPoolPage):
    """Atomic page object for the TMS vehicle task pool."""

    PATH = "/vehicle-task/tmsTaskList"
    PAGE_TITLE = "车辆任务池管理"
    STATUS_LABEL = "状态"

    @property
    def vehicle_id_input(self) -> Locator:
        return self.page.get_by_label("车辆ID", exact=True)

    def fill_vehicle_id(self, vehicle_id: str) -> None:
        self.fill(self.vehicle_id_input, vehicle_id)

    def click_task_detail(self, task_code: str) -> None:
        """Open the detail view for one uniquely identified task row."""
        row = self._task_row(task_code)
        self.wait_until_visible(row)
        self.click(row.get_by_role("button", name="详情", exact=True))
