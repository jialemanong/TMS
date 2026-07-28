# TMS AI测试Agent 知识库索引

> 【重要】AI测试Agent查询知识时，必须优先读取本索引，按照路由规则定位对应文档，禁止编造文档不存在的业务规则。
> 规则冲突优先级：约束规则(04) > 状态机(02) > 流程场景(03) > 业务域(01)

## 一、知识库目录结构
```
docs/knowledge/
├── KNOWLEDGE_INDEX.md 本文件【入口索引，优先读取】
├── 01_business_domain/ 业务领域层
├── 02_state_machine/ 状态机层【测试核心】
├── 03_process_scenario/ 业务流程场景
│ ├── main_flow/ 正向主流程
│ └── exception_flow/ 异常中断流程
├── 04_constraint_rule/ 硬性业务约束
├── 05_reference/ 参考资料
│ ├── openapi/ 接口规范、接口明细与测试指南
│ └── database/ 数据库 DDL、字段字典与断言指南
├── 06_auto_test_spec/ 自动化测试编码规范【AI 脚本生成强制标准】
└── test_feedback/ 测试反馈回流【生成用例必须参考】
```

## 二、知识查询路由规则

### 🔹 查询【系统整体架构、模块划分、上下游对接】
→ 读取 `01_business_domain/system_overview.md`
适用场景：
- 了解系统定位、模块组成
- 上下游系统有哪些、交互什么内容
- 核心业务对象关系

### 🔹 查询【业务对象定义、单据概念、核心实体属性】
→ 读取 `01_business_domain/bill_definition.md`
适用场景：
- 需求、容器任务、车辆任务、任务组是什么
- 容器、储位、条件组、规则的定义
- 各对象的状态枚举、核心属性

### 🔹 查询【上下游系统交互逻辑、通信流程】
→ 读取 `01_business_domain/system_interaction.md`
适用场景：
- 明眸/雷达信号触发逻辑
- WMS/MES下发规则
- RCS、门、电梯、广播对接流程
- 异常信号处理

### 🔹 查询【需求状态流转、入池出池规则】
→ 读取 `02_state_machine/demand_flow.md`
适用场景：
- 需求状态有哪些、怎么流转
- 什么条件生成需求、什么条件处理需求
- 需求回退规则

### 🔹 查询【容器任务状态流转、各节点动作】
→ 读取 `02_state_machine/container_task_flow.md`
适用场景：
- 容器任务完整状态链路
- 每个状态变更触发条件
- 任务完成/取消后的资源处理
- 非法跳转禁止操作

### 🔹 查询【车辆任务状态、RCS执行阶段】
→ 读取 `02_state_machine/vehicle_task_flow.md`
适用场景：
- 车辆任务各阶段状态
- 已离开起点、已到达终点对应动作
- 管制区状态子流程

### 🔹 查询【储位状态、容器状态、深度组标识】
→ 读取 `02_state_machine/location_container_flow.md`
适用场景：
- 储位空闲/占用/预占流转
- 容器空/可用/占用中流转
- 容器与储位绑定解绑时机
- 深度组三个标识含义

### 🔹 查询【任务组状态、全局禁止跳转、校验节点】
→ 读取 `02_state_machine/state_transition_matrix.md`
适用场景：
- 任务组状态流转
- 全局状态非法跳转矩阵
- 核心测试校验节点清单
- 深度组并发约束

### 🔹 查询【点对点搬运完整业务流程】
→ 读取 `03_process_scenario/main_flow/point_to_point.md`
适用场景：
- 点对点从创建到完成全步骤
- 各节点校验逻辑
- 需求→任务→调度→执行全链路

### 🔹 查询【点对区搬运流程、终点自动分配逻辑】
→ 读取 `03_process_scenario/main_flow/point_to_area.md`
适用场景：
- 点对区业务逻辑
- 终点储位自动分配规则
- 与点对点的异同

### 🔹 查询【叫料、下料、移库、自动触发搬运流程】
→ 读取 `03_process_scenario/main_flow/call_pick_move.md`
适用场景：
- 叫料上料流程
- 下料流程及后置触发
- 移库触发条件和执行逻辑
- 自动搬运触发规则

### 🔹 查询【所有异常场景、中断流程、回滚逻辑】
→ 读取 `03_process_scenario/exception_flow/all_exception.md`
适用场景：
- 任务取消回滚全流程
- AGV异常回告处理
- 外部信号异常
- 资源不足、并发冲突场景

### 🔹 查询【深度组上下架分配规则、排序逻辑】
→ 读取 `04_constraint_rule/depth_group_rule.md`
适用场景：
- 单进单出、一侧进一侧出模式区别
- 上架储位分配排序优先级
- 下架储位分配排序优先级
- 混放参数影响

### 🔹 查询【取货规则、放货规则、起点终点校验】
→ 读取 `04_constraint_rule/pick_place_rule.md`
适用场景：
- 终点放货校验规则
- 起点取货校验规则
- 不可跳过阻挡规则
- 人工绑定解绑规则

