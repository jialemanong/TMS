# TMS 数据库测试断言指南

## 一、断言原则

1. 接口响应成功后，继续校验核心业务表、关联对象、状态历史和外部调用日志。
2. 业务表多数没有物理外键，必须主动检查孤儿记录和软关联一致性。
3. 不直接修改生产数据库；自动化准备和清理数据仅允许在明确的测试环境执行。
4. 状态值以DDL注释、状态机文档和实际代码共同确认；发生冲突时记录差异，不自行选择。

## 二、主流程断言

| 业务节点 | 主表 | 重点字段 |
|---|---|---|
| 创建需求 | `tms_demand_poll` | `demand_id`、`demand_type`、`status`、起终点、`container_id` |
| 生成容器任务 | `tms_task_poll` | `task_code`、`pid_code`、`status`、`group_status`、`dispatch` |
| 生成车辆任务 | `tms_task` | `task_code`、`task_poll_id`、`vehicle_code`、`status` |
| 状态变化 | `tms_task_poll_status` | `task_poll_id`、`status`、`create_time` |
| 绑定容器储位 | `tms_location_container` | 储位ID、容器ID、绑定状态 |
| 更新资源状态 | `tms_storage_location`、`tms_container` | 业务状态、占用状态、绑定时间 |
| 调用外部系统 | `tms_send_http_log` | 请求地址、请求体、响应体、调用时间 |
| 异常处理 | `tms_task_abnormal`、`tms_agv_error` | 任务编码、异常类型、异常内容 |

## 三、一致性检查

### 需求与任务

- 已处理需求应存在对应的 `task_poll_id`。
- `tms_demand_poll.task_poll_id` 应能定位到 `tms_task_poll.id`。
- 容器任务生成车辆任务后，应能通过 `tms_task.task_poll_id` 反查。
- 取消或失败场景不能残留错误的调度状态和资源占用。

### 储位与容器

- 有效绑定记录中的储位和容器必须真实存在。
- 同一容器不应同时绑定多个有效储位。
- 储位占用状态、容器业务状态和绑定记录应一致。
- 解绑后应同步更新解绑时间和资源状态。

### 状态历史

- 状态历史应按时间单调递增。
- 最新历史状态应与任务主表当前状态一致。
- 禁止出现状态机文档定义之外的跳转。

## 四、数据质量检查

- 业务编码为空或重复。
- `_id` 字段引用不存在的记录。
- 已删除对象仍被有效任务引用。
- 已完成/取消任务仍占用储位、容器、车辆或管制区。
- 枚举字段出现DDL注释未定义的值。
- 字符串数值字段包含无法转换的数据。
- `create_time` 晚于 `update_time`，或完成时间早于下发时间。

## 五、接口与表的联合定位

接口属于哪个控制器，可先在 `../openapi/API_OVERVIEW.md` 定位；请求和响应字段再与本目录的TMS字段字典交叉检索。Swagger模型名与表名不保证一一对应，不能只凭名称直接建立映射。

