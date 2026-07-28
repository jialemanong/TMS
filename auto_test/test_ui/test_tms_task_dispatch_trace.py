"""TMS container-to-vehicle task trace UI scenario."""

from __future__ import annotations

from typing import Any

import pytest

from auto_test.pom.tms import TmsPageRegistry

CONTAINER_TASK_STATUSES = {"创建", "待执行", "执行中", "完成", "取消", "中止"}
CONTAINER_STATUS_DISPLAY_MAP = {"已完成": "完成"}
VEHICLE_TASK_STATUSES = {
    "已创建",
    "已下发",
    "已离开起点",
    "已到达终点",
    "已完成",
    "已取消",
    "异常",
}


def _normalize_container_status(display_status: str) -> str:
    """Map the inspected UI terminal label to the knowledge state name."""
    return CONTAINER_STATUS_DISPLAY_MAP.get(display_status, display_status)


@pytest.mark.ui_tms
@pytest.mark.e2e
@pytest.mark.knowledge(
    "knowledge/01_business_domain/bill_definition.md",
    "knowledge/02_state_machine/container_task_flow.md",
    "knowledge/02_state_machine/vehicle_task_flow.md",
    "knowledge/03_process_scenario/main_flow/point_to_point.md",
)
@pytest.mark.scenario("容器任务完成调度后可在车辆任务池追踪同一容器")
def test_container_task_dispatch_to_vehicle_task_is_traceable(
    tms_pages: TmsPageRegistry,
    task_dispatch_data: dict[str, Any],
) -> None:
    """场景：追踪容器任务到车辆任务；前置：测试数据已完成车辆分配；预期：两级任务均可查询且关联同一容器。"""
    task_data = task_dispatch_data

    # Given：容器任务由需求匹配规则生成。
    # 依据：knowledge/01_business_domain/bill_definition.md
    container_page = tms_pages.container_task_pool
    container_page.open()

    # When：按容器任务编号和容器编码查询容器任务。
    # 依据：knowledge/02_state_machine/container_task_flow.md
    container_page.fill_task_code(task_data["container_task_code"])
    container_page.fill_container_code(task_data["container_code"])
    container_page.click_query()
    container_row = container_page.get_task_row_text(
        task_data["container_task_code"]
    )

    # Then：容器任务存在，且容器和状态符合知识库定义。
    assert (
        _normalize_container_status(task_data["container_status"])
        in CONTAINER_TASK_STATUSES
    )
    assert task_data["container_task_code"] in container_row
    assert task_data["container_code"] in container_row
    assert task_data["container_status"] in container_row

    # Given：容器任务分配车辆后生成车辆任务并下发RCS。
    # 依据：knowledge/03_process_scenario/main_flow/point_to_point.md
    vehicle_page = tms_pages.vehicle_task_pool
    vehicle_page.open()

    # When：按车辆任务编号和同一容器编码查询车辆任务。
    # 依据：knowledge/02_state_machine/vehicle_task_flow.md
    vehicle_page.fill_task_code(task_data["vehicle_task_code"])
    vehicle_page.fill_container_code(task_data["container_code"])
    vehicle_page.click_query()
    vehicle_row = vehicle_page.get_task_row_text(task_data["vehicle_task_code"])

    # Then：车辆任务存在，并与容器任务关联同一容器且状态合法。
    assert task_data["vehicle_status"] in VEHICLE_TASK_STATUSES
    assert task_data["vehicle_task_code"] in vehicle_row
    assert task_data["container_code"] in vehicle_row
    assert task_data["vehicle_status"] in vehicle_row
