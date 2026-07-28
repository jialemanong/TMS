# TMS V2 数据库全表索引

> 来源：`../raw/tms_v2.sql`，采集日期：2026-07-28。表说明和字段说明均来自DDL注释。

## 分类统计

| 分类 | 表数 |
|---|---:|
| 示例 | 11 |
| 报表 | 14 |
| 在线表单 | 13 |
| 其他 | 11 |
| Quartz调度 | 11 |
| Jeecg系统 | 39 |
| TMS业务 | 80 |

合计：179 张表。

## 全表清单

### 示例

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| ceshi_note |  | 25 | 1 |
| demo |  | 18 | 1 |
| demo_field_def_val_main |  | 11 | 1 |
| demo_field_def_val_sub |  | 10 | 1 |
| demo_field_def_val_sub_copy1 |  | 10 | 1 |
| jeecg_monthly_growth_analysis |  | 5 | 1 |
| jeecg_order_customer |  | 11 | 1 |
| jeecg_order_main |  | 11 | 1 |
| jeecg_order_ticket |  | 8 | 1 |
| jeecg_project_nature_income |  | 8 | 1 |
| joa_demo | 流程测试 | 11 | 0 |

### 报表

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| jimu_dict |  | 11 | 2 |
| jimu_dict_item |  | 11 | 5 |
| jimu_report | 在线excel设计器 | 21 | 4 |
| jimu_report_data_source |  | 17 | 3 |
| jimu_report_db |  | 24 | 4 |
| jimu_report_db_field |  | 17 | 3 |
| jimu_report_db_param |  | 16 | 2 |
| jimu_report_link | 超链接配置表 | 10 | 2 |
| jimu_report_map | 地图配置表 | 10 | 2 |
| jimu_report_share | 积木报表预览权限表 | 8 | 1 |
| rep_demo_dxtj |  | 10 | 1 |
| rep_demo_employee |  | 32 | 1 |
| rep_demo_gongsi |  | 7 | 1 |
| rep_demo_jianpiao |  | 10 | 1 |

### 在线表单

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| onl_auth_data |  | 11 | 1 |
| onl_auth_page |  | 11 | 1 |
| onl_auth_relation |  | 6 | 1 |
| onl_cgform_button | Online表单自定义按钮 | 11 | 5 |
| onl_cgform_enhance_java |  | 7 | 4 |
| onl_cgform_enhance_js |  | 5 | 3 |
| onl_cgform_enhance_sql |  | 6 | 2 |
| onl_cgform_field |  | 44 | 2 |
| onl_cgform_head |  | 34 | 5 |
| onl_cgform_index |  | 11 | 2 |
| onl_cgreport_head |  | 14 | 3 |
| onl_cgreport_item |  | 20 | 4 |
| onl_cgreport_param |  | 10 | 2 |

### 其他

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| oss_file | Oss File | 7 | 1 |
| test_demo |  | 19 | 1 |
| test_enhance_select |  | 6 | 1 |
| test_note |  | 11 | 1 |
| test_order_customer |  | 12 | 1 |
| test_order_main |  | 9 | 1 |
| test_order_product |  | 11 | 1 |
| test_shoptype_tree |  | 10 | 1 |
| test_v3_hello |  | 13 | 1 |
| tmp_report_data_1 |  | 6 | 0 |
| tmp_report_data_income |  | 8 | 0 |

### Quartz调度

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| qrtz_blob_triggers |  | 4 | 1 |
| qrtz_calendars |  | 3 | 1 |
| qrtz_cron_triggers |  | 5 | 1 |
| qrtz_fired_triggers |  | 13 | 1 |
| qrtz_job_details |  | 10 | 1 |
| qrtz_locks |  | 2 | 1 |
| qrtz_paused_trigger_grps |  | 2 | 1 |
| qrtz_scheduler_state |  | 4 | 1 |
| qrtz_simple_triggers |  | 6 | 1 |
| qrtz_simprop_triggers |  | 14 | 1 |
| qrtz_triggers |  | 16 | 2 |

