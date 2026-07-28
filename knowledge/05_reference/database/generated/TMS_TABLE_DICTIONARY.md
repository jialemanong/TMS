# TMS 业务表字段字典



> 本文由 `tools/generate_database_docs.js` 根据 `raw/tms_v2.sql` 自动生成，请勿手工修改。



共 80 张 TMS 业务表。数据库仅对少量框架表声明物理外键；TMS业务表字段关联通常由应用层维护。



## tms_agv_error

- 表说明：AGV异常管理
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| req_code | varchar(32) | 是 | NULL | 否 | RCS请求编码 |
| type | tinyint(1) | 是 | NULL | 否 | 操作类型: 1 取消, 2 完成 |
| container_code | varchar(32) | 是 | NULL | 否 | 容器编码 |
| task_code | varchar(32) | 是 | NULL | 否 | 任务编码 |
| agv_code | varchar(32) | 是 | NULL | 否 | 车辆编码 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(32) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_broadcast_speech

- 表说明：广播语
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 | 主键 |
| name | varchar(255) | 是 | NULL | 否 | 广播语名称 |
| code | varchar(255) | 是 | NULL | 否 | 广播语编码 |
| template_id | varchar(255) | 是 | NULL | 否 | 广播模板ID |
| status | varchar(255) | 是 | NULL | 否 | 状态：0 禁用，1 启用 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| sys_org_code | varchar(255) | 是 | NULL | 否 | 所属部门 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_broadcast_template

- 表说明：广播模板
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 | 主键 |
| name | varchar(255) | 是 | NULL | 否 | 模板名称 |
| code | varchar(255) | 是 | NULL | 否 | 模板编码 |
| content | varchar(255) | 是 | NULL | 否 | 模板内容 |
| status | varchar(255) | 是 | NULL | 否 | 状态：0 禁用，1 启用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |
| sys_org_code | varchar(255) | 是 | NULL | 否 | 所属部门 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_components

- 表说明：部件主数据
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 部件编码 |
| name | varchar(255) | 是 | NULL | 否 | 部件名称 |
| status | tinyint | 是 | NULL | 否 | 状态(0 禁用, 1 启用) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_condition