### 🔹 查询【接口约束、数据一致性、幂等性、日志规则】
→ 读取 `04_constraint_rule/data_consistency_rule.md`
适用场景：
- 接口幂等、参数校验规则
- 各对象数据一致性约束
- 日志分类与清理规则
- 并发冲突处理

### 🔹 查询【接口文档、数据库表、环境信息】
→ 读取 `05_reference/reference_notes.md`
适用场景：
- 接口清单分类
- 核心数据库表说明
- 环境地址信息

### 🔹 查询【具体接口URL、方法、请求参数、响应模型】
→ 先读取 `05_reference/openapi/API_OVERVIEW.md`，再按服务进入 `05_reference/openapi/generated/`
适用场景：
- 按业务模块定位接口
- 查询请求参数位置、必填性和字段类型
- 查询响应模型及模型字段
- 生成接口契约测试和自动化脚本

### 🔹 查询【接口自动化策略、通用断言、高风险接口】
→ 读取 `05_reference/openapi/API_TEST_GUIDE.md`
适用场景：
- 设计接口自动化分层
- 补充鉴权、参数、幂等和一致性断言
- 识别系统开关、硬件控制、批量操作等高风险接口

### 🔹 查询【真实数据库表、字段、索引、关联关系】
→ 先读取 `05_reference/database/DATABASE_OVERVIEW.md`，再查询 `05_reference/database/generated/`
适用场景：
- 定位业务对象对应的真实表名
- 查询字段类型、默认值、注释和索引
- 检查物理外键与应用层软关联
- 设计接口和流程的数据库断言

### 🔹 查询【数据库一致性断言、数据质量检查】
→ 读取 `05_reference/database/DATABASE_TEST_GUIDE.md`
适用场景：
- 校验需求、容器任务、车辆任务完整链路
- 校验储位、容器和绑定关系一致性
- 检查孤儿记录、重复编码和非法状态

### 🔹 查询【API自动化代码、接口Fixture、断言和结果回流规范】
→ 生成或修改任何API自动化代码前，必须读取 `06_auto_test_spec/api_code_spec.md`
适用场景：
- 使用统一ApiClient和pytest fixture
- 编写TMS接口测试、参数化测试和业务断言
- 规范请求日志、异常处理和敏感信息脱敏
- 输出可回流 `test_feedback` 的结构化结果
- 约束Codex生成API测试代码的允许范围和禁止事项

### 🔹 查询【UI自动化代码、POM边界、Playwright和Codex生成规范】
→ 人工维护POM或Codex生成UI流程前，必须读取 `06_auto_test_spec/ui_code_spec.md`
适用场景：
- 人工创建和维护TMS页面POM及元素定位
- 使用统一Browser、Context、Page和页面fixture
- 编写截图、录屏、等待和UI断言
- Codex仅在 `test_ui` 编排业务流程
- 发现POM能力缺口并交由人工扩充

### 🔹 自动化代码规则冲突处理
→ `06_auto_test_spec/` 约束代码组织和生成边界；业务预期仍按以下优先级判断：
`04_constraint_rule` > `02_state_machine` > `03_process_scenario` > `01_business_domain`

自动化规范不得覆盖或改写业务规则。知识库没有明确业务信息时，禁止为了生成脚本而自行推断。


### 🔹 查询【历史缺陷、未覆盖场景、自动化优化点】
→ 读取 `test_feedback/` 目录下所有文件
适用场景：
- 生成测试用例前必须参考
- 历史缺陷对应场景必须覆盖
- 已知遗漏场景必须纳入
- 自动化脚本优化点规避

## 三、系统范围边界
### ✅ 本知识库覆盖范围
- 工厂内部AGV搬运调度TMS系统
- 后台管理、服务端核心逻辑
- PAD端、PDA端业务操作
- 上下游系统对接逻辑
- TMS五个服务的Swagger接口契约
- TMS V2数据库179张表的DDL及字段字典
- 所有业务模式：点对点、点对区、叫料、下料、移库
- 深度组规则、任务组规则、规则引擎

### ❌ 不在本知识库范围
- WMS仓储管理系统本身逻辑
- MES生产执行系统本身逻辑
- RCS机器人调度系统内部算法
- 前端UI样式、交互细节
- 非测试相关的运维、部署内容

## 四、Agent行为约束
1. **禁止编造**：知识库中没有的业务规则，禁止自行推断编造，必须标注"知识库未明确说明"
2. **优先级原则**：规则冲突时，约束规则 > 状态机 > 流程文档 > 业务概述
3. **版本说明**：本知识库基于 TMS方案V2.2.0.1-20250615 版本整理
4. **反馈回流**：发现缺失场景，记录到 test_feedback/uncovered_scenario.md
5. **测试生成**：生成测试用例时，必须同时参考主流程 + 异常流程 + 历史缺陷库
6. **编码规范**：生成或修改自动化代码前，必须读取 `06_auto_test_spec/` 对应规范
7. **POM边界**：POM元素定位仅由人工维护；Codex只允许在 `test_ui` 中调用已有POM编排流程
