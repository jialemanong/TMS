"""Typed registry for all TMS pages visible to the automation account."""

from auto_test.core.browser_base import BrowserBase
from auto_test.pom.tms.basic_management_page import (
    AgvErrorLogPage,
    ConditionGroupPage,
    ControlAreaLogPage,
    DoorPage,
    OperationRulePage,
    PickingRulePage,
    PutawayRulePage,
    RulePage,
    StrategyPage,
    TaskGroupPage,
    TaskTypePage,
)
from auto_test.pom.tms.config_page import TmsConfigPage
from auto_test.pom.tms.demand_page import DemandPoolPage, UpstreamTaskPoolPage
from auto_test.pom.tms.monitor_page import (
    DataLogPage,
    DataSourcePage,
    ExternalSystemLogPage,
    GatewayRoutePage,
    OnlineUserPage,
    RedisMonitorPage,
    RequestTracePage,
    ScheduledTaskPage,
    ServerMonitorPage,
    SqlMonitorPage,
    SystemLogPage,
)
from auto_test.pom.tms.task_pool_page import (
    ContainerTaskPoolPage,
    VehicleTaskPoolPage,
)


class TmsPageRegistry:
    """Expose all page objects over one fixture-managed browser page."""

    def __init__(self, browser: BrowserBase) -> None:
        self.task_type = TaskTypePage(browser)
        self.control_area_log = ControlAreaLogPage(browser)
        self.door = DoorPage(browser)
        self.agv_error_log = AgvErrorLogPage(browser)
        self.putaway_rule = PutawayRulePage(browser)
        self.picking_rule = PickingRulePage(browser)
        self.strategy = StrategyPage(browser)
        self.condition_group = ConditionGroupPage(browser)
        self.rule = RulePage(browser)
        self.operation_rule = OperationRulePage(browser)
        self.task_group = TaskGroupPage(browser)
        self.demand_pool = DemandPoolPage(browser)
        self.upstream_task_pool = UpstreamTaskPoolPage(browser)
        self.container_task_pool = ContainerTaskPoolPage(browser)
        self.vehicle_task_pool = VehicleTaskPoolPage(browser)
        self.system_log = SystemLogPage(browser)
        self.external_system_log = ExternalSystemLogPage(browser)
        self.gateway_route = GatewayRoutePage(browser)
        self.scheduled_task = ScheduledTaskPage(browser)
        self.data_source = DataSourcePage(browser)
        self.data_log = DataLogPage(browser)
        self.sql_monitor = SqlMonitorPage(browser)
        self.server_monitor = ServerMonitorPage(browser)
        self.redis_monitor = RedisMonitorPage(browser)
        self.request_trace = RequestTracePage(browser)
        self.online_user = OnlineUserPage(browser)
        self.config = TmsConfigPage(browser)
