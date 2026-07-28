"""POM classes for TMS configuration and rule-management pages.

Definitions come from ``knowledge/01_business_domain/bill_definition.md`` and
constraints from ``knowledge/04_constraint_rule/``.
"""

from auto_test.pom.tms.list_page import TmsListPage


class TaskTypePage(TmsListPage):
    PATH = "/task_type_route/tmsTaskTypeRouteList"

    def fill_task_type(self, task_type: str) -> None:
        self.fill_labeled_input("任务类型", task_type)


class ControlAreaLogPage(TmsListPage):
    PATH = "/control_area_log/tmsControlAreaLogList"


class DoorPage(TmsListPage):
    PATH = "/door/tmsDoorList"


class AgvErrorLogPage(TmsListPage):
    PATH = "/tms_agv_error/tmsAgvErrorList"

    def fill_container_code(self, container_code: str) -> None:
        self.fill_labeled_input("容器编码", container_code)

    def fill_task_code(self, task_code: str) -> None:
        self.fill_labeled_input("任务编码", task_code)

    def fill_vehicle_code(self, vehicle_code: str) -> None:
        self.fill_labeled_input("车辆编码", vehicle_code)


class PutawayRulePage(TmsListPage):
    PATH = "/rule_up_config/tmsRuleDictList"

    def fill_rule_code(self, rule_code: str) -> None:
        self.fill_labeled_input("上架规则编码", rule_code)

    def fill_rule_name(self, rule_name: str) -> None:
        self.fill_labeled_input("上架规则名称", rule_name)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class PickingRulePage(TmsListPage):
    PATH = "/rule_down_config/tmsRuleDictList"

    def fill_rule_code(self, rule_code: str) -> None:
        self.fill_labeled_input("下架规则编码", rule_code)

    def fill_rule_name(self, rule_name: str) -> None:
        self.fill_labeled_input("下架规则名称", rule_name)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class StrategyPage(TmsListPage):
    PATH = "/strategy/tmsStrategyList"

    def fill_strategy_name(self, strategy_name: str) -> None:
        self.fill_labeled_input("策略名称", strategy_name)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class ConditionGroupPage(TmsListPage):
    PATH = "/condition-group/tmsConditionalCombinationList"

    def fill_group_code(self, group_code: str) -> None:
        self.fill_labeled_input("条件组编码", group_code)

    def fill_group_name(self, group_name: str) -> None:
        self.fill_labeled_input("条件组名称", group_name)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class RulePage(TmsListPage):
    PATH = "/rule/tmsRuleList"

    def fill_rule_code(self, rule_code: str) -> None:
        self.fill_labeled_input("规则编码", rule_code)

    def fill_rule_name(self, rule_name: str) -> None:
        self.fill_labeled_input("规则名称", rule_name)

    def select_condition_group(self, condition_group: str) -> None:
        self.select_labeled_option("关联条件组", condition_group)

    def select_area(self, area_name: str) -> None:
        self.select_labeled_option("逻辑区", area_name)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class OperationRulePage(TmsListPage):
    PATH = "/tms_operation_rule/tmsOperationRuleList"

    def fill_rule_code(self, rule_code: str) -> None:
        self.fill_labeled_input("操作型规则编码", rule_code)

    def fill_rule_name(self, rule_name: str) -> None:
        self.fill_labeled_input("操作型规则名称", rule_name)

    def fill_condition_group(self, condition_group: str) -> None:
        self.fill_labeled_input("关联条件组", condition_group)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("状态", status)


class TaskGroupPage(TmsListPage):
    PATH = "/task_group/tmsTaskGroupList"

    def fill_task_group_code(self, task_group_code: str) -> None:
        self.fill_labeled_input("任务组编号", task_group_code)

    def fill_start_area(self, area_name: str) -> None:
        self.fill_labeled_input("起始储区名称", area_name)

    def fill_start_location(self, location_code: str) -> None:
        self.fill_labeled_input("起始储位编码", location_code)

    def fill_end_area(self, area_name: str) -> None:
        self.fill_labeled_input("终点储区名称", area_name)

    def fill_end_location(self, location_code: str) -> None:
        self.fill_labeled_input("终点储位编码", location_code)

    def select_status(self, status: str) -> None:
        self.select_labeled_option("任务组状态", status)

    def click_task_group_detail(self, task_group_code: str) -> None:
        self.click_row_action(task_group_code, "详情")
