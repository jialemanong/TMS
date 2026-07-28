# TMS V2 数据库知识库总览

> 数据源：MySQL 8.0.41，Schema：`tms_v2`，DDL导出时间：2026-07-28 09:47:54。

## 一、知识库文件

| 文件 | 用途 |
|---|---|
| `raw/tms_v2.sql` | 原始DDL，数据库结构事实源 |
| `generated/ALL_TABLE_INDEX.md` | 179张表的分类、说明和规模索引 |
| `generated/TMS_TABLE_DICTIONARY.md` | 所有TMS业务表的字段、类型、默认值和索引 |
| `generated/PHYSICAL_FOREIGN_KEYS.md` | DDL明确声明的物理外键 |
| `DATABASE_TEST_GUIDE.md` | 接口及流程测试的数据库断言指南 |
| `tools/generate_database_docs.js` | 根据DDL重新生成数据库文档 |

## 二、核心业务表路由

| 业务对象 | 核心表 | 关键用途 |
|---|---|---|
| 需求池 | `tms_demand_poll` | 需求来源、起终点、容器、工序、状态、优先级 |
| 容器任务/任务组 | `tms_task_poll` | 容器任务、父子任务、调度状态、组状态 |
| 车辆任务 | `tms_task` | RCS执行任务、车辆、执行状态 |
| 任务状态历史 | `tms_task_poll_status` | 容器任务状态变化记录 |
| 上游任务 | `tms_task_upstream` | 上游系统任务映射 |
| 任务异常 | `tms_task_abnormal`、`tms_agv_error` | RCS与AGV异常记录 |
| 容器 | `tms_container` | 容器编码、货型、容器状态、业务状态 |
| 储位 | `tms_storage_location` | 储位状态、业务状态、深度组和容量 |
| 储位与容器 | `tms_location_container` | 储位和容器的绑定关系 |
| 储区 | `tms_storage_cavern` | 储区基础信息 |
| 深度组 | `tms_depth_group` | 深度组模式、排序和占用标识 |
| 流程卡 | `tms_flow_card` | 工单、容器、工序及物料信息 |
| 工单 | `tms_work_order` | MES工单信息 |
| 工序/路线 | `tms_process`、`tms_process_route`、`tms_process_route_process` | 工艺路线及工序顺序 |
| 条件与规则 | `tms_condition*`、`tms_rule*`、`tms_strategy*` | 条件组、规则、策略和动作 |
| 设备与事件 | `tms_device*`、`tms_event*` | 设备接口、事件和参数配置 |
| 外部调用日志 | `tms_send_http_log` | 外部请求和响应记录 |
| 管制区日志 | `tms_control_area_log` | 车辆进出管制区记录 |

## 三、核心链路软关联

以下关联来自字段名称和注释，DDL未声明物理外键，使用前应结合代码或数据核验：

```text
tms_demand_poll.task_poll_id
  -> tms_task_poll.id
  -> tms_task.task_poll_id

tms_task_poll.container_id
  -> tms_container.id

tms_task_poll.start_location_id / end_location_id
  -> tms_storage_location.id

tms_location_container.storage_location_id
  -> tms_storage_location.id

tms_location_container.container_id
  -> tms_container.id

tms_flow_card.work_order_id
  -> tms_work_order.id

tms_flow_card.container_id
  -> tms_container.id
```

## 四、重要发现

1. TMS业务表主要依赖应用层软关联，数据库无法通过外键自动防止孤儿数据。
2. DDL包含 `_copy1`、`_copy2`、`_copy3` 备份或临时表，业务查询默认不应使用这些表。
3. `tms_demand_condition` 的表注释明确标记为弃用。
4. 多个状态和业务类型使用字符串字段保存枚举，测试时必须同时校验值和业务含义。
5. 部分字段类型与语义不完全一致，例如编码可能使用 `varbinary`，重量、坐标可能使用 `varchar`。
6. 业务唯一性多数没有唯一索引保护，重复下发和并发写入需要重点测试。
