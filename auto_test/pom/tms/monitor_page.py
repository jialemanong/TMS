"""POM classes for the visible TMS log and monitoring pages.

Logging rules are documented in
``knowledge/04_constraint_rule/data_consistency_rule.md``.
"""

from playwright.sync_api import Locator

from auto_test.core.base_page import BasePage
from auto_test.pom.tms.list_page import TmsListPage


class SystemLogPage(TmsListPage):
    PATH = "/monitor/log"


class ExternalSystemLogPage(TmsListPage):
    PATH = "/monitor/external-log/tmsSendHttpLogList"


class GatewayRoutePage(TmsListPage):
    PATH = "/monitor/route"


class ScheduledTaskPage(TmsListPage):
    PATH = "/monitor/quartz"


class DataSourcePage(TmsListPage):
    PATH = "/monitor/datasource"


class DataLogPage(TmsListPage):
    PATH = "/monitor/datalog"


class SqlMonitorPage(BasePage):
    PATH = "/monitor/druid"

    @property
    def monitor_frame(self) -> Locator:
        return self.page.locator("iframe")

    def open(self, path: str = PATH) -> None:
        super().open(path)
        self.wait_until_visible(self.monitor_frame)


class ServerMonitorPage(TmsListPage):
    PATH = "/monitor/server"


class RedisMonitorPage(TmsListPage):
    PATH = "/monitor/redis"


class RequestTracePage(TmsListPage):
    PATH = "/monitor/trace"


class OnlineUserPage(TmsListPage):
    PATH = "/system/onlineuser"

    def fill_username(self, username: str) -> None:
        self.fill_labeled_input("用户账号", username)

    def click_force_logout(self, username: str) -> None:
        self.click_row_action(username, "强退")
