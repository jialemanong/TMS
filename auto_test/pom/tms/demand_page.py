"""POM classes for TMS demand and upstream task pools.

See ``knowledge/02_state_machine/demand_flow.md`` and
``knowledge/01_business_domain/bill_definition.md``.
"""

from auto_test.pom.tms.list_page import TmsListPage
from auto_test.pom.tms.task_pool_page import TaskPoolPage


class DemandPoolPage(TmsListPage):
    PATH = "/demand_poll/tmsDemandPollList"

    def fill_flow_card_code(self, flow_card_code: str) -> None:
        self.fill_labeled_input("流程卡号", flow_card_code)

    def fill_work_order(self, work_order: str) -> None:
        self.fill_labeled_input("工单", work_order)

    def fill_upstream_business_code(self, business_code: str) -> None:
        self.fill_labeled_input("上游业务号", business_code)

    def click_demand_detail(self, demand_code: str) -> None:
        self.click_row_action(demand_code, "详情")


class UpstreamTaskPoolPage(TaskPoolPage):
    PATH = "/task_upstream/tmsTaskUpstreamList"
    PAGE_TITLE = "上游任务池管理"
    STATUS_LABEL = "任务状态"
