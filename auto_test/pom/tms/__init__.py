"""TMS page object models.

Element locators in this package require verification against the real TMS UI.
"""
"""Human-maintained TMS page objects."""

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
from auto_test.pom.tms.list_page import TmsListPage
from auto_test.pom.tms.login_page import TmsLoginPage
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
from auto_test.pom.tms.page_registry import TmsPageRegistry
from auto_test.pom.tms.task_pool_page import (
    ContainerTaskPoolPage,
    TaskPoolPage,
    VehicleTaskPoolPage,
)

__all__ = [
    "AgvErrorLogPage",
    "ConditionGroupPage",
    "ContainerTaskPoolPage",
    "ControlAreaLogPage",
    "DataLogPage",
    "DataSourcePage",
    "DemandPoolPage",
    "DoorPage",
    "ExternalSystemLogPage",
    "GatewayRoutePage",
    "OnlineUserPage",
    "OperationRulePage",
    "PickingRulePage",
    "PutawayRulePage",
    "RedisMonitorPage",
    "RequestTracePage",
    "RulePage",
    "ScheduledTaskPage",
    "ServerMonitorPage",
    "SqlMonitorPage",
    "StrategyPage",
    "SystemLogPage",
    "TaskPoolPage",
    "TaskGroupPage",
    "TaskTypePage",
    "TmsConfigPage",
    "TmsListPage",
    "TmsLoginPage",
    "TmsPageRegistry",
    "UpstreamTaskPoolPage",
    "VehicleTaskPoolPage",
]