### Jeecg系统

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| sys_announcement | 系统通告表 | 25 | 1 |
| sys_announcement_send | 用户通告阅读标记表 | 10 | 0 |
| sys_category |  | 11 | 3 |
| sys_check_rule |  | 9 | 2 |
| sys_comment | 系统评论回复表 | 11 | 2 |
| sys_data_log |  | 10 | 2 |
| sys_data_source |  | 16 | 2 |
| sys_depart | 组织机构表 | 23 | 5 |
| sys_depart_permission | 部门权限表 | 4 | 1 |
| sys_depart_role | 部门角色表 | 9 | 1 |
| sys_depart_role_permission | 部门角色权限表 | 7 | 4 |
| sys_depart_role_user | 部门角色用户表 | 3 | 1 |
| sys_dict | 字典类型 | 12 | 2 |
| sys_dict_item | 数据字典 | 13 | 5 |
| sys_files | 知识库-文档管理 | 22 | 3 |
| sys_fill_rule |  | 9 | 2 |
| sys_form_file |  | 7 | 3 |
| sys_gateway_route |  | 16 | 1 |
| sys_log | 系统日志表 | 17 | 5 |
| sys_permission | 菜单权限表 | 30 | 4 |
| sys_permission_data_rule |  | 11 | 2 |
| sys_permission_v2 | 菜单权限表 | 27 | 9 |
| sys_position |  | 11 | 2 |
| sys_quartz_job |  | 11 | 1 |
| sys_role | 后台管理角色表 | 10 | 3 |
| sys_role_index | 角色首页表 | 12 | 1 |
| sys_role_permission | 角色权限表 | 6 | 4 |
| sys_sms |  | 15 | 5 |
| sys_sms_template |  | 11 | 2 |
| sys_tenant | 多租户信息表 | 21 | 1 |
| sys_tenant_pack | 租户产品包 | 10 | 1 |
| sys_tenant_pack_perms | 租户产品包和菜单关系表 | 7 | 1 |
| sys_tenant_pack_user | 租户套餐人员表 | 9 | 1 |
| sys_third_account |  | 13 | 2 |
| sys_user | 用户表 | 29 | 8 |
| sys_user_agent | 用户代理人设置 | 14 | 5 |
| sys_user_depart |  | 3 | 4 |
| sys_user_role | 用户角色表 | 4 | 4 |
| sys_user_tenant | 用户租户关系表 | 8 | 4 |

### TMS业务

