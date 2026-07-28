# 参考资料说明

## 一、OpenAPI接口文档

### 文档入口与本地归档
- 在线文档：`http://111.160.91.170:59999/#/home`
- 汇总入口：`openapi/API_OVERVIEW.md`
- 自动化指南：`openapi/API_TEST_GUIDE.md`
- 原始Swagger：`openapi/raw/*.swagger.json`
- 可检索明细：`openapi/generated/*.md`
- 生成工具：`openapi/tools/generate_api_docs.js`

### 已归档服务
| 服务 | 业务定位 | 接口操作数 |
|---|---|---:|
| jeecg-tms | TMS核心后台、基础数据、任务、规则、配置 | 327 |
| jeecg-tms-api | PAD/PDA、MES/WMS/WCS、AGV、提升机 | 109 |
| jeecg-camera | 摄像头/明眸 | 2 |
| jeecg-radar | 雷达、RFID、报警灯 | 17 |
| jeecg-system | 登录、权限、数据字典、系统能力 | 95 |

合计495条路径、550个接口操作、368个数据模型。

### 核心接口分类
#### 上游接口（入站）
1. WMS任务下发接口
2. MES工单/工序同步接口
3. 明眸检测信号回调接口
4. 雷达检测信号回调接口
5. PAD/PDA操作接口
6. 后台管理CRUD接口

#### 下游接口（出站）
1. RCS任务下发接口
2. RCS管制区授权接口
3. 自动门控制接口
4. 电梯控制接口
5. 广播系统接口

### 其他参考资料
- 数据字典在线文档：https://docs.qq.com/sheet/DZUFvUE5oRW9TdEZS?tab=BB08J2

---

## 二、核心数据库表

### 数据库归档
- 数据库：MySQL 8.0.41 / `tms_v2`
- 总览：`database/DATABASE_OVERVIEW.md`
- 原始DDL：`database/raw/tms_v2.sql`
- 全表索引：`database/generated/ALL_TABLE_INDEX.md`
- TMS字段字典：`database/generated/TMS_TABLE_DICTIONARY.md`
- 物理外键：`database/generated/PHYSICAL_FOREIGN_KEYS.md`
- 测试指南：`database/DATABASE_TEST_GUIDE.md`

### 核心业务表
| 表名 | 说明 | 关键字段 |
|------|------|----------|
| tms_demand_poll | 需求池 | 需求ID、来源、起终点、容器、状态、优先级 |
| tms_task_poll | 容器任务池与任务组 | 任务编号、父任务、容器、起终点、状态、组状态 |
| tms_task | TMS车辆任务 | 任务编号、任务池ID、车辆、起终点、状态 |
| tms_task_poll_status | 容器任务状态历史 | 任务池ID、状态、创建时间 |
| tms_container | 容器管理 | 容器编码、容器状态、业务状态、货型 |
| tms_storage_location | 储位管理 | 储位编码、状态、业务状态、储区、深度组 |
| tms_location_container | 储位容器关系 | 储位ID、容器ID及绑定信息 |
| tms_depth_group | 深度组 | 深度组编码、类型、排序和占用标识 |
| tms_flow_card | 流程卡 | 工单、容器、工序、物料和业务标识 |
| tms_work_order | 工单 | 工单业务信息 |
| tms_condition_group | 条件组 | 条件组配置 |
| tms_rule | 规则 | 条件与业务规则配置 |
| tms_control_area_log | 管制区日志 | 车辆、管制区、任务编码和进出时间 |
| tms_send_http_log | 外部系统调用日志 | 请求与响应信息 |

### 配置表
- 仓库、储区、逻辑区配置表
- 车辆、车型、车辆分组表
- 路由配置表
- 工序、工艺路线、工单表
- 参数配置表
- 用户、角色、权限表

---

## 三、环境信息
> 待补充：各环境地址、账号信息

### 环境清单
- 开发环境
- 测试环境
- 预发布环境
- 生产环境

### 访问方式
- 后台管理地址
- PAD端地址
- PDA端地址
- 接口服务地址
- 数据库连接信息

---

## 四、补充说明
1. 本目录存放参考性资料，不作为业务规则判断依据
2. 业务规则、状态流转、流程逻辑以02、03、04目录文档为准
3. 接口字段以 `openapi/raw/` 中的Swagger规范为准，业务规则仍以01至04目录为准
4. 数据库字段以 `database/raw/tms_v2.sql` 为准；跨表软关联需要结合代码或实际数据确认