- 表说明：条件组条件明细表
- 存储引擎：InnoDB
- 字段数：14

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| condition_group_id | varchar(50) | 是 | NULL | 否 | 所属条件分组ID |
| condition_key | varchar(255) | 是 | NULL | 否 | 条件key：(表名,字段, |
| condition_base_operator | varchar(50) | 是 | NULL | 否 | 条件运算符(等于、加、减、乘、除、余数、IF、左括号、右括号、与、或、非、包含) |
| condition_value | varchar(255) | 是 | NULL | 否 | 条件值 |
| condition_logical_operator | varchar(50) | 是 | '&' | 否 | 与、或 |
| sort | int | 是 | NULL | 否 | 排序，或相关时起作用，判断条件优先级 |
| conditional_combination_id | varchar(50) | 是 | NULL | 否 | 所属条件组ID |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| is_query_database | varchar(10) | 是 | '1' | 否 | 是否查询数据库：1 是，2 否 |
| query_demand | char(1) | 是 | NULL | 否 | 是否根据需求查询匹配条件：1是，2否 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_condition_combination_id | 否 | `conditional_combination_id` |


## tms_condition_group

- 表说明：条件分组
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| conditional_combination_id | varchar(50) | 是 | NULL | 否 | 所属条件组ID |
| parent_id | varchar(50) | 是 | NULL | 否 | 父分组ID |
| sort | int | 是 | NULL | 否 | 排序 |
| condition_logical_operator | varchar(50) | 是 | NULL | 否 | 与、或 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_group_combination_id | 否 | `conditional_combination_id` |


## tms_condition_table

- 表说明：TMS条件+规则的模块+字段设置
- 存储引擎：InnoDB
- 字段数：6

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | int | 否 | - | 是 | id |
| condition_table_code | varchar(255) | 是 | NULL | 否 | 表名 |
| condition_table_name | varchar(255) | 是 | NULL | 否 | 表描述 |
| is_table | int | 是 | NULL | 否 | 是否是真实表：1是，2不是 |
| status | int | 是 | NULL | 否 | 状态：1启用，2禁用 |
| type | int | 是 | NULL | 否 | 所属 1 条件组 2 规则 3 条件组+规则 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| condition_table_code | 是 | `condition_table_code` |
| idx_table_code | 否 | `condition_table_code` |


## tms_condition_table_column

- 表说明：TMS条件+规则字段配置表
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | int | 否 | - | 是 | 字段id |
| condition_table_id | int | 是 | NULL | 否 | 表id |
| column_code | varchar(255) | 是 | NULL | 否 | 字段code |
| column_name | varchar(255) | 是 | NULL | 否 | 字段名称 |
| is_dict | int | 是 | NULL | 否 | 是否来源于字典：1是，2否 |
| column_dict_data | varchar(255) | 是 | NULL | 否 | 数据来源：字典对应的码 |
| status | int | 是 | '1' | 否 | 状态：1启用，2禁用 |
| query_demand | char(1) | 是 | NULL | 否 | 是否根据需求查询匹配条件：1是，2否 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_table_column_query | 否 | `condition_table_id`,`column_code`,`query_demand` |


## tms_conditional_combination

- 表说明：条件组主表
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| code | varchar(50) | 是 | NULL | 否 | 条件组编码 |
| name | varchar(50) | 是 | NULL | 否 | 条件组名称 |
| status | varchar(50) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_config

- 表说明：系统参数表
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| param_key | varchar(255) | 是 | NULL | 否 | 参数key |
| param_value | text | 是 | - | 否 | 参数值 |
| remark | varchar(255) | 是 | NULL | 否 | 描述 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| is_show | varchar(255) | 是 | NULL | 否 | 1 显示，2 不显示 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_container

- 表说明：容器管理
- 存储引擎：InnoDB
- 字段数：16

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| container_code | varchar(255) | 是 | NULL | 否 | 容器编码 |
| container_good | varchar(255) | 是 | NULL | 否 | 容器商品 |
| container_weight | varchar(32) | 是 | NULL | 否 | 容器重量 |
| container_quantity | int | 是 | NULL | 否 | 容器数量 |
| container_status | varchar(32) | 是 | NULL | 否 | 容器状态：0 空，1 满，2 满+1（该状态已停用） |
| business_status | varchar(50) | 是 | NULL | 否 | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| goods_type_id | varchar(36) | 是 | NULL | 否 | 货型id |
| process_flag | varchar(255) | 是 | NULL | 否 | 工序标：0 镭射过油，1 丝印，2 翻纸工序，3 打包工序，4 首件签样，5 复合工序，6 单凹工序，7 切纸工序，8 模切工序，9 机检工序， 10 烫金工序，11 凹印工序，12 胶印工序，13 模切工序，14 打包工序 |
| order_flag | varchar(255) | 是 | NULL | 否 | 工单标 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| deleted | tinyint | 是 | '0' | 否 | 1-已删除，0未删除 |
| company_id | varchar(255) | 是 | NULL | 否 | 公司ID |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_control_area_log

- 表说明：管制区任务指令
- 存储引擎：InnoDB
- 字段数：13

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| req_code | varchar(32) | 是 | NULL | 否 | 请求编码 |
| vehicle_id | varchar(32) | 是 | NULL | 否 | 车辆ID |
| control_area_id | varchar(32) | 是 | NULL | 否 | 管制区ID |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 请求进入，2 已进入，3 已退出管制区 |
| task_code | varchar(255) | 是 | NULL | 否 | 任务请求编码(海康管制区所需) |
| enter_time | datetime | 是 | NULL | 否 | 进入时间 |
| quit_time | datetime | 是 | NULL | 否 | 退出时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| sys_org_code | varchar(64) | 是 | NULL | 否 |  |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_demand_condition

- 表说明：弃用----记录需求池条件表(标识需求配置)
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1 |
| flag_two | varchar(255) | 是 | NULL | 否 | 标识2 |
| flag_three | varchar(255) | 是 | NULL | 否 | 标识3 |
| flag_five | varchar(255) | 是 | NULL | 否 | 标识5 |
| storage_location_ids | longtext | 是 | - | 否 | 储位范围ID，逗号拼接 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_demand_poll

- 表说明：【需求池】
- 存储引擎：InnoDB
- 字段数：83

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 | 需求数据来源：1移库,2点对点3工序标识4容器标识5下料6上料,7点对区,8明眸 |
| demand_id | varchar(32) | 是 | NULL | 否 | 需求ID |
| current_storage_location_id | varchar(32) | 是 | NULL | 否 | 当前储位ID |
| current_storage_location_business_id | varchar(32) | 是 | NULL | 否 | 当前储位业务ID |
| current_storage_location_code | varchar(255) | 是 | NULL | 否 | 当前储位编码 |
| current_storage_cavern_id | varchar(255) | 是 | NULL | 否 | 当前储区ID |
| current_storage_cavern_business_id | varchar(255) | 是 | NULL | 否 | 当前储区业务ID |
| current_storage_cavern_code | varchar(255) | 是 | NULL | 否 | 当前储区编码 |
| current_logical_area_id | varchar(255) | 是 | NULL | 否 | 当前逻辑区 |
| current_logical_area_code | varchar(255) | 是 | NULL | 否 | 当前逻辑区编码 |
| target_storage_location_id | varchar(32) | 是 | NULL | 否 | 目标储位ID |
| target_storage_location_business_id | varchar(32) | 是 | NULL | 否 | 目标储位业务ID |
| target_storage_location_code | varchar(255) | 是 | NULL | 否 | 目标储位编码 |
| target_storage_cavern_id | varchar(32) | 是 | NULL | 否 | 目标储区ID |
| target_storage_cavern_business_id | varchar(255) | 是 | NULL | 否 | 目标储区业务ID |
| target_storage_cavern_code | varchar(255) | 是 | NULL | 否 | 目标储区编码 |
| target_logical_area_id | varchar(32) | 是 | NULL | 否 | 目标逻辑区ID |
| target_logical_area_code | varchar(255) | 是 | NULL | 否 | 目标逻辑区编码 |
| goods_type_id | varchar(64) | 是 | NULL | 否 | 货型ID |
| goods_type_code | varchar(255) | 是 | NULL | 否 | 货型编码 |
| pattern | varchar(10) | 是 | NULL | 否 | 模式：1 上料，2 下料，4 移动 |
| flow_card_id | varchar(32) | 是 | NULL | 否 | 流程卡ID |
| flow_card_num | varchar(255) | 是 | NULL | 否 | 流程卡号 |
| current_process_id | varchar(32) | 是 | NULL | 否 | 当前工序ID |
| container_id | varchar(255) | 是 | NULL | 否 | 容器ID |
| container_code | varbinary(255) | 是 | NULL | 否 | 容器编号 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 待处理，2 已处理，3 已取消 |
| remark | varchar(255) | 是 | NULL | 否 | 显示失败原因等等 |
| work_order | varchar(255) | 是 | NULL | 否 | 工单编码 |
| last_process_id | varchar(255) | 是 | NULL | 否 | 上工序ID |
| last_process_code | varchar(255) | 是 | NULL | 否 | 上工序编码 |
| this_process_id | varchar(255) | 是 | NULL | 否 | 本工序ID |
| this_process_code | varchar(255) | 是 | NULL | 否 | 本工序编码 |
| next_process_id | varchar(255) | 是 | NULL | 否 | 下工序ID |
| next_process_code | varchar(255) | 是 | NULL | 否 | 下工序编码 |
| target_machine_id | varchar(32) | 是 | NULL | 否 | 目的机台ID |
| current_machine_id | varchar(255) | 是 | NULL | 否 | 当前机台ID |
| item_id | varchar(32) | 是 | NULL | 否 | 物料ID |
| item_code | varchar(255) | 是 | NULL | 否 | 物料编码 |
| item_qty | int | 是 | NULL | 否 | 物料数量 |
| item_character | varchar(255) | 是 | NULL | 否 | 物料特性 |
| priority | int | 是 | NULL | 否 | 优先级 |
| sort | int | 是 | NULL | 否 | 排序：本系统定义/承接上层系统 |
| upstream_task_no | varchar(255) | 是 | NULL | 否 | 上层系统任务单号 |
| task_type | varchar(255) | 是 | NULL | 否 | 任务类型/单据类型：承接上层系统/ move，camera，relay |
| task_poll_id | varchar(255) | 是 | NULL | 否 | 容器任务池任务ID |
| command_source_system | varchar(255) | 是 | NULL | 否 | 指令来源系统 |
| vehicle_code | varchar(32) | 是 | NULL | 否 | 车辆编号 |
| cancel_task_system | varchar(255) | 是 | NULL | 否 | 取消任务系统 |
| date_in_produced | datetime | 是 | NULL | 否 | 生产日期 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime(3) | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| cancel_time | datetime | 是 | NULL | 否 | 需求取消时间 |
| sys_org_code | varchar(64) | 是 | NULL | 否 | 所属部门 |
| demand_type | varchar(255) | 是 | '0' | 否 | 需求数据来源：1移库,2点对点3工序标识4容器标识5下料6上料,7点对区,8明眸 |
| category | varchar(10) | 是 | NULL | 否 | 需求类型，1-任务型，2-操作型 |
| comment | varchar(255) | 是 | NULL | 否 | 备注 |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1 |
| flag_two | varchar(255) | 是 | NULL | 否 | 标识2 |
| flag_three | varchar(255) | 是 | NULL | 否 | 标识3 |
| flag_four | varchar(255) | 是 | NULL | 否 | 标识4 |
| flag_five | varchar(255) | 是 | NULL | 否 | 标识5 |
| flag_six | varchar(255) | 是 | NULL | 否 | 标识6 |
| flag_seven | varchar(255) | 是 | NULL | 否 | 标识7 |
| flag_eight | varchar(255) | 是 | NULL | 否 | 标识8 |
| flag_nine | varchar(255) | 是 | NULL | 否 | 标识9 |
| flag_ten | varchar(255) | 是 | NULL | 否 | 标识10 |
| flag_eleven | varchar(255) | 是 | NULL | 否 | 标识11 |
| flag_twelve | varchar(255) | 是 | NULL | 否 | 标识12 |
| flag_thirteen | varchar(255) | 是 | NULL | 否 | 标识13 |
| flag_fourteen | varchar(255) | 是 | NULL | 否 | 标识14 |
| flag_fifteen | varchar(255) | 是 | NULL | 否 | 标识15 |
| flag_sixteen | varchar(255) | 是 | NULL | 否 | 标识16 |
| flag_seventeen | varchar(255) | 是 | NULL | 否 | 标识17 |
| flag_eighteen | varchar(255) | 是 | NULL | 否 | 标识18 |
| flag_nineteen | varchar(255) | 是 | NULL | 否 | 标识19 |
| flag_twenty | varchar(255) | 是 | NULL | 否 | 标识20 |
| flag_twenty_one | varchar(255) | 是 | NULL | 否 | 标识21 |
| print_number | varchar(255) | 是 | NULL | 否 | 印号 |
| sub_print_number | varchar(255) | 是 | NULL | 否 | 辅号 |
| doc_type | varchar(255) | 是 | NULL | 否 | 单据类型 move，camera，relay---弃用 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_depth_group

- 表说明：深度组管理
- 存储引擎：InnoDB
- 字段数：21

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| depth_group_code | varchar(255) | 是 | NULL | 否 | 深度组编码 |
| storage_location_id | varchar(32) | 是 | NULL | 否 | 库位ID |
| depth_one | int | 是 | NULL | 否 | 深度1，默认左 |
| depth_two | int | 是 | NULL | 否 | 深度2，默认右 |
| single_or_double | varchar(50) | 是 | NULL | 否 | 单双向：1 单，2 双 |
| hit_the_shelf_order | int | 是 | NULL | 否 | 上架顺序 |
| sold_out_order | int | 是 | NULL | 否 | 下架顺序 |
| direction | varchar(255) | 是 | NULL | 否 | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| hit_the_shelf_flag | tinyint(1) | 是 | NULL | 否 | 上架标识，存在上架任务为1，不存在为0，[10，20，30，40] |
| sold_out_flag | tinyint(1) | 是 | NULL | 否 | 下架标识，存在下架任务为1，不存在为0，[10，20，30] |
| free_flag | tinyint(1) | 是 | NULL | 否 | 空闲标识，空闲为1，非空闲为0 |
| qr_code | varchar(255) | 是 | NULL | 否 | 深度组二维码 |
| qr_code_status | tinyint(1) | 是 | NULL | 否 | 二维码状态：0 未生成，1 已生成 |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1 |
| flag_two | varchar(255) | 是 | NULL | 否 | 标识2 |
| flag_three | varchar(255) | 是 | NULL | 否 | 标识3 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_depth_group_copy1

- 表说明：深度组管理—中华商务备份
- 存储引擎：InnoDB
- 字段数：18

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| depth_group_code | varchar(255) | 是 | NULL | 否 | 深度组编码 |
| storage_location_id | varchar(32) | 是 | NULL | 否 | 库位ID |
| depth_one | int | 是 | NULL | 否 | 深度1，默认左 |
| depth_two | int | 是 | NULL | 否 | 深度2，默认右 |
| single_or_double | varchar(50) | 是 | NULL | 否 | 单双向：1 单，2 双 |
| hit_the_shelf_order | int | 是 | NULL | 否 | 上架顺序 |
| sold_out_order | int | 是 | NULL | 否 | 下架顺序 |
| direction | varchar(255) | 是 | NULL | 否 | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| hit_the_shelf_flag | tinyint(1) | 是 | NULL | 否 | 上架标识，存在上架任务为1，不存在为0，[10，20，30，40] |
| sold_out_flag | tinyint(1) | 是 | NULL | 否 | 下架标识，存在下架任务为1，不存在为0，[10，20，30] |
| free_flag | tinyint(1) | 是 | NULL | 否 | 空闲标识，空闲为1，非空闲为0 |
| qr_code | varchar(255) | 是 | NULL | 否 | 深度组二维码 |
| qr_code_status | tinyint(1) | 是 | NULL | 否 | 二维码状态：0 未生成，1 已生成 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_device

- 表说明：设备主表
- 存储引擎：InnoDB
- 字段数：18

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| device_code | varchar(32) | 否 | - | 否 | 设备编码 |
| device_name | varchar(32) | 是 | NULL | 否 | 设备名称 |
| device_ip | varchar(32) | 是 | NULL | 否 | IP |
| device_port | int | 是 | NULL | 否 | 端口 |
| device_type | tinyint | 是 | '1' | 否 | 设备类型 1.输送线 2.激光类型 |
| protocol_type | tinyint | 是 | '1' | 否 | 1. modbus tcp  2.tcp 3.http |
| device_status | tinyint | 是 | '1' | 否 | 0:禁用 1 ：启用 |
| connect_status | tinyint | 是 | '1' | 否 | 0:离线 1：在线 |
| connect_mode | tinyint | 是 | '1' | 否 | 连接模式 1.客户端 2.服务端 |
| connect_id | int | 是 | NULL | 否 | 网络通信中身份ID |
| time_out_heart | int | 是 | NULL | 否 | 心跳超时秒 |
| time_out_rw | int | 是 | NULL | 否 | 读写超时秒 |
| system_source | varchar(32) | 是 | NULL | 否 | 系统来源，eg：plc，master |
| create_time | datetime | 是 | NULL | 否 |  |
| create_by | varchar(32) | 是 | NULL | 否 |  |
| update_time | datetime | 是 | NULL | 否 |  |
| update_by | varchar(32) | 是 | NULL | 否 |  |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_device_code | 是 | `device_code` |


## tms_device_interface

- 表说明：设备明细表
- 存储引擎：InnoDB
- 字段数：26

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| interface_code | varchar(32) | 否 | - | 否 |  |
| interface_name | varchar(64) | 否 | - | 否 |  |
| device_code | varchar(32) | 否 | - | 否 |  |
| interface_type | int | 否 | '1' | 否 | 接口类型1：触发  2.定时 |
| business_type | int | 是 | '0' | 否 | 1:上料；2下料 |
| location_id | bigint | 是 | NULL | 否 |  |
| location_code | varchar(32) | 否 | - | 否 |  |
| y_read_address | varchar(32) | 是 | NULL | 否 | Y读地址 |
| n_read_address | varchar(32) | 是 | NULL | 否 | N读地址 |
| y_read_default | varchar(32) | 是 | NULL | 否 | Y读默认值 |
| n_read_default | varchar(32) | 是 | NULL | 否 | N读默认值 |
| read_function_code | varchar(10) | 是 | NULL | 否 | 地址读功能码 |
| y_write_address | varchar(32) | 是 | NULL | 否 | Y写地址 |
| n_write_address | varchar(32) | 是 | NULL | 否 | N写地址 |
| y_write_default | varchar(32) | 是 | NULL | 否 | Y写默认值 |
| n_write_default | varchar(32) | 是 | NULL | 否 | N写默认值 |
| write_function_code | varchar(10) | 是 | NULL | 否 | 地址写功能码 |
| interval_time | int | 是 | '1' | 否 | 频次秒 |
| test_read_value | varchar(32) | 是 | NULL | 否 | 测试读取值 |
| start_offset | int | 是 | '0' | 否 | 寄存器起始地址 |
| register_quantity | int | 是 | NULL | 否 | 寄存器数量 |
| create_time | datetime | 是 | NULL | 否 |  |
| create_by | varchar(32) | 是 | NULL | 否 |  |
| update_time | datetime | 是 | NULL | 否 |  |
| update_by | varchar(32) | 是 | '1' | 否 |  |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_device_interface_location | 否 | `location_code` |
| idx_device_interface_dcode | 否 | `device_code` |


## tms_device_interface_event

- 表说明：设备事件关联表
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| device_interface_id | varchar(36) | 是 | NULL | 否 | 设备动作id |
| event_code | varchar(36) | 是 | NULL | 否 | 编码 |
| event_name | varchar(36) | 是 | NULL | 否 | 名称 |
| event_sort | int | 是 | NULL | 否 | 排序 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(32) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_door

- 表说明：门
- 存储引擎：InnoDB
- 字段数：17

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| port | int | 是 | NULL | 否 | modbus 端口 |
| ip | varchar(32) | 是 | NULL | 否 | modbus ip |
| door_name | varchar(255) | 是 | NULL | 否 | 门名称 |
| task_type_route_id | varchar(64) | 是 | NULL | 否 | 任务类型id |
| open_status_offset | int | 是 | NULL | 否 | 开状态反馈点 |
| close_status_offset | int | 是 | NULL | 否 | 关状态反馈点 |
| open_write_offset | int | 是 | NULL | 否 | 开状态写入点 |
| close_write_offset | int | 是 | NULL | 否 | 关状态写入点 |
| tier | int | 是 | NULL | 否 | 门所在层 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建人 |
| update_by | varchar(32) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| sys_org_code | varchar(64) | 是 | NULL | 否 | 所属部门 |
| type | varchar(1) | 是 | '2' | 否 | 1电梯2卷帘门3交通灯 |
| slave_id | int | 是 | NULL | 否 |  |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_door_control_area

- 表说明：管制区与门对照表
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| control_area | varchar(32) | 是 | NULL | 否 | 管制区ID |
| door_id | varchar(32) | 是 | NULL | 否 | 门ID |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| sys_org_code | varchar(64) | 是 | NULL | 否 | 所属部门 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_event

- 表说明：事件
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| event_code | varchar(36) | 是 | NULL | 否 | 编码 |
| event_name | varchar(36) | 是 | NULL | 否 | 名称 |
| event_status | tinyint | 是 | '1' | 否 | 0:禁用 1 ：启用 |
| parameter_code | varchar(32) | 是 | NULL | 否 | 事件参数编码 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_event_parameter

- 表说明：参数主表
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| parameter_code | varchar(36) | 是 | NULL | 否 | 编码 |
| parameter_name | varchar(36) | 是 | NULL | 否 | 名称 |
| parameter_status | tinyint | 是 | '1' | 否 | 0:禁用 1 ：启用 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_event_parameter_item

- 表说明：参数明细表
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| item_code | varchar(36) | 是 | NULL | 否 | 编码 |
| item_name | varchar(36) | 是 | NULL | 否 | 名称 |
| required_flag | tinyint(1) | 是 | '1' | 否 | 0非必须1必须 |
| item_status | tinyint | 是 | '1' | 否 | 0:禁用 1 ：启用 |
| parameter_code | varchar(32) | 是 | NULL | 否 | 参数编码 |
| data_type | varchar(1) | 是 | 'S' | 否 | 数据类型，S字符串，N数字 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_event_process_record

- 表说明：事件处理记录表
- 存储引擎：InnoDB
- 字段数：17

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| strategy_action_event_id | varchar(36) | 是 | NULL | 否 | 策略事件ID |
| strategy_action_id | varchar(36) | 是 | NULL | 否 | 策略动作ID |
| demand_id | varchar(255) | 是 | NULL | 否 | 需求ID |
| device_code | varchar(32) | 是 | NULL | 否 | 设备编码 |
| device_interface_code | varchar(32) | 是 | NULL | 否 | 设备接口编码 |
| location_code | varchar(32) | 是 | NULL | 否 | 设备编码 |
| event_code | varchar(255) | 是 | NULL | 否 | 事件编码 |
| event_parameter | longtext | 是 | - | 否 | 事件参数 |
| record_status | int | 是 | '0' | 否 | 状态0失败1成功 |
| remark | longtext | 是 | - | 否 | 备注 |
| event_source | varchar(32) | 是 | NULL | 否 | 设备编码 |
| retry_num | int | 是 | '0' | 否 | 重试次数 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_flow_card

- 表说明：流程卡表
- 存储引擎：InnoDB
- 字段数：42

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 | 流程卡表ID |
| flow_card_number | varchar(255) | 是 | NULL | 否 | 流程卡编码 |
| work_order_id | varchar(50) | 是 | NULL | 否 | 工单ID |
| serial_number | int | 是 | NULL | 否 | 顺序号 |
| container_id | varchar(50) | 是 | NULL | 否 | 容器id |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1-上工序 |
| flag_two | varchar(255) | 是 | NULL | 否 | 标识2-本工序 |
| flag_three | varchar(255) | 是 | NULL | 否 | 标识3-下工序 |
| flag_four | varchar(255) | 是 | NULL | 否 | 标识4-工单编码/印号+辅号 |
| flag_five | varchar(255) | 是 | NULL | 否 | 标识5-容器标识(仁叶的值默认为WMS) |
| flag_six | varchar(255) | 是 | NULL | 否 | 标识6-部件 |
| flag_seven | varchar(255) | 是 | '' | 否 | 标识7-当前贴次 |
| flag_eight | varchar(255) | 是 | NULL | 否 | 标识8-总贴次 |
| flag_nine | varchar(255) | 是 | NULL | 否 | 标识9-是否首尾贴 |
| flag_ten | varchar(255) | 是 | NULL | 否 | 标识10-是否后续有贴衬 |
| flag_eleven | varchar(255) | 是 | NULL | 否 | 标识11-是否正贴 |
| flag_twelve | varchar(255) | 是 | NULL | 否 | 标识12-是否反贴 |
| material_name | varchar(50) | 是 | NULL | 否 | 物料名称 |
| material_code | varchar(50) | 是 | NULL | 否 | 物料编码 |
| material_number | decimal(10,3) | 是 | NULL | 否 | 物料数量 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| flow_card_business_id | varchar(255) | 是 | NULL | 否 | MES的流程卡号 |
| print_number | varchar(255) | 是 | NULL | 否 | 印号 |
| sub_print_number | varchar(255) | 是 | NULL | 否 | 辅号 |
| units_name | varchar(255) | 是 | NULL | 否 | 单位名称 |
| label_num | varchar(255) | 是 | NULL | 否 | 标签号 |
| big_type_name | varchar(255) | 是 | NULL | 否 | 大类名称 |
| deputy_type_name | varchar(255) | 是 | NULL | 否 | 副类名称 |
| deputy_type_noun | varchar(255) | 是 | NULL | 否 | 副类名词 |
| flag_thirteen | varchar(255) | 是 | NULL | 否 | 标识13-印色 |
| flag_fourteen | varchar(255) | 是 | NULL | 否 | 标识14-是否包含样品:1是 |
| flag_fifteen | varchar(255) | 是 | NULL | 否 | 标识15-是否不合格 |
| flag_sixteen | varchar(255) | 是 | NULL | 否 | 标识16-跺型高度 |
| flag_seventeen | varchar(255) | 是 | NULL | 否 | 标识17-跺型重量 |
| flag_eighteen | varchar(255) | 是 | NULL | 否 | 标识18-钉式编码 |
| flag_nineteen | varchar(255) | 是 | NULL | 否 | 标识19-大类编号 |
| flag_twenty | varchar(255) | 是 | NULL | 否 | 标识20-物料类型名称 |
| flag_twenty_one | varchar(255) | 是 | NULL | 否 | 标识21-副类编号 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_flow_card_copy1

- 表说明：流程卡表
- 存储引擎：InnoDB
- 字段数：42

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 | 流程卡表ID |
| flow_card_number | varchar(255) | 是 | NULL | 否 | 流程卡编码 |
| work_order_id | varchar(50) | 是 | NULL | 否 | 工单ID |
| serial_number | int | 是 | NULL | 否 | 顺序号 |
| container_id | varchar(50) | 是 | NULL | 否 | 容器id |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1-上工序 |
| flag_two | varchar(255) | 是 | NULL | 否 | 标识2-本工序 |
| flag_three | varchar(255) | 是 | NULL | 否 | 标识3-下工序 |
| flag_four | varchar(255) | 是 | NULL | 否 | 标识4-工单编码 |
| flag_five | varchar(255) | 是 | NULL | 否 | 标识5-容器标识(仁叶的值默认为WMS) |
| flag_six | varchar(255) | 是 | NULL | 否 | 标识6 |
| flag_seven | varchar(255) | 是 | '' | 否 | 标识7 |
| flag_eight | varchar(255) | 是 | NULL | 否 | 标识8 |
| flag_nine | varchar(255) | 是 | NULL | 否 | 标识9 |
| flag_ten | varchar(255) | 是 | NULL | 否 | 标识10 |
| flag_eleven | varchar(255) | 是 | NULL | 否 | 标识11 |
| flag_twelve | varchar(255) | 是 | NULL | 否 | 标识12 |
| material_name | varchar(50) | 是 | NULL | 否 | 物料名称 |
| material_code | varchar(50) | 是 | NULL | 否 | 物料编码 |
| material_number | decimal(10,3) | 是 | NULL | 否 | 物料数量 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| flow_card_business_id | varchar(255) | 是 | NULL | 否 | MES的流程卡号 |
| print_number | varchar(255) | 是 | NULL | 否 | 印号 |
| sub_print_number | varchar(255) | 是 | NULL | 否 | 辅号 |
| units_name | varchar(255) | 是 | NULL | 否 | 单位名称 |
| label_num | varchar(255) | 是 | NULL | 否 | 标签号 |
| big_type_name | varchar(255) | 是 | NULL | 否 | 大类名称 |
| deputy_type_name | varchar(255) | 是 | NULL | 否 | 副类名称 |
| deputy_type_noun | varchar(255) | 是 | NULL | 否 | 副类名词 |
| flag_thirteen | varchar(255) | 是 | NULL | 否 | 标识13 |
| flag_fourteen | varchar(255) | 是 | NULL | 否 | 标识14 |
| flag_fifteen | varchar(255) | 是 | NULL | 否 | 标识15 |
| flag_sixteen | varchar(255) | 是 | NULL | 否 | 标识16 |
| flag_seventeen | varchar(255) | 是 | NULL | 否 | 标识17 |
| flag_eighteen | varchar(255) | 是 | NULL | 否 | 标识18 |
| flag_nineteen | varchar(255) | 是 | NULL | 否 | 标识19 |
| flag_twenty | varchar(255) | 是 | NULL | 否 | 标识20 |
| flag_twenty_one | varchar(255) | 是 | NULL | 否 | 标识21 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_goods_type

- 表说明：货型管理
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| goods_type_code | varchar(255) | 是 | NULL | 否 | 货型编号 |
| goods_type_name | varchar(255) | 是 | NULL | 否 | 货型名称 |
| goods_length | varchar(50) | 是 | NULL | 否 | 长 |
| goods_width | varchar(50) | 是 | NULL | 否 | 宽 |
| goods_height | varchar(50) | 是 | NULL | 否 | 高 |
| status | varchar(50) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| direction | varchar(50) | 是 | NULL | 否 | 方向 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_location_container

- 表说明：库位与容器中间表
- 存储引擎：InnoDB
- 字段数：7

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| storage_location_id | varchar(32) | 是 | NULL | 否 | 库位ID |
| container_id | varchar(32) | 是 | NULL | 否 | 容器ID |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| container_id | 是 | `container_id` |


## tms_logical_area_tag

- 表说明：逻辑区标签
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 是 | NULL | 否 |  |
| tag_code | varchar(64) | 是 | NULL | 否 | 逻辑区标签编码 |
| tag_name | varchar(64) | 是 | NULL | 否 | 逻辑区标签名称 |
| status | varchar(1) | 是 | NULL | 否 | 状态：0 禁用，1 启用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(64) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(64) | 是 | NULL | 否 | 更新人 |

索引：

_SQL未声明索引。_


## tms_machine

- 表说明：机台主数据
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 机台编码 |
| name | varchar(255) | 是 | NULL | 否 | 机台名称 |
| status | tinyint | 是 | NULL | 否 | 状态(0 禁用, 1 启用) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_machine_data

- 表说明：机台实时数据
- 存储引擎：InnoDB
- 字段数：22

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 | 机台实时数据ID |
| company_id | varchar(255) | 是 | NULL | 否 | 公司ID（实时数据接口传的值） |
| work_space_id | varchar(255) | 是 | NULL | 否 | 工作中心ID（实时数据接口传的值） |
| machine_id | varchar(255) | 是 | NULL | 否 | 机台ID(（实时数据接口传的值。等于机台主数据的编码） |
| machine_status | varchar(255) | 是 | NULL | 否 | 机台状态:生产Product；预生产PreProduct |
| current_process_id | varchar(255) | 是 | NULL | 否 | 本工序ID（实时数据接口传的=工序编码，存的是该编码对应的分类名称的值） |
| current_print_number | varchar(255) | 是 | NULL | 否 | 当前印号 |
| current_sub_print_number | varchar(255) | 是 | NULL | 否 | 当前辅号 |
| current_book_part_code | varchar(255) | 是 | NULL | 否 | 当前部件ID（实时数据接口传的值） |
| current_sing_number | varchar(255) | 是 | NULL | 否 | 当前贴次 |
| current_positive_sign | varchar(255) | 是 | NULL | 否 | 当前是否正贴  Y是 N否 |
| current_negative_sign | varchar(255) | 是 | NULL | 否 | 当前是否反贴  Y是 N否 |
| total_part | varchar(255) | 是 | NULL | 否 | 总贴次 |
| current_sample | varchar(255) | 是 | NULL | 否 | 当前是否样品 Y是 N否 |
| set_collect | varchar(255) | 是 | NULL | 否 | 是否齐套 Y是 N否 |
| sample_set_collect | varchar(255) | 是 | NULL | 否 | 是否样品齐套 Y是 N否 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |
| sample_count | int | 是 | NULL | 否 | 样品托盘数（实时数据接口不传，TMS统计的数） |
| sample_prod_flag | varchar(1) | 是 | NULL | 否 | 样品生产标识 1/0 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_monitoring_source_log

- 表说明：资源监控日志
- 存储引擎：InnoDB
- 字段数：13

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| monitoring_id | varchar(36) | 是 | NULL | 否 | 资源监控日志ID |
| resource_type | varchar(10) | 是 | NULL | 否 | 资源类型：储位，容器，车辆 |
| resource_source | varchar(255) | 是 | NULL | 否 | 资源来源名称 |
| resource_id | varchar(36) | 是 | NULL | 否 | 被监控的资源ID |
| resource_code | varchar(255) | 是 | NULL | 否 | 被监控的资源编码 |
| old_data | varchar(255) | 是 | NULL | 否 | 监控前状态 |
| new_data | varchar(255) | 是 | NULL | 否 | 监控到状态 |
| discovery_time | datetime | 是 | NULL | 否 | 发现时间 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_nail

- 表说明：钉式主数据
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 钉式编码 |
| name | varchar(255) | 是 | NULL | 否 | 钉式称 |
| status | tinyint | 是 | NULL | 否 | 状态(0 禁用, 1 启用) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_operation_rule

- 表说明：操作型规则
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 操作型规则编码 |
| name | varchar(255) | 是 | NULL | 否 | 操作型规则名称 |
| conditional_combination_id | varchar(255) | 是 | NULL | 否 | 关联条件组ID |
| operation_type | varchar(255) | 是 | NULL | 否 | 操作类型：1 解绑 |
| broadcast_speech_id | varchar(255) | 是 | NULL | 否 | 广播语事件ID |
| status | varchar(32) | 是 | NULL | 否 | 状态：0 禁用，1 启用 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| sys_org_code | varchar(64) | 是 | NULL | 否 | 所属部门 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_operation_rule_event

- 表说明：操作型规则事件关联表
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| operation_rule_id | varchar(36) | 是 | NULL | 否 | 设备动作id |
| event_code | varchar(36) | 是 | NULL | 否 | 编码 |
| event_name | varchar(36) | 是 | NULL | 否 | 名称 |
| event_sort | int | 是 | NULL | 否 | 排序 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(32) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_paramter_mapping

- 表说明：监控资源记录-无用
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| mapping_key | varchar(255) | 是 | NULL | 否 | 映射key |
| type | varchar(5) | 是 | NULL | 否 | 类型：1 入参，2 映射 |
| is_update | varchar(1) | 是 | NULL | 否 | 是否更新： 1 是，2 否 |
| status | varchar(1) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| is_query | varchar(1) | 是 | NULL | 否 | 是否查询： 1 是，2 否 |
| pid_key | varchar(255) | 是 | NULL | 否 | 关联key |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

_SQL未声明索引。_


## tms_pda_log

- 表说明：PDA操作日志
- 存储引擎：InnoDB
- 字段数：14

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| operation_module | varchar(255) | 是 | NULL | 否 | 操作模块 |
| pda_log_id | varchar(36) | 是 | NULL | 否 | pda日志ID |
| request_url | varchar(255) | 是 | NULL | 否 | 请求地址 |
| request_params | longtext | 是 | - | 否 | 请求参数 |
| returned_value | longtext | 是 | - | 否 | 接口返回值 |
| user_id | varchar(255) | 是 | NULL | 否 | 操作用户账号 |
| user_name | varchar(255) | 是 | NULL | 否 | 操作用户名 |
| ip | varchar(255) | 是 | NULL | 否 | ip |
| remark | longtext | 是 | - | 否 | 备注 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_permission

- 表说明：PDA菜单表
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 | 主键id |
| name | varchar(255) | 是 | NULL | 否 | 菜单标题 |
| status | varchar(255) | 是 | NULL | 否 | 状态 1启用/禁用0 |
| sort | int | 是 | '0' | 否 | 菜单排序 |
| component_name | varchar(255) | 是 | NULL | 否 | 前端组件名，对应菜单的vue组件 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | date | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | date | 是 | NULL | 否 | 更新日期 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_role

- 表说明：PDA用户角色表
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| role_name | varchar(255) | 是 | NULL | 否 | 角色名 |
| role_code | varchar(255) | 是 | NULL | 否 | 角色编码 |
| description | varchar(255) | 是 | NULL | 否 | 描述 |
| status | varchar(255) | 是 | NULL | 否 | 启用/禁用 |
| tms_task_data_permission | varchar(255) | 是 | NULL | 否 | 任务数据权限 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 |  |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 |  |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_role_permission

- 表说明：角色权限表
- 存储引擎：InnoDB
- 字段数：5

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| role_id | varchar(255) | 是 | NULL | 否 | 角色Id |
| permission_id | varchar(255) | 是 | NULL | 否 | 菜单ID |
| operate_date | datetime | 是 | NULL | 否 | 操作时间 |
| operate_ip | varchar(100) | 是 | NULL | 否 | 操作ip |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_user

- 表说明：PDA用户表
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| user_name | varchar(255) | 是 | NULL | 否 | 登录账号 |
| real_name | varchar(255) | 是 | NULL | 否 | 真实姓名 |
| pass_word | varchar(255) | 是 | NULL | 否 | 密码 |
| salt | varchar(255) | 是 | NULL | 否 | md5密码盐 |
| status | varchar(255) | 是 | NULL | 否 | 状态(1：正常  2：冻结 ） |
| del_flag | varchar(255) | 是 | NULL | 否 | 删除状态（0，正常，1已删除） |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_user_cache

- 表说明：PDA用户信息
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| user_id | varchar(32) | 是 | NULL | 否 | 用户ID |
| user_name | varchar(255) | 是 | NULL | 否 | 用户名称 |
| this_process_id | varchar(255) | 是 | NULL | 否 | 本工序ID |
| this_process_name | varchar(255) | 是 | NULL | 否 | 本工序名称 |
| loading_area_id | varchar(255) | 是 | NULL | 否 | 上料区ID |
| blanking_area_id | varchar(255) | 是 | NULL | 否 | 下料区ID |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |
| work_shop_id | varchar(255) | 是 | NULL | 否 | 车间ID |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_pda_user_role

- 表说明：用户角色关联表
- 存储引擎：InnoDB
- 字段数：3

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| user_id | varchar(255) | 是 | NULL | 否 | 用户id |
| role_id | varchar(255) | 是 | NULL | 否 | 角色Id |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_process

- 表说明：工序表
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| process_code | varchar(50) | 是 | NULL | 否 | 工序编码 |
| process_name | varchar(50) | 是 | NULL | 否 | 工序名称 |
| process_type | varchar(50) | 是 | NULL | 否 | 工序分类名称 |
| production_unit | varchar(50) | 是 | NULL | 否 | 投产单位(米) |
| output_unit | varchar(50) | 是 | NULL | 否 | 产出单位(米) |
| status | varchar(50) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_process_copy1

- 表说明：工序表
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| process_code | varchar(50) | 是 | NULL | 否 | 工序编码 |
| process_name | varchar(50) | 是 | NULL | 否 | 工序名称 |
| process_type | varchar(50) | 是 | NULL | 否 | 工序分类名称 |
| production_unit | varchar(50) | 是 | NULL | 否 | 投产单位(米) |
| output_unit | varchar(50) | 是 | NULL | 否 | 产出单位(米) |
| status | varchar(50) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| process_code | 是 | `process_code` |


## tms_process_route

- 表说明：工艺路线
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| process_route_name | varchar(50) | 是 | NULL | 否 | 工艺路线名称 |
| process_route_code | varchar(50) | 是 | NULL | 否 | 工艺路线编码 |
| status | int | 是 | NULL | 否 | 状态：1启用， 2禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_process_route_process

- 表说明：工序 工艺路线 中间表\r\n
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 是 | NULL | 否 |  |
| process_route_id | varchar(32) | 是 | NULL | 否 | 工艺路线id |
| process_id | varchar(32) | 是 | NULL | 否 | 工序id |
| sort | int | 是 | NULL | 否 | 排序：10 20 30 40... |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

_SQL未声明索引。_


## tms_query_demand_log

- 表说明：查询需求池日志
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| query_demand_id | varchar(36) | 是 | NULL | 否 | 查询需求池日志ID |
| monitoring_log_id | varchar(36) | 是 | NULL | 否 | 监控资源日志ID |
| start_time | datetime | 是 | NULL | 否 | 开始查询时间 |
| end_time | datetime | 是 | NULL | 否 | 结束查询时间 |
| demand_id | longtext | 否 | - | 否 | 被查询需求池的需求ID |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_router

- 表说明：路由管理
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| router_code | varchar(255) | 是 | NULL | 否 | 路由编号 |
| start_storage_location_id | varchar(36) | 是 | NULL | 否 | 起点库位id |
| end_storage_location_id | varchar(36) | 是 | NULL | 否 | 终点库位id |
| router_weight | int | 是 | NULL | 否 | 路由权数 |
| task_type_route_id | varchar(255) | 是 | NULL | 否 | 任务类型名称ID |
| sort | int | 是 | NULL | 否 | 排序：用于权重相同时选择路由 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| router_code | 是 | `router_code` |
| idx_start_end | 否 | `start_storage_location_id`,`end_storage_location_id` |


## tms_rule

- 表说明：规则管理
- 存储引擎：InnoDB
- 字段数：24

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| rule_code | varchar(50) | 是 | NULL | 否 | 规则编码 |
| rule_name | varchar(50) | 是 | NULL | 否 | 规则名称 |
| conditional_combination_id | varchar(50) | 是 | NULL | 否 | 关联条件组id |
| pattern | varchar(10) | 是 | NULL | 否 | 模式：1 上料，2 下料 |
| logic_area_id | varchar(255) | 是 | NULL | 否 | 逻辑区id |
| logic_location_status | varchar(10) | 是 | NULL | 否 | 目标储位状态 |
| vehicle_group_id | varchar(255) | 是 | NULL | 否 | 车辆分组id |
| container_status | varchar(32) | 是 | NULL | 否 | 容器状态 |
| container_initialize | varchar(50) | 是 | NULL | 否 | 容器初始化 |
| is_release_container | varchar(50) | 是 | NULL | 否 | 是否释放容器：1 是，2 否 |
| algorithm_package_top | varchar(50) | 是 | NULL | 否 | 算法包(上架规则)：1 先进先出  2先进后出 |
| algorithm_package_bottom | varchar(50) | 是 | NULL | 否 | 算法包(下架规则)：1 先进先出  2先进后出 |
| action_ids | varchar(255) | 是 | NULL | 否 | 策略动作id(id,id,id) |
| customized_results | varchar(255) | 是 | NULL | 否 | 定制化结果id(id,id,id) |
| is_timeout | int | 是 | NULL | 否 | 是否开启超时 1 是，2 否 |
| flow_card_flag | varchar(255) | 是 | NULL | 否 | 流程卡标识新增（id,id,id |
| priority | int | 是 | NULL | 否 | 优先级 |
| good_type | varchar(10) | 是 | NULL | 否 | 下发RCS时携带的货型编码(优先取自规则, 其次需求, 默认1) |
| status | varchar(10) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_rule_dict

- 表说明：上下架规则设置
- 存储引擎：InnoDB
- 字段数：14

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| type | varchar(10) | 是 | NULL | 否 | 类型：1 上架，2 下架 |
| name | varchar(255) | 是 | NULL | 否 | 规则名称 |
| is_show | varchar(10) | 是 | NULL | 否 | 显示：1 显示，2 不显示 |
| old_value | varchar(10) | 是 | NULL | 否 | 对应的，1，2，3 |
| remark | varchar(255) | 是 | NULL | 否 | 描述 |
| rule_config | longtext | 是 | - | 否 | 标识配置 |
| status | tinyint | 是 | NULL | 否 | 状态：0 禁用，1 启用 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| code | varchar(255) | 是 | NULL | 否 | 规则编码 |
| is_old_rule | tinyint | 是 | NULL | 否 | 是否是老规则 1 是 2否 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_send_http_log

- 表说明：调用第三方接口日志记录表
- 存储引擎：InnoDB
- 字段数：10

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| task_id | varchar(255) | 是 | NULL | 否 | 任务id |
| request_url | varchar(255) | 是 | NULL | 否 | 请求地址 |
| request_params | longtext | 是 | - | 否 | 请求参数 |
| returned_value | longtext | 是 | - | 否 | 接口返回值 |
| remark | longtext | 是 | - | 否 | 备注 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_source_change_record

- 表说明：资源变更记录表
- 存储引擎：InnoDB
- 字段数：13

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| source_id | varchar(255) | 是 | NULL | 否 | 库位ID |
| source_code | varchar(255) | 是 | NULL | 否 | 资源编码 |
| occurrence_time | datetime | 是 | NULL | 否 | 发生时间 |
| new_data | varchar(255) | 是 | NULL | 否 | 新数据 |
| type | varchar(255) | 是 | NULL | 否 | 类型：1 库位，2 容器 |
| old_data | varchar(255) | 是 | NULL | 否 | 老数据 |
| update_source | varchar(255) | 是 | NULL | 否 | 修改来源接口路径 |
| remark | varchar(255) | 是 | NULL | 否 | 描述信息 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varbinary(255) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_storage_cavern

- 表说明：储区管理
- 存储引擎：InnoDB
- 字段数：14

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| warehouse_id | varchar(36) | 是 | NULL | 否 | 仓库id |
| business_id | varchar(255) | 是 | NULL | 否 | 库区业务ID |
| storage_cavern_code | varchar(255) | 是 | NULL | 否 | 库区编码 |
| storage_cavern_name | varchar(255) | 是 | NULL | 否 | 库区名称 |
| storage_cavern_type | varchar(32) | 是 | NULL | 否 | 库区类型：0 立库，1 平库，2 货架库，3 暂存库，4 输送线 5容器 |
| single_or_double | varchar(255) | 是 | NULL | 否 | 深度组方向：1 单向，2 双向 |
| direction | varchar(255) | 是 | NULL | 否 | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| workshop | varchar(50) | 是 | NULL | 否 | 车间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_storage_cavern_type

- 表说明：储区分类
- 存储引擎：InnoDB
- 字段数：14

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| type_code | varchar(255) | 是 | NULL | 否 | 库区类型编码 |
| type_name | varchar(255) | 是 | NULL | 否 | 库区类型名称 |
| type | varchar(255) | 是 | NULL | 否 | 类型：1 设备，2 人工 |
| equipment_port | varchar(255) | 是 | NULL | 否 | 设备端口 |
| equipment_domain | varchar(255) | 是 | NULL | 否 | 设备域名 |
| equipment_ip | varchar(255) | 是 | NULL | 否 | 设备IP |
| status | varchar(255) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| remakr | text | 是 | - | 否 | 备注 |
| storage_location_their | int | 是 | NULL | 否 | 储位所属 1储区，2容器 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_storage_history

- 表说明：PAD常用储位记录
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| user_id | varchar(32) | 是 | NULL | 否 | 用户ID |
| storage_location_id | varchar(32) | 是 | NULL | 否 | 库位ID |
| type | varchar(255) | 是 | NULL | 否 | 1 起点选择，2 终点选择 |
| is_del | varchar(10) | 是 | NULL | 否 | 是否删除, 1 是, 2 否 |
| goods_type_id | varchar(255) | 是 | NULL | 否 | 货型id |
| source | varchar(10) | 是 | NULL | 否 | 来源: 1 点对点, 2 释放库位, 3 绑定库位, 4 点对区 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建日期 |
| update_by | varchar(50) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新日期 |
| sys_org_code | varchar(64) | 是 | NULL | 否 | 所属部门 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_storage_location

- 表说明：储位管理
- 存储引擎：InnoDB
- 字段数：56

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| business_id | varchar(255) | 是 | NULL | 否 | 业务ID，用于和其他系统对接储位信息 |
| warehouse_id | varchar(36) | 是 | NULL | 否 | 仓库id |
| storage_cavern_id | varchar(36) | 是 | NULL | 否 | 库区id |
| storage_location_code | varchar(255) | 是 | NULL | 否 | 库位编码 |
| storage_location_name | varchar(255) | 是 | NULL | 否 | 库位名称 |
| storage_location_type | varchar(32) | 是 | NULL | 否 | 库位类型：0 立库，1 平库，2 货架库，3 暂存库，4 输送线  5容器 |
| container_id | varchar(36) | 是 | NULL | 否 | 容器id |
| delivery_time | datetime | 是 | NULL | 否 | 放货时间 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| storage_location_status | varchar(32) | 是 | NULL | 否 | 库位状态：0 占用，1 空闲，2 预占，3 超时，4 冻结 |
| storage_location_qr_code | varchar(255) | 是 | NULL | 否 | 库位码 |
| is_generate_qr_code | varchar(32) | 是 | NULL | 否 | 是否生成库位码：1 不生成，2 生成 |
| row_number | int | 是 | NULL | 否 | 行 |
| column_number | int | 是 | NULL | 否 | 列 |
| flag | varchar(255) | 是 | NULL | 否 | 标识1 |
| bay | varchar(32) | 是 | NULL | 否 | bay |
| storage_location_their | varchar(255) | 是 | NULL | 否 | 储位所属 1储区，2容器 |
| channel | varchar(255) | 是 | NULL | 否 | 通道 |
| tier | varchar(255) | 是 | NULL | 否 | 层 |
| lattice | varchar(255) | 是 | NULL | 否 | 格 |
| depth | varchar(255) | 是 | NULL | 否 | 深度 |
| cover | varchar(255) | 是 | NULL | 否 | 面 |
| is_scan_or_check | varchar(32) | 是 | NULL | 否 | 是否扫描校验：1 是，2 否 |
| is_retain_container | varchar(32) | 是 | NULL | 否 | 是否保留容器：1 是，2 否 |
| restriction_rule | varchar(255) | 是 | NULL | 否 | 限制规则 1许进许出 2许出不许进  3不许出许进  4不许出不许进\n |
| is_freeze | varchar(32) | 是 | NULL | 否 | 是否冻结：1 冻结，2 没冻结 |
| mixed_quantity | int | 是 | NULL | 否 | 混放数量 |
| mixed_batch_quantity | int | 是 | NULL | 否 | 混放批次数量 |
| coordinate_x | varchar(32) | 是 | NULL | 否 | 坐标X |
| coordinate_y | varchar(32) | 是 | NULL | 否 | 坐标y |
| coordinate_z | varchar(32) | 是 | NULL | 否 | 坐标z |
| length | varchar(32) | 是 | NULL | 否 | 长 |
| width | varchar(32) | 是 | NULL | 否 | 宽 |
| deep | varchar(32) | 是 | NULL | 否 | 深 |
| maximum_load_bearing | varchar(32) | 是 | NULL | 否 | 最大承重 |
| maximum_cubage | varchar(32) | 是 | NULL | 否 | 最大容积 |
| maximum_tray_quantity | int | 是 | NULL | 否 | 最大托盘数量 |
| maximum_box_quantity | int | 是 | NULL | 否 | 最大箱数量 |
| container_quantity | int | 是 | NULL | 否 | 容器数量 |
| residue_tray_quantity | int | 是 | NULL | 否 | 剩余托盘数量 |
| residue_box_quantity | int | 是 | NULL | 否 | 剩余箱数量 |
| volume_vacancy_rate | varchar(32) | 是 | NULL | 否 | 体积空置率 |
| weight_vacancy_rate | varchar(32) | 是 | NULL | 否 | 重量空置率 |
| associative_container_bind_time | datetime | 是 | NULL | 否 | 关联容器的最新绑定时间 |
| associative_container_unbind_time | datetime | 是 | NULL | 否 | 关联容器的最新解绑时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| flag2 | varchar(255) | 是 | NULL | 否 | 标识2 |
| camera_code | varchar(255) | 是 | NULL | 否 | 摄像头编码 |
| machine_id | varchar(255) | 是 | NULL | 否 | 机台id |
| empty_loc | tinyint | 是 | NULL | 否 | 是否为空托储位(2否, 1是) |
| virtual_loc | tinyint | 是 | NULL | 否 | 是否为虚拟储位(2否, 1是) |
| detection_point | varchar(255) | 是 | NULL | 否 | 探测点 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_id | 否 | `id` |
| idx_storage_cavern_id | 否 | `storage_cavern_id` |
| idx_storage_location_code | 否 | `storage_location_code` |


## tms_storage_location_copy1

- 表说明：储位管理
- 存储引擎：InnoDB
- 字段数：51

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| business_id | varchar(255) | 是 | NULL | 否 | 业务ID，用于和其他系统对接储位信息 |
| warehouse_id | varchar(36) | 是 | NULL | 否 | 仓库id |
| storage_cavern_id | varchar(36) | 是 | NULL | 否 | 库区id |
| storage_location_code | varchar(255) | 是 | NULL | 否 | 库位编码 |
| storage_location_name | varchar(255) | 是 | NULL | 否 | 库位名称 |
| storage_location_type | varchar(32) | 是 | NULL | 否 | 库位类型：0 立库，1 平库，2 货架库，3 暂存库，4 输送线  5容器 |
| container_id | varchar(36) | 是 | NULL | 否 | 容器id |
| delivery_time | datetime | 是 | NULL | 否 | 放货时间 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| storage_location_status | varchar(32) | 是 | NULL | 否 | 库位状态：0 占用，1 空闲，2 预占，3 超时 |
| storage_location_qr_code | varchar(255) | 是 | NULL | 否 | 库位码 |
| is_generate_qr_code | varchar(32) | 是 | NULL | 否 | 是否生成库位码：1 不生成，2 生成 |
| row_number | int | 是 | NULL | 否 | 行 |
| column_number | int | 是 | NULL | 否 | 列 |
| flag | varchar(255) | 是 | NULL | 否 | 标识 |
| bay | varchar(32) | 是 | NULL | 否 | bay |
| storage_location_their | varchar(255) | 是 | NULL | 否 | 储位所属 1储区，2容器 |
| channel | varchar(255) | 是 | NULL | 否 | 通道 |
| tier | varchar(255) | 是 | NULL | 否 | 层 |
| lattice | varchar(255) | 是 | NULL | 否 | 格 |
| depth | varchar(255) | 是 | NULL | 否 | 深度 |
| cover | varchar(255) | 是 | NULL | 否 | 面 |
| is_scan_or_check | varchar(32) | 是 | NULL | 否 | 是否扫描校验：1 是，2 否 |
| is_retain_container | varchar(32) | 是 | NULL | 否 | 是否保留容器：1 是，2 否 |
| restriction_rule | varchar(255) | 是 | NULL | 否 | 限制规则 1许进许出 2许出不许进  3不许出许进  4不许出不许进\n |
| is_freeze | varchar(32) | 是 | NULL | 否 | 是否冻结：1 冻结，2 没冻结 |
| mixed_quantity | int | 是 | NULL | 否 | 混放数量 |
| mixed_batch_quantity | int | 是 | NULL | 否 | 混放批次数量 |
| coordinate_x | varchar(32) | 是 | NULL | 否 | 坐标X |
| coordinate_y | varchar(32) | 是 | NULL | 否 | 坐标y |
| coordinate_z | varchar(32) | 是 | NULL | 否 | 坐标z |
| length | varchar(32) | 是 | NULL | 否 | 长 |
| width | varchar(32) | 是 | NULL | 否 | 宽 |
| deep | varchar(32) | 是 | NULL | 否 | 深 |
| maximum_load_bearing | varchar(32) | 是 | NULL | 否 | 最大承重 |
| maximum_cubage | varchar(32) | 是 | NULL | 否 | 最大容积 |
| maximum_tray_quantity | int | 是 | NULL | 否 | 最大托盘数量 |
| maximum_box_quantity | int | 是 | NULL | 否 | 最大箱数量 |
| container_quantity | int | 是 | NULL | 否 | 容器数量 |
| residue_tray_quantity | int | 是 | NULL | 否 | 剩余托盘数量 |
| residue_box_quantity | int | 是 | NULL | 否 | 剩余箱数量 |
| volume_vacancy_rate | varchar(32) | 是 | NULL | 否 | 体积空置率 |
| weight_vacancy_rate | varchar(32) | 是 | NULL | 否 | 重量空置率 |
| associative_container_bind_time | datetime | 是 | NULL | 否 | 关联容器的最新绑定时间 |
| associative_container_unbind_time | datetime | 是 | NULL | 否 | 关联容器的最新解绑时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| flag2 | varchar(255) | 是 | NULL | 否 | 标识2 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| storage_location_code | 是 | `storage_location_code` |


## tms_storage_location_copy2

- 表说明：储位管理
- 存储引擎：InnoDB
- 字段数：52

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| business_id | varchar(255) | 是 | NULL | 否 | 业务ID，用于和其他系统对接储位信息 |
| warehouse_id | varchar(36) | 是 | NULL | 否 | 仓库id |
| storage_cavern_id | varchar(36) | 是 | NULL | 否 | 库区id |
| storage_location_code | varchar(255) | 是 | NULL | 否 | 库位编码 |
| storage_location_name | varchar(255) | 是 | NULL | 否 | 库位名称 |
| storage_location_type | varchar(32) | 是 | NULL | 否 | 库位类型：0 立库，1 平库，2 货架库，3 暂存库，4 输送线  5容器 |
| container_id | varchar(36) | 是 | NULL | 否 | 容器id |
| delivery_time | datetime | 是 | NULL | 否 | 放货时间 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| storage_location_status | varchar(32) | 是 | NULL | 否 | 库位状态：0 占用，1 空闲，2 预占，3 超时 |
| storage_location_qr_code | varchar(255) | 是 | NULL | 否 | 库位码 |
| is_generate_qr_code | varchar(32) | 是 | NULL | 否 | 是否生成库位码：1 不生成，2 生成 |
| row_number | int | 是 | NULL | 否 | 行 |
| column_number | int | 是 | NULL | 否 | 列 |
| flag | varchar(255) | 是 | NULL | 否 | 标识 |
| bay | varchar(32) | 是 | NULL | 否 | bay |
| storage_location_their | varchar(255) | 是 | NULL | 否 | 储位所属 1储区，2容器 |
| channel | varchar(255) | 是 | NULL | 否 | 通道 |
| tier | varchar(255) | 是 | NULL | 否 | 层 |
| lattice | varchar(255) | 是 | NULL | 否 | 格 |
| depth | varchar(255) | 是 | NULL | 否 | 深度 |
| cover | varchar(255) | 是 | NULL | 否 | 面 |
| is_scan_or_check | varchar(32) | 是 | NULL | 否 | 是否扫描校验：1 是，2 否 |
| is_retain_container | varchar(32) | 是 | NULL | 否 | 是否保留容器：1 是，2 否 |
| restriction_rule | varchar(255) | 是 | NULL | 否 | 限制规则 1许进许出 2许出不许进  3不许出许进  4不许出不许进\n |
| is_freeze | varchar(32) | 是 | NULL | 否 | 是否冻结：1 冻结，2 没冻结 |
| mixed_quantity | int | 是 | NULL | 否 | 混放数量 |
| mixed_batch_quantity | int | 是 | NULL | 否 | 混放批次数量 |
| coordinate_x | varchar(32) | 是 | NULL | 否 | 坐标X |
| coordinate_y | varchar(32) | 是 | NULL | 否 | 坐标y |
| coordinate_z | varchar(32) | 是 | NULL | 否 | 坐标z |
| length | varchar(32) | 是 | NULL | 否 | 长 |
| width | varchar(32) | 是 | NULL | 否 | 宽 |
| deep | varchar(32) | 是 | NULL | 否 | 深 |
| maximum_load_bearing | varchar(32) | 是 | NULL | 否 | 最大承重 |
| maximum_cubage | varchar(32) | 是 | NULL | 否 | 最大容积 |
| maximum_tray_quantity | int | 是 | NULL | 否 | 最大托盘数量 |
| maximum_box_quantity | int | 是 | NULL | 否 | 最大箱数量 |
| container_quantity | int | 是 | NULL | 否 | 容器数量 |
| residue_tray_quantity | int | 是 | NULL | 否 | 剩余托盘数量 |
| residue_box_quantity | int | 是 | NULL | 否 | 剩余箱数量 |
| volume_vacancy_rate | varchar(32) | 是 | NULL | 否 | 体积空置率 |
| weight_vacancy_rate | varchar(32) | 是 | NULL | 否 | 重量空置率 |
| associative_container_bind_time | datetime | 是 | NULL | 否 | 关联容器的最新绑定时间 |
| associative_container_unbind_time | datetime | 是 | NULL | 否 | 关联容器的最新解绑时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| flag2 | varchar(255) | 是 | NULL | 否 | 标识2 |
| camera_code | varchar(255) | 是 | NULL | 否 | 摄像头编码 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_id | 否 | `id` |
| idx_storage_cavern_id | 否 | `storage_cavern_id` |
| idx_storage_location_code | 否 | `storage_location_code` |


## tms_storage_location_copy3

- 表说明：储位管理—中华商务备份
- 存储引擎：InnoDB
- 字段数：56

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| business_id | varchar(255) | 是 | NULL | 否 | 业务ID，用于和其他系统对接储位信息 |
| warehouse_id | varchar(36) | 是 | NULL | 否 | 仓库id |
| storage_cavern_id | varchar(36) | 是 | NULL | 否 | 库区id |
| storage_location_code | varchar(255) | 是 | NULL | 否 | 库位编码 |
| storage_location_name | varchar(255) | 是 | NULL | 否 | 库位名称 |
| storage_location_type | varchar(32) | 是 | NULL | 否 | 库位类型：0 立库，1 平库，2 货架库，3 暂存库，4 输送线  5容器 |
| container_id | varchar(36) | 是 | NULL | 否 | 容器id |
| delivery_time | datetime | 是 | NULL | 否 | 放货时间 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| storage_location_status | varchar(32) | 是 | NULL | 否 | 库位状态：0 占用，1 空闲，2 预占，3 超时，4 冻结 |
| storage_location_qr_code | varchar(255) | 是 | NULL | 否 | 库位码 |
| is_generate_qr_code | varchar(32) | 是 | NULL | 否 | 是否生成库位码：1 不生成，2 生成 |
| row_number | int | 是 | NULL | 否 | 行 |
| column_number | int | 是 | NULL | 否 | 列 |
| flag | varchar(255) | 是 | NULL | 否 | 标识 |
| bay | varchar(32) | 是 | NULL | 否 | bay |
| storage_location_their | varchar(255) | 是 | NULL | 否 | 储位所属 1储区，2容器 |
| channel | varchar(255) | 是 | NULL | 否 | 通道 |
| tier | varchar(255) | 是 | NULL | 否 | 层 |
| lattice | varchar(255) | 是 | NULL | 否 | 格 |
| depth | varchar(255) | 是 | NULL | 否 | 深度 |
| cover | varchar(255) | 是 | NULL | 否 | 面 |
| is_scan_or_check | varchar(32) | 是 | NULL | 否 | 是否扫描校验：1 是，2 否 |
| is_retain_container | varchar(32) | 是 | NULL | 否 | 是否保留容器：1 是，2 否 |
| restriction_rule | varchar(255) | 是 | NULL | 否 | 限制规则 1许进许出 2许出不许进  3不许出许进  4不许出不许进\n |
| is_freeze | varchar(32) | 是 | NULL | 否 | 是否冻结：1 冻结，2 没冻结 |
| mixed_quantity | int | 是 | NULL | 否 | 混放数量 |
| mixed_batch_quantity | int | 是 | NULL | 否 | 混放批次数量 |
| coordinate_x | varchar(32) | 是 | NULL | 否 | 坐标X |
| coordinate_y | varchar(32) | 是 | NULL | 否 | 坐标y |
| coordinate_z | varchar(32) | 是 | NULL | 否 | 坐标z |
| length | varchar(32) | 是 | NULL | 否 | 长 |
| width | varchar(32) | 是 | NULL | 否 | 宽 |
| deep | varchar(32) | 是 | NULL | 否 | 深 |
| maximum_load_bearing | varchar(32) | 是 | NULL | 否 | 最大承重 |
| maximum_cubage | varchar(32) | 是 | NULL | 否 | 最大容积 |
| maximum_tray_quantity | int | 是 | NULL | 否 | 最大托盘数量 |
| maximum_box_quantity | int | 是 | NULL | 否 | 最大箱数量 |
| container_quantity | int | 是 | NULL | 否 | 容器数量 |
| residue_tray_quantity | int | 是 | NULL | 否 | 剩余托盘数量 |
| residue_box_quantity | int | 是 | NULL | 否 | 剩余箱数量 |
| volume_vacancy_rate | varchar(32) | 是 | NULL | 否 | 体积空置率 |
| weight_vacancy_rate | varchar(32) | 是 | NULL | 否 | 重量空置率 |
| associative_container_bind_time | datetime | 是 | NULL | 否 | 关联容器的最新绑定时间 |
| associative_container_unbind_time | datetime | 是 | NULL | 否 | 关联容器的最新解绑时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| flag2 | varchar(255) | 是 | NULL | 否 | 标识2 |
| camera_code | varchar(255) | 是 | NULL | 否 | 摄像头编码 |
| machine_id | varchar(255) | 是 | NULL | 否 | 机台id |
| empty_loc | tinyint | 是 | NULL | 否 | 是否为空托储位(2否, 1是) |
| virtual_loc | tinyint | 是 | NULL | 否 | 是否为虚拟储位(2否, 1是) |
| detection_point | varchar(255) | 是 | NULL | 否 | 探测点 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_id | 否 | `id` |
| idx_storage_cavern_id | 否 | `storage_cavern_id` |
| idx_storage_location_code | 否 | `storage_location_code` |


## tms_strategy

- 表说明：策略主表
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| strategy_code | varchar(255) | 是 | NULL | 否 | 策略编码 |
| strategy_name | varchar(255) | 是 | NULL | 否 | 策略名称 |
| flag_one | varchar(255) | 是 | NULL | 否 | 标识1 |
| flage_two | varchar(255) | 是 | NULL | 否 | 标识2 |
| create_container | varchar(50) | 是 | NULL | 否 | 是否创建容器：1 创建，2 不创建 |
| container_init_status | varchar(50) | 是 | NULL | 否 | 容器初始状态：0 空，1 满，2 满+1 |
| status | varchar(255) | 是 | NULL | 否 | 状态 1启用 2禁用 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_strategy_action

- 表说明：策略行为表
- 存储引擎：InnoDB
- 字段数：13

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| strategy_id | varchar(255) | 是 | NULL | 否 | 策略ID |
| task_status | varchar(25) | 是 | NULL | 否 | 任务状态：10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| broadcast_speech_id | varchar(255) | 是 | NULL | 否 | 事件ID |
| router_weight | int | 是 | NULL | 否 | 路由权重 |
| start_storage_location_status | varchar(50) | 是 | NULL | 否 | 起点库位状态：0 占用，1 空闲，2 锁定 |
| end_storage_location_status | varchar(50) | 是 | NULL | 否 | 终点库位状态：0 占用，1 空闲，2 锁定 |
| business_status | varchar(50) | 是 | NULL | 否 | 容器业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| container_status | varchar(50) | 是 | NULL | 否 | 容器状态：0 空，1 满，2 满+1 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_strategy_action_event

- 表说明：策略事件
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| strategy_action_id | varchar(36) | 是 | NULL | 否 | 策略ID |
| event_code | varchar(64) | 是 | NULL | 否 | 编码 |
| event_name | varchar(64) | 是 | NULL | 否 | 名称 |
| event_sort | int | 是 | NULL | 否 | 排序 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(32) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_strategy_action_event_parameter_item

- 表说明：策略事件参数明细
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| strategy_action_event_id | varchar(36) | 是 | NULL | 否 | 策略事件ID |
| event_code | varchar(36) | 是 | NULL | 否 | 编码 |
| parameter_code | varchar(36) | 是 | NULL | 否 | 名称 |
| parameter_item_code | varchar(36) | 是 | NULL | 否 | 名称 |
| value_type | varchar(36) | 是 | NULL | 否 | 值类型,C常量,E 表达式 |
| parameter_item_value | varchar(36) | 是 | NULL | 否 | 名称 |
| required_flag | tinyint(1) | 是 | '0' | 否 | 0 非必填，1必填 |
| create_by | varchar(32) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(32) | 是 | NULL | 否 | 更新人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_task

- 表说明：TMS车辆任务
- 存储引擎：InnoDB
- 字段数：23

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| task_code | varchar(255) | 是 | NULL | 否 | 任务编号 |
| pid_code | varchar(255) | 是 | NULL | 否 | 任务父编号 |
| task_type | varchar(255) | 是 | NULL | 否 | 1下料，2上料，3非上料和下料 |
| task_source | varchar(255) | 是 | NULL | 否 | 任务来源 1 海康 2 未来 |
| task_priority | varchar(255) | 是 | NULL | 否 | 任务优先级 |
| issue_time | datetime | 是 | NULL | 否 | 任务下发时间 |
| task_over_time | datetime | 是 | NULL | 否 | 任务完成时间 |
| start_location_id | varchar(255) | 是 | NULL | 否 | 起始点位id |
| end_location_id | varchar(255) | 是 | NULL | 否 | 目标点位id |
| container_id | varchar(255) | 是 | NULL | 否 | 容器id |
| task_type_id | varchar(255) | 是 | NULL | 否 | 任务类型管理id |
| status | varchar(255) | 是 | NULL | 否 | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| vehicle_code | varchar(255) | 是 | NULL | 否 | 执行车辆编号 |
| task_poll_id | varchar(50) | 是 | NULL | 否 | 任务池id |
| business_config_id | varchar(36) | 是 | NULL | 否 | 业务配置ID |
| conditional_combination_id | varchar(32) | 是 | NULL | 否 | 条件组ID |
| rule_id | varchar(32) | 是 | NULL | 否 | 规则ID |
| is_exception | int | 是 | NULL | 否 | 是否异常，1是，2否 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_task_code | 否 | `task_code` |


## tms_task_abnormal

- 表说明：RCS异常任务记录
- 存储引擎：InnoDB
- 字段数：16

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(32) | 否 | - | 否 |  |
| code | varchar(100) | 是 | NULL | 否 | 异常记录编码 |
| task_code | varchar(100) | 是 | NULL | 否 | 任务编码 |
| business_config_id | varchar(100) | 是 | NULL | 否 | 业务配置ID |
| container_id | varchar(100) | 是 | NULL | 否 | 容器ID |
| start_storage_location_id | varchar(100) | 是 | NULL | 否 | 起始储位ID |
| end_storage_location_id | varchar(100) | 是 | NULL | 否 | 终点储位编码 |
| begin_time | datetime | 是 | NULL | 否 | 告警开始时间 |
| warn_content | text | 是 | - | 否 | 告警内容 |
| abnormal_type | varchar(10) | 是 | NULL | 否 | 异常类型 |
| object | varchar(100) | 是 | NULL | 否 | 报警对象 |
| equipment_coding | varchar(100) | 是 | NULL | 否 | 设备编码：呼叫器为IP+区域，车辆为车辆编号 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(100) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(100) | 是 | NULL | 否 | 修改人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_task_poll

- 表说明：容器任务池+任务组
- 存储引擎：InnoDB
- 字段数：26

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| task_code | varchar(255) | 是 | NULL | 否 | 任务编号 |
| pid_code | varchar(255) | 是 | NULL | 否 | 任务父编号 |
| task_type | varchar(255) | 是 | NULL | 否 | 1下料，2上料，3非上料和下料 |
| task_source | varchar(255) | 是 | NULL | 否 | 任务来源：1海康，2未来 |
| task_priority | varchar(255) | 是 | NULL | 否 | 优先级 |
| issue_time | datetime | 是 | NULL | 否 | 任务下发时间 |
| task_over_time | datetime | 是 | NULL | 否 | 任务完成时间 |
| start_location_id | varchar(255) | 是 | NULL | 否 | 起始点位id |
| end_location_id | varchar(255) | 是 | NULL | 否 | 目标点位id |
| container_id | varchar(255) | 是 | NULL | 否 | 容器id |
| task_type_id | varchar(255) | 是 | NULL | 否 | 任务类型管理id |
| business_config_id | varchar(36) | 是 | NULL | 否 | 业务配置ID |
| status | varchar(255) | 是 | NULL | 否 | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| group_status | varchar(50) | 是 | NULL | 否 | 任务组状态：10 创建，20 进行中，50 完成，60 取消，80 终止 |
| dispatch | varchar(50) | 是 | NULL | 否 | 是否调度：1 未调度，2已调度 |
| button_code | varchar(32) | 是 | NULL | 否 | 按钮编号 |
| conditional_combination_id | varchar(32) | 是 | NULL | 否 | 条件组ID |
| rule_id | varchar(32) | 是 | NULL | 否 | 规则ID |
| is_exception | int | 是 | NULL | 否 | 是否异常，1是，2否 |
| good_type | varchar(10) | 是 | NULL | 否 | 下发RCS时携带的货型编码(优先取自规则, 其次需求, 默认1) |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| task_sort | tinyint | 是 | NULL | 否 | 子任务排序 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_pid_code | 否 | `pid_code` |
| idx_location_ids | 否 | `start_location_id`,`end_location_id` |
| idx_covering_query | 否 | `start_location_id`(100),`end_location_id`(100),`container_id`,`business_config_id`,`task_type_id` |
| idx_task_code | 否 | `task_code` |


## tms_task_poll_status

- 表说明：TMS任务池中任务状态详情
- 存储引擎：InnoDB
- 字段数：7

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| task_poll_id | varchar(255) | 是 | NULL | 否 | TMS任务id |
| status | varchar(255) | 是 | NULL | 否 | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |
| idx_task_poll_id_status | 否 | `task_poll_id` |


## tms_task_retrigger

- 表说明：容器任务下发RCS失败的记录
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 是 | NULL | 否 |  |
| task_poll_id | varchar(255) | 是 | NULL | 否 | 容器任务ID |
| status | varchar(255) | 是 | NULL | 否 | 状态: 1 再次触发失败, 2 再次触发成功 |
| number_of_triggers | int | 是 | NULL | 否 | 再次触发次数 |
| remark | longtext | 是 | - | 否 | 备注 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

_SQL未声明索引。_


## tms_task_type_range

- 表说明：逻辑区管理
- 存储引擎：InnoDB
- 字段数：12

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| range_code | varchar(255) | 是 | NULL | 否 | 范围编码 |
| range_name | varchar(255) | 是 | NULL | 否 | 范围名称 |
| storage_location_ids | text | 是 | - | 否 | 逻辑包含库位ID组 |
| logical_area_tag_ids | varchar(255) | 是 | NULL | 否 | 逻辑区标签 |
| user_ids | varchar(255) | 是 | NULL | 否 | 用户ID |
| status | varchar(32) | 是 | NULL | 否 | 状态 |
| is_show | varchar(10) | 是 | NULL | 否 | 是否PDA显示：1 是，2 否 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

_SQL未声明索引。_


## tms_task_type_route

- 表说明：任务类型：电梯+路由
- 存储引擎：InnoDB
- 字段数：9

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| name | varchar(255) | 是 | NULL | 否 | 名称由电梯+路由组成 |
| type | varchar(10) | 是 | NULL | 否 | 字段是目标层数, 与门对应的用name查询\r\n |
| target_tier | int | 是 | NULL | 否 | 目标层 |
| dict_value | varchar(10) | 是 | NULL | 否 | 字典值 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_task_upstream

- 表说明：TMS上游任务表
- 存储引擎：InnoDB
- 字段数：23

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(255) | 否 | - | 否 |  |
| task_code | varchar(255) | 是 | NULL | 否 | 任务编号 |
| pid_code | varchar(255) | 是 | NULL | 否 | 任务父编号 |
| task_type | varchar(255) | 是 | NULL | 否 | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7打包台6任务类型2 |
| task_source | varchar(255) | 是 | NULL | 否 | 任务来源 1 海康 2 未来 |
| task_priority | varchar(255) | 是 | NULL | 否 | 任务优先级 |
| issue_time | datetime | 是 | NULL | 否 | 任务下发时间 |
| task_over_time | datetime | 是 | NULL | 否 | 任务完成时间 |
| start_location_id | varchar(255) | 是 | NULL | 否 | 起始点位id |
| end_location_id | varchar(255) | 是 | NULL | 否 | 目标点位id |
| container_id | varchar(255) | 是 | NULL | 否 | 容器id |
| task_type_id | varchar(255) | 是 | NULL | 否 | 任务类型管理id |
| status | varchar(255) | 是 | NULL | 否 | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| vehicle_code | varchar(255) | 是 | NULL | 否 | 执行车辆编号 |
| task_poll_id | varchar(50) | 是 | NULL | 否 | 任务池id |
| business_config_id | varchar(36) | 是 | NULL | 否 | 业务配置ID |
| conditional_combination_id | varchar(32) | 是 | NULL | 否 | 条件组ID |
| rule_id | varchar(32) | 是 | NULL | 否 | 规则ID |
| is_exception | int | 是 | NULL | 否 | 是否异常，1是，2否 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_units

- 表说明：单位管理
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 单位编码 |
| name | varchar(255) | 是 | NULL | 否 | 单位名称 |
| status | tinyint | 是 | NULL | 否 | 状态(0 禁用, 1 启用) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_vehicle

- 表说明：车辆管理
- 存储引擎：InnoDB
- 字段数：19

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| vehicle_code | varchar(255) | 是 | NULL | 否 | 车辆编码 |
| vehicle_group_id | varchar(255) | 是 | NULL | 否 | 车辆分组id |
| vehicle_group_name | varchar(255) | 是 | NULL | 否 | 车辆分组 |
| vehicle_type_id | varchar(36) | 是 | NULL | 否 | 车型 |
| vehicle_type_name | varchar(255) | 是 | NULL | 否 | 车辆类型名称 |
| vehicle_type_code | varchar(255) | 是 | NULL | 否 | 车辆类型编码 |
| vehicle_source | varchar(255) | 是 | NULL | 否 | 车辆来源 |
| vehicle_kw | varchar(255) | 是 | NULL | 否 | 车辆电量 |
| status | varchar(32) | 是 | NULL | 否 | 状态 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| rfid_read_code | varchar(255) | 是 | NULL | 否 | RFID读头编码 |
| pos_x | varchar(255) | 是 | NULL | 否 | 车辆X坐标 |
| pos_y | varchar(255) | 是 | NULL | 否 | 车辆Y坐标 |
| map_code | varchar(255) | 是 | NULL | 否 | 车辆所在地图 |
| run_status | varchar(255) | 是 | NULL | 否 | 车辆运行状态 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_vehicle_group

- 表说明：车辆分组表
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| vehicle_group_code | varchar(255) | 是 | NULL | 否 | 车辆分组编码 |
| vehicle_group_name | varchar(255) | 是 | NULL | 否 | 车辆分组 |
| status | varchar(32) | 是 | NULL | 否 | 状态 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_vehicle_type

- 表说明：车型管理
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 |  |
| vehicle_type_code | varchar(255) | 是 | NULL | 否 | 车型编码 |
| vehicle_type_name | varchar(255) | 是 | NULL | 否 | 车型名称 |
| status | varchar(32) | 是 | NULL | 否 | 状态 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_warehouse

- 表说明：仓库管理
- 存储引擎：InnoDB
- 字段数：11

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(36) | 否 | - | 否 | 主键 |
| warehouse_code | varchar(255) | 是 | NULL | 否 | 仓库编码 |
| warehouse_name | varchar(255) | 是 | NULL | 否 | 仓库名称 |
| contacts | varchar(32) | 是 | NULL | 否 | 联系人 |
| contacts_number | varchar(32) | 是 | NULL | 否 | 联系电话 |
| warehouse_address | text | 是 | - | 否 | 仓库地址 |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 正常，2 禁用 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |


## tms_work_order

- 表说明：工单表
- 存储引擎：InnoDB
- 字段数：13

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(50) | 否 | - | 否 |  |
| work_order_number | varchar(50) | 是 | NULL | 否 | 工单号 |
| material_name | varchar(255) | 是 | NULL | 否 | 物料名称 |
| material_code | varchar(255) | 是 | NULL | 否 | 物料编码 |
| process_route_id | varchar(255) | 是 | NULL | 否 | 工艺路线id |
| status | varchar(32) | 是 | NULL | 否 | 状态：1 启用，2 禁用 |
| business_status | char(1) | 是 | NULL | 否 | 业务状态 (1-开始，2-完工) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(50) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 修改时间 |
| update_by | varchar(50) | 是 | NULL | 否 | 修改人 |
| units_id | varchar(255) | 是 | NULL | 否 | 公司ID |
| work_space_code | varchar(255) | 是 | NULL | 否 | 工作中心编码 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| id | 是 | `id` |
| work_order_number | 是 | `work_order_number` |


## tms_work_space

- 表说明：工作中心主数据
- 存储引擎：InnoDB
- 字段数：8

| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |
|---|---|---:|---|---:|---|
| id | varchar(64) | 否 | - | 否 |  |
| code | varchar(255) | 是 | NULL | 否 | 工作中心编码 |
| name | varchar(255) | 是 | NULL | 否 | 工作中心名称 |
| status | tinyint | 是 | NULL | 否 | 状态(0 禁用, 1 启用) |
| create_time | datetime | 是 | NULL | 否 | 创建时间 |
| create_by | varchar(255) | 是 | NULL | 否 | 创建人 |
| update_time | datetime | 是 | NULL | 否 | 更新时间 |
| update_by | varchar(255) | 是 | NULL | 否 | 更新人 |

索引：

| 索引 | 唯一 | 字段 |
|---|---:|---|
| PRIMARY | 是 | `id` |