| 表名 | 表说明 | 字段数 | 索引数 |
|---|---|---:|---:|
| tms_agv_error | AGV异常管理 | 10 | 1 |
| tms_broadcast_speech | 广播语 | 10 | 1 |
| tms_broadcast_template | 广播模板 | 10 | 1 |
| tms_components | 部件主数据 | 8 | 1 |
| tms_condition | 条件组条件明细表 | 14 | 2 |
| tms_condition_group | 条件分组 | 9 | 2 |
| tms_condition_table | TMS条件+规则的模块+字段设置 | 6 | 3 |
| tms_condition_table_column | TMS条件+规则字段配置表 | 8 | 2 |
| tms_conditional_combination | 条件组主表 | 8 | 1 |
| tms_config | 系统参数表 | 9 | 1 |
| tms_container | 容器管理 | 16 | 1 |
| tms_control_area_log | 管制区任务指令 | 13 | 1 |
| tms_demand_condition | 弃用----记录需求池条件表(标识需求配置) | 10 | 1 |
| tms_demand_poll | 【需求池】 | 83 | 1 |
| tms_depth_group | 深度组管理 | 21 | 1 |
| tms_depth_group_copy1 | 深度组管理—中华商务备份 | 18 | 1 |
| tms_device | 设备主表 | 18 | 2 |
| tms_device_interface | 设备明细表 | 26 | 3 |
| tms_device_interface_event | 设备事件关联表 | 9 | 1 |
| tms_door | 门 | 17 | 1 |
| tms_door_control_area | 管制区与门对照表 | 8 | 1 |
| tms_event | 事件 | 9 | 1 |
| tms_event_parameter | 参数主表 | 8 | 1 |
| tms_event_parameter_item | 参数明细表 | 11 | 1 |
| tms_event_process_record | 事件处理记录表 | 17 | 1 |
| tms_flow_card | 流程卡表 | 42 | 1 |
| tms_flow_card_copy1 | 流程卡表 | 42 | 1 |
| tms_goods_type | 货型管理 | 12 | 1 |
| tms_location_container | 库位与容器中间表 | 7 | 2 |
| tms_logical_area_tag | 逻辑区标签 | 8 | 0 |
| tms_machine | 机台主数据 | 8 | 1 |
| tms_machine_data | 机台实时数据 | 22 | 1 |
| tms_monitoring_source_log | 资源监控日志 | 13 | 1 |
| tms_nail | 钉式主数据 | 8 | 1 |
| tms_operation_rule | 操作型规则 | 12 | 1 |
| tms_operation_rule_event | 操作型规则事件关联表 | 9 | 1 |
| tms_paramter_mapping | 监控资源记录-无用 | 11 | 0 |
| tms_pda_log | PDA操作日志 | 14 | 1 |
| tms_pda_permission | PDA菜单表 | 9 | 1 |
| tms_pda_role | PDA用户角色表 | 10 | 1 |
| tms_pda_role_permission | 角色权限表 | 5 | 1 |
| tms_pda_user | PDA用户表 | 11 | 1 |
| tms_pda_user_cache | PDA用户信息 | 12 | 1 |
| tms_pda_user_role | 用户角色关联表 | 3 | 1 |
| tms_process | 工序表 | 11 | 1 |
| tms_process_copy1 | 工序表 | 11 | 2 |
| tms_process_route | 工艺路线 | 8 | 1 |
| tms_process_route_process | 工序 工艺路线 中间表\r\n | 8 | 0 |
| tms_query_demand_log | 查询需求池日志 | 10 | 1 |
| tms_router | 路由管理 | 12 | 3 |
| tms_rule | 规则管理 | 24 | 1 |
| tms_rule_dict | 上下架规则设置 | 14 | 1 |
| tms_send_http_log | 调用第三方接口日志记录表 | 10 | 1 |
| tms_source_change_record | 资源变更记录表 | 13 | 1 |
| tms_storage_cavern | 储区管理 | 14 | 1 |
| tms_storage_cavern_type | 储区分类 | 14 | 1 |
| tms_storage_history | PAD常用储位记录 | 12 | 1 |
| tms_storage_location | 储位管理 | 56 | 4 |
| tms_storage_location_copy1 | 储位管理 | 51 | 2 |
| tms_storage_location_copy2 | 储位管理 | 52 | 4 |
| tms_storage_location_copy3 | 储位管理—中华商务备份 | 56 | 4 |
| tms_strategy | 策略主表 | 12 | 1 |
| tms_strategy_action | 策略行为表 | 13 | 1 |
| tms_strategy_action_event | 策略事件 | 9 | 1 |
| tms_strategy_action_event_parameter_item | 策略事件参数明细 | 12 | 1 |
| tms_task | TMS车辆任务 | 23 | 2 |
| tms_task_abnormal | RCS异常任务记录 | 16 | 1 |
| tms_task_poll | 容器任务池+任务组 | 26 | 5 |
| tms_task_poll_status | TMS任务池中任务状态详情 | 7 | 2 |
| tms_task_retrigger | 容器任务下发RCS失败的记录 | 9 | 0 |
| tms_task_type_range | 逻辑区管理 | 12 | 0 |
| tms_task_type_route | 任务类型：电梯+路由 | 9 | 1 |
| tms_task_upstream | TMS上游任务表 | 23 | 1 |
| tms_units | 单位管理 | 8 | 1 |
| tms_vehicle | 车辆管理 | 19 | 1 |
| tms_vehicle_group | 车辆分组表 | 8 | 1 |
| tms_vehicle_type | 车型管理 | 8 | 1 |
| tms_warehouse | 仓库管理 | 11 | 1 |
| tms_work_order | 工单表 | 13 | 2 |
| tms_work_space | 工作中心主数据 | 8 | 1 |

