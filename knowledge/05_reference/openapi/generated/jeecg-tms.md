# TMS 核心后台接口明细

> 来源：`../raw/jeecg-tms.swagger.json`。本文由生成器自动生成，请勿手工修改生成区内容。

## 服务信息

- 服务标识：`jeecg-tms`
- 网关地址：`http://111.160.91.170:59999`
- Base Path：`/jeecg-tms`
- 鉴权头：`X-Access-Token`
- 路径数：283
- 接口操作数：327
- 数据模型数：225

## 控制器索引

| 控制器/标签 | 接口数 |
|---|---:|
| 仓库管理 | 7 |
| 操作型规则管理 | 7 |
| 策略管理 | 7 |
| 查询需求日志 | 7 |
| 车辆分组管理 | 8 |
| 车辆管理 | 7 |
| 车型管理 | 7 |
| 储区管理 | 7 |
| 储区类型 | 7 |
| 储位报表 | 1 |
| 储位管理 | 8 |
| 调用外部系统日志 | 7 |
| 工单管理 | 7 |
| 工序管理 | 8 |
| 工艺路线 | 7 |
| 管制区日志 | 7 |
| 广播模板 | 7 |
| 广播语 | 8 |
| 规则管理 | 7 |
| 规则上下架配置 | 7 |
| 货型管理 | 7 |
| 监控资源日志 | 7 |
| 流程卡管理 | 14 |
| 路由管理 | 7 |
| 逻辑区标签 | 7 |
| 逻辑区管理 | 7 |
| 门 | 7 |
| 任务类型 | 7 |
| 任务类型管理 | 7 |
| 容器管理 | 7 |
| 容器任务 | 10 |
| 容器任务时间记录 | 1 |
| 设备储位绑定 | 7 |
| 深度组 | 9 |
| 条件管理 | 7 |
| 条件组管理 | 7 |
| 系统开关 | 6 |
| 系统配置 | 9 |
| 小车任务 | 7 |
| 需求池 | 7 |
| 需求条件配置 | 7 |
| 业务配置 | 7 |
| 异常信息管理 | 7 |
| AGV异常日志 | 7 |
| PDA日志 | 7 |
| TMS任务组 | 7 |

## 接口清单

### 仓库管理

#### POST /jeecg-tms/tmsServer/tmsWarehouse/add

- 名称：仓库管理-添加
- Operation ID：`addUsingPOST_41`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWarehouse | body | 是 | tms_warehouse对象 | tmsWarehouse |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsWarehouse/delete

- 名称：仓库管理-通过id删除
- Operation ID：`deleteUsingDELETE_41`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsWarehouse/deleteBatch

- 名称：仓库管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_41`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsWarehouse/edit

- 名称：仓库管理-编辑
- Operation ID：`editUsingPOST_41`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWarehouse | body | 是 | tms_warehouse对象 | tmsWarehouse |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsWarehouse/edit

- 名称：仓库管理-编辑
- Operation ID：`editUsingPUT_41`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWarehouse | body | 是 | tms_warehouse对象 | tmsWarehouse |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsWarehouse/list

- 名称：仓库管理-分页列表查询
- Operation ID：`queryPageListUsingGET_43`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| contacts | query | 否 | string | 联系人 |
| contactsNumber | query | 否 | string | 联系电话 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | 主键 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| warehouseAddress | query | 否 | string | 仓库地址 |
| warehouseCode | query | 否 | string | 仓库编码 |
| warehouseName | query | 否 | string | 仓库名称 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_warehouse对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsWarehouse/queryById

- 名称：仓库管理-通过id查询
- Operation ID：`queryByIdUsingGET_41`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_warehouse对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 操作型规则管理

#### POST /jeecg-tms/tmsServer/tmsOperationRule/add

- 名称：操作型规则管理-添加
- Operation ID：`addUsingPOST_17`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsOperationRule | body | 是 | tms_operation_rule对象 | tmsOperationRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsOperationRule/delete

- 名称：操作型规则管理-通过id删除
- Operation ID：`deleteUsingDELETE_17`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsOperationRule/deleteBatch

- 名称：操作型规则管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_17`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsOperationRule/edit

- 名称：操作型规则管理-编辑
- Operation ID：`editUsingPOST_17`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsOperationRule | body | 是 | tms_operation_rule对象 | tmsOperationRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsOperationRule/edit

- 名称：操作型规则管理-编辑
- Operation ID：`editUsingPUT_17`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsOperationRule | body | 是 | tms_operation_rule对象 | tmsOperationRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsOperationRule/list

- 名称：操作型规则管理-分页列表查询
- Operation ID：`queryPageListUsingGET_17`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| broadcastSpeechId | query | 否 | string | 广播语事件ID |
| code | query | 否 | string | 操作型规则编码 |
| conditionalCombinationId | query | 否 | string | 关联条件组ID |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| id | query | 否 | string | 主键 |
| name | query | 否 | string | 操作型规则名称 |
| operationType | query | 否 | string | 操作类型：1 解绑 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | query | 否 | string | 所属部门 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_operation_rule对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsOperationRule/queryById

- 名称：操作型规则管理-通过id查询
- Operation ID：`queryByIdUsingGET_17`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_operation_rule对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 策略管理

#### POST /jeecg-tms/tmsServer/tmsStrategy/add

- 名称：策略管理-添加
- Operation ID：`addUsingPOST_30`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStrategy | body | 是 | tms_strategy对象1 | tmsStrategy |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsStrategy/delete

- 名称：策略管理-通过id删除
- Operation ID：`deleteUsingDELETE_30`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsStrategy/deleteBatch

- 名称：策略管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_30`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsStrategy/edit

- 名称：策略管理-编辑
- Operation ID：`editUsingPOST_30`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStrategy | body | 是 | tms_strategy对象1 | tmsStrategy |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsStrategy/edit

- 名称：策略管理-编辑
- Operation ID：`editUsingPUT_30`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStrategy | body | 是 | tms_strategy对象1 | tmsStrategy |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStrategy/list

- 名称：策略管理-分页列表查询
- Operation ID：`queryPageListUsingGET_31`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| containerInitStatus | query | 否 | string | 容器初始状态：0 空，1 满，2 满+1 |
| createBy | query | 否 | string | 创建人 |
| createContainer | query | 否 | string | 是否创建容器：1 创建，2 不创建 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| flageTwo | query | 否 | string | 标识2 |
| flagOne | query | 否 | string | 标识1 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| strategyCode | query | 否 | string | 策略编码 |
| strategyName | query | 否 | string | 策略名称 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_strategy对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStrategy/queryById

- 名称：策略管理-通过id查询
- Operation ID：`queryByIdUsingGET_30`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_strategy对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 查询需求日志

#### POST /jeecg-tms/tmsServer/tmsQueryDemandLog/add

- 名称：查询需求日志-添加
- Operation ID：`addUsingPOST_21`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsQueryDemandLog | body | 是 | tms_query_demand_log对象 | tmsQueryDemandLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsQueryDemandLog/delete

- 名称：查询需求日志-通过id删除
- Operation ID：`deleteUsingDELETE_21`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsQueryDemandLog/deleteBatch

- 名称：查询需求日志-批量删除
- Operation ID：`deleteBatchUsingDELETE_21`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsQueryDemandLog/edit

- 名称：查询需求日志-编辑
- Operation ID：`editUsingPOST_21`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsQueryDemandLog | body | 是 | tms_query_demand_log对象 | tmsQueryDemandLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsQueryDemandLog/edit

- 名称：查询需求日志-编辑
- Operation ID：`editUsingPUT_21`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsQueryDemandLog | body | 是 | tms_query_demand_log对象 | tmsQueryDemandLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsQueryDemandLog/list

- 名称：查询需求日志-分页列表查询
- Operation ID：`queryPageListUsingGET_21`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| demandId | query | 否 | string | 被查询需求池的需求ID |
| endTime | query | 否 | string(date-time) | 结束查询时间 |
| id | query | 否 | string | id |
| monitoringLogId | query | 否 | string | 监控资源日志ID |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| queryDemandId | query | 否 | string | 查询需求池日志ID |
| startTime | query | 否 | string(date-time) | 开始查询时间 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_query_demand_log对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsQueryDemandLog/queryById

- 名称：查询需求日志-通过id查询
- Operation ID：`queryByIdUsingGET_21`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_query_demand_log对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 车辆分组管理

#### POST /jeecg-tms/tmsServer/tmsVehicleGroup/add

- 名称：车辆分组管理-添加
- Operation ID：`addUsingPOST_39`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleGroup | body | 是 | tms_vehicle_group对象 | tmsVehicleGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsVehicleGroup/delete

- 名称：车辆分组管理-通过id删除
- Operation ID：`deleteUsingDELETE_39`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsVehicleGroup/deleteBatch

- 名称：车辆分组管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_39`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsVehicleGroup/edit

- 名称：车辆分组管理-编辑
- Operation ID：`editUsingPOST_39`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleGroup | body | 是 | tms_vehicle_group对象 | tmsVehicleGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsVehicleGroup/edit

- 名称：车辆分组管理-编辑
- Operation ID：`editUsingPUT_39`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleGroup | body | 是 | tms_vehicle_group对象 | tmsVehicleGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicleGroup/list

- 名称：车辆分组管理-分页列表查询
- Operation ID：`queryPageListUsingGET_41`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleGroupCode | query | 否 | string | 车辆分组编码 |
| vehicleGroupName | query | 否 | string | 车辆分组 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_vehicle_group对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicleGroup/noPageList

- 名称：车辆分组管理-分页列表查询
- Operation ID：`queryNoPageListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| status | query | 否 | string | 状态 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleGroupCode | query | 否 | string | 车辆分组编码 |
| vehicleGroupName | query | 否 | string | 车辆分组 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_vehicle_group对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicleGroup/queryById

- 名称：车辆分组管理-通过id查询
- Operation ID：`queryByIdUsingGET_39`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_vehicle_group对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 车辆管理

#### POST /jeecg-tms/tmsServer/tmsVehicle/add

- 名称：车辆管理-添加
- Operation ID：`addUsingPOST_38`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicle | body | 是 | tms_vehicle对象 | tmsVehicle |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsVehicle/delete

- 名称：车辆管理-通过id删除
- Operation ID：`deleteUsingDELETE_38`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsVehicle/deleteBatch

- 名称：车辆管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_38`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsVehicle/edit

- 名称：车辆管理-编辑
- Operation ID：`editUsingPOST_38`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicle | body | 是 | tms_vehicle对象 | tmsVehicle |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsVehicle/edit

- 名称：车辆管理-编辑
- Operation ID：`editUsingPUT_38`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicle | body | 是 | tms_vehicle对象 | tmsVehicle |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicle/list

- 名称：车辆管理-分页列表查询
- Operation ID：`queryPageListUsingGET_40`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| mapCode | query | 否 | string | 车辆所在地图 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| posX | query | 否 | string | 车辆X坐标 |
| posY | query | 否 | string | 车辆Y坐标 |
| runStatus | query | 否 | string | 车辆运行状态 |
| status | query | 否 | string | 状态 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleCode | query | 否 | string | 车辆编码 |
| vehicleGroupCodes | query | 否 | string | - |
| vehicleGroupId | query | 否 | string | 车辆分组 |
| vehicleGroupName | query | 否 | string | 车辆分组 |
| vehicleKw | query | 否 | string | 车辆电量 |
| vehicleSource | query | 否 | string | 车辆来源 |
| vehicleTypeCode | query | 否 | string | 车辆类型编码 |
| vehicleTypeId | query | 否 | string | 车型 |
| vehicleTypeName | query | 否 | string | 车辆类型名称 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_vehicle对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicle/queryById

- 名称：车辆管理-通过id查询
- Operation ID：`queryByIdUsingGET_38`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_vehicle对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 车型管理

#### POST /jeecg-tms/tmsServer/tmsVehicleType/add

- 名称：车型管理-添加
- Operation ID：`addUsingPOST_40`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleType | body | 是 | tms_vehicle_type对象 | tmsVehicleType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsVehicleType/delete

- 名称：车型管理-通过id删除
- Operation ID：`deleteUsingDELETE_40`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsVehicleType/deleteBatch

- 名称：车型管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_40`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsVehicleType/edit

- 名称：车型管理-编辑
- Operation ID：`editUsingPOST_40`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleType | body | 是 | tms_vehicle_type对象 | tmsVehicleType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsVehicleType/edit

- 名称：车型管理-编辑
- Operation ID：`editUsingPUT_40`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsVehicleType | body | 是 | tms_vehicle_type对象 | tmsVehicleType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicleType/list

- 名称：车型管理-分页列表查询
- Operation ID：`queryPageListUsingGET_42`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleTypeCode | query | 否 | string | 车型编码 |
| vehicleTypeName | query | 否 | string | 车型名称 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_vehicle_type对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsVehicleType/queryById

- 名称：车型管理-通过id查询
- Operation ID：`queryByIdUsingGET_40`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_vehicle_type对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 储区管理

#### POST /jeecg-tms/tmsServer/tmsStorageCavern/add

- 名称：储区管理-添加
- Operation ID：`addUsingPOST_26`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavern | body | 是 | tms_storage_cavern对象0 | tmsStorageCavern |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsStorageCavern/delete

- 名称：储区管理-通过id删除
- Operation ID：`deleteUsingDELETE_26`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsStorageCavern/deleteBatch

- 名称：储区管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_26`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsStorageCavern/edit

- 名称：储区管理-编辑
- Operation ID：`editUsingPOST_26`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavern | body | 是 | tms_storage_cavern对象0 | tmsStorageCavern |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsStorageCavern/edit

- 名称：储区管理-编辑
- Operation ID：`editUsingPUT_26`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavern | body | 是 | tms_storage_cavern对象0 | tmsStorageCavern |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageCavern/list

- 名称：储区管理-分页列表查询
- Operation ID：`queryPageListUsingGET_27`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessId | query | 否 | string | 库区业务id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| direction | query | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| singleOrDouble | query | 否 | string | 深度组方向：1 单向，2 双向 |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | query | 否 | string | 库区编码 |
| storageCavernName | query | 否 | string | 库区名称 |
| storageCavernType | query | 否 | string | 库区类型 |
| typeName | query | 否 | string | - |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| warehouseCode | query | 否 | string | - |
| warehouseId | query | 否 | string | 仓库id |
| warehouseName | query | 否 | string | - |
| workshop | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_storage_cavern对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageCavern/queryById

- 名称：储区管理-通过id查询
- Operation ID：`queryByIdUsingGET_26`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_storage_cavern对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 储区类型

#### POST /jeecg-tms/tmsServer/tmsStorageCavernType/add

- 名称：储区类型-添加
- Operation ID：`addUsingPOST_27`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavernType | body | 是 | tms_storage_cavern_type对象 | tmsStorageCavernType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsStorageCavernType/delete

- 名称：储区类型-通过id删除
- Operation ID：`deleteUsingDELETE_27`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsStorageCavernType/deleteBatch

- 名称：储区类型-批量删除
- Operation ID：`deleteBatchUsingDELETE_27`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsStorageCavernType/edit

- 名称：储区类型-编辑
- Operation ID：`editUsingPOST_27`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavernType | body | 是 | tms_storage_cavern_type对象 | tmsStorageCavernType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsStorageCavernType/edit

- 名称：储区类型-编辑
- Operation ID：`editUsingPUT_27`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageCavernType | body | 是 | tms_storage_cavern_type对象 | tmsStorageCavernType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageCavernType/list

- 名称：储区类型-分页列表查询
- Operation ID：`queryPageListUsingGET_28`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| equipmentDomain | query | 否 | string | 设备域名 |
| equipmentIp | query | 否 | string | 设备IP |
| equipmentPort | query | 否 | string | 设备端口 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| remakr | query | 否 | string | 备注 |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| storageLocationTheir | query | 否 | string | 储位所属 1储区，2容器 |
| type | query | 否 | string | 类型：1 设备，2 人工 |
| typeCode | query | 否 | string | 库区类型编码 |
| typeName | query | 否 | string | 库区类型名称 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_storage_cavern_type对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageCavernType/queryById

- 名称：储区类型-通过id查询
- Operation ID：`queryByIdUsingGET_27`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_storage_cavern_type对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 储位报表

#### GET /jeecg-tms/tmsServer/statement/list

- 名称：储位报表-分页列表查询
- Operation ID：`queryPageListUsingGET_26`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| cavernCode | query | 否 | string | - |
| containerCode | query | 否 | string | - |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| depthCode | query | 否 | string | - |
| flagEight | query | 否 | string | - |
| flagEleven | query | 否 | string | - |
| flagFive | query | 否 | string | - |
| flagFour | query | 否 | string | - |
| flagNine | query | 否 | string | - |
| flagOne | query | 否 | string | - |
| flagSeven | query | 否 | string | - |
| flagSix | query | 否 | string | - |
| flagTen | query | 否 | string | - |
| flagThree | query | 否 | string | - |
| flagTwelve | query | 否 | string | - |
| flagTwo | query | 否 | string | - |
| flowCardNo | query | 否 | string | - |
| id | query | 否 | string | 储位ID |
| ids | query | 否 | array<string> | - |
| locBusinessStatus | query | 否 | string | - |
| locCode | query | 否 | string | - |
| locStatus | query | 否 | string | - |
| locType | query | 否 | string | - |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |
| warehouseCode | query | 否 | string | - |
| workOrderNo | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«TmsLocStatement»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 储位管理

#### POST /jeecg-tms/tmsServer/tmsStorageLocation/add

- 名称：储位管理-添加
- Operation ID：`addUsingPOST_29`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocation | body | 是 | tms_storage_location对象 | tmsStorageLocation |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsStorageLocation/delete

- 名称：储位管理-通过id删除
- Operation ID：`deleteUsingDELETE_29`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsStorageLocation/deleteBatch

- 名称：储位管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_29`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsStorageLocation/edit

- 名称：储位管理-编辑
- Operation ID：`editUsingPOST_29`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocation | body | 是 | tms_storage_location对象 | tmsStorageLocation |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsStorageLocation/edit

- 名称：储位管理-编辑
- Operation ID：`editUsingPUT_29`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocation | body | 是 | tms_storage_location对象 | tmsStorageLocation |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageLocation/generateQrCode

- 名称：库位表-获取二维码
- Operation ID：`generateQrCodeUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageLocation/list

- 名称：储位管理-分页列表查询
- Operation ID：`queryPageListUsingGET_30`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| associativeContainerBindTime | query | 否 | string(date-time) | 关联容器的最新绑定时间 |
| associativeContainerUnbindTime | query | 否 | string(date-time) | 关联容器的最新解绑时间 |
| bay | query | 否 | string | BAY |
| businessId | query | 否 | string | 储位业务ID |
| cameraCode | query | 否 | string | 摄像头编码 |
| cavernBusinessId | query | 否 | string | 储区业务ID |
| channel | query | 否 | string | 通道 |
| columnNumber | query | 否 | integer(int32) | 列 |
| containerCode | query | 否 | string | 容器编码 |
| containerCodeList | query | 否 | string | 容器编码组 |
| containerId | query | 否 | string | 容器id |
| containerIdT | query | 否 | string | - |
| containerQuantity | query | 否 | integer(int32) | 容器数量 |
| coordinateX | query | 否 | string | 坐标X |
| coordinateY | query | 否 | string | 坐标y |
| coordinateZ | query | 否 | string | 坐标z |
| cover | query | 否 | string | 面 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| deep | query | 否 | string | 深 |
| deliveryTime | query | 否 | string(date-time) | 放货时间 |
| depthCode | query | 否 | string | 深度组编码 |
| depthDirection | query | 否 | string | 深度组方向：1 单向，2 双向 |
| depthOne | query | 否 | integer(int32) | 深度组1 |
| depthTwo | query | 否 | integer(int32) | 深度组2 |
| direction | query | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flag | query | 否 | string | 标识 |
| flag2 | query | 否 | string | 标识2 |
| hitTheShelfOrder | query | 否 | integer(int32) | 上架顺序 |
| id | query | 否 | string | id |
| isFreeze | query | 否 | string | 是否冻结：1 冻结，2 没冻结 |
| isGenerateQrCode | query | 否 | string | 是否生成储位码：1 不生成，2 生成 |
| isRetainContainer | query | 否 | string | 是否保留容器：1 是，2 否 |
| isScanOrCheck | query | 否 | string | 是否扫描校验：1 是，2 否 |
| lattice | query | 否 | string | 格 |
| length | query | 否 | string | 长 |
| maximumBoxQuantity | query | 否 | integer(int32) | 最大箱数量 |
| maximumCubage | query | 否 | string | 最大容积 |
| maximumLoadBearing | query | 否 | string | 最大承重 |
| maximumTrayQuantity | query | 否 | integer(int32) | 最大托盘数量 |
| mixedBatchQuantity | query | 否 | integer(int32) | 混放批次数量 |
| mixedQuantity | query | 否 | integer(int32) | 混放数量 |
| onlyGodKnows | query | 否 | string | - |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| residueBoxQuantity | query | 否 | integer(int32) | 剩余箱数量 |
| residueTrayQuantity | query | 否 | integer(int32) | 剩余托盘数量 |
| restrictionRule | query | 否 | string | 限制规则 |
| rowNumber | query | 否 | integer(int32) | 行 |
| soldOutOrder | query | 否 | integer(int32) | 下架顺序 |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | query | 否 | string | 储区编码 |
| storageCavernId | query | 否 | string | 储区id |
| storageCavernName | query | 否 | string | 储区名称 |
| storageLocationCode | query | 否 | string | 储位编码 |
| storageLocationName | query | 否 | string | 储位名称 |
| storageLocationQrCode | query | 否 | string | 储位二维码 |
| storageLocationStatus | query | 否 | string | 储位状态：0 占用，1 空闲，2 预占，3 超时 |
| storageLocationTheir | query | 否 | string | 储位所属：库区类型选择容器区，储位所属默认未容器 |
| storageLocationTheir1 | query | 否 | string | - |
| storageLocationType | query | 否 | string | 储位类型编码 |
| tier | query | 否 | string | 层 |
| typeName | query | 否 | string | - |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| volumeVacancyRate | query | 否 | string | 体积空置率 |
| warehouseCode | query | 否 | string | 仓库编码 |
| warehouseId | query | 否 | string | 仓库id |
| warehouseName | query | 否 | string | 仓库名称 |
| weightVacancyRate | query | 否 | string | 重量空置率 |
| width | query | 否 | string | 宽 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_storage_location对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageLocation/queryById

- 名称：储位管理-通过id查询
- Operation ID：`queryByIdUsingGET_29`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_storage_location对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 调用外部系统日志

#### POST /jeecg-tms/tmsServer/tmsSendHttpLog/add

- 名称：调用外部系统日志-添加
- Operation ID：`addUsingPOST_25`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsSendHttpLog | body | 是 | tms_send_http_log对象 | tmsSendHttpLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsSendHttpLog/delete

- 名称：调用外部系统日志-通过id删除
- Operation ID：`deleteUsingDELETE_25`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsSendHttpLog/deleteBatch

- 名称：调用外部系统日志-批量删除
- Operation ID：`deleteBatchUsingDELETE_25`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsSendHttpLog/edit

- 名称：调用外部系统日志-编辑
- Operation ID：`editUsingPOST_25`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsSendHttpLog | body | 是 | tms_send_http_log对象 | tmsSendHttpLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsSendHttpLog/edit

- 名称：调用外部系统日志-编辑
- Operation ID：`editUsingPUT_25`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsSendHttpLog | body | 是 | tms_send_http_log对象 | tmsSendHttpLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsSendHttpLog/list

- 名称：调用外部系统日志-分页列表查询
- Operation ID：`queryPageListUsingGET_25`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| i18nCode | query | 否 | string | - |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| remark | query | 否 | string | 备注 |
| requestParams | query | 否 | string | 请求参数 |
| requestUrl | query | 否 | string | 请求地址 |
| returnedValue | query | 否 | string | 接口返回值 |
| taskId | query | 否 | string | 任务id |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_send_http_log对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsSendHttpLog/queryById

- 名称：调用外部系统日志-通过id查询
- Operation ID：`queryByIdUsingGET_25`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_send_http_log对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 工单管理

#### POST /jeecg-tms/tmsServer/tmsWorkOrder/add

- 名称：工单管理-添加
- Operation ID：`addUsingPOST_42`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWorkOrder | body | 是 | tms_work_order对象 | tmsWorkOrder |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsWorkOrder/delete

- 名称：工单管理-通过id删除
- Operation ID：`deleteUsingDELETE_42`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsWorkOrder/deleteBatch

- 名称：工单管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_42`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsWorkOrder/edit

- 名称：工单管理-编辑
- Operation ID：`editUsingPOST_42`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWorkOrder | body | 是 | tms_work_order对象 | tmsWorkOrder |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsWorkOrder/edit

- 名称：工单管理-编辑
- Operation ID：`editUsingPUT_42`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsWorkOrder | body | 是 | tms_work_order对象 | tmsWorkOrder |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsWorkOrder/list

- 名称：工单管理-分页列表查询
- Operation ID：`queryPageListUsingGET_44`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessStatus | query | 否 | string | 业务状态：1 开始，2 完工 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endTime | query | 否 | string | - |
| flagEight | query | 否 | string | 标识8 |
| flagFive | query | 否 | string | 标识5 |
| flagFour | query | 否 | string | 标识4 |
| flagNine | query | 否 | string | 标识9 |
| flagOne | query | 否 | string | 标识1 |
| flagSeven | query | 否 | string | 标识7 |
| flagSix | query | 否 | string | 标识6 |
| flagTen | query | 否 | string | 标识10 |
| flagThree | query | 否 | string | 标识3 |
| flagTwo | query | 否 | string | 标识2 |
| id | query | 否 | string | id |
| materialCode | query | 否 | string | 物料编码 |
| materialName | query | 否 | string | 物料名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| processCodeGroup | query | 否 | string | 工序组（工艺路线）code |
| processRouteCode | query | 否 | string | - |
| processRouteId | query | 否 | string | 工艺路线ID |
| startTime | query | 否 | string | - |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| workOrderNumber | query | 否 | string | 工单号 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_work_order对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsWorkOrder/queryById

- 名称：工单管理-通过id查询
- Operation ID：`queryByIdUsingGET_42`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_work_order对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 工序管理

#### POST /jeecg-tms/tmsServer/tmsProcess/add

- 名称：工序管理-添加
- Operation ID：`addUsingPOST_19`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcess | body | 是 | tms_process对象 | tmsProcess |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsProcess/delete

- 名称：工序管理-通过id删除
- Operation ID：`deleteUsingDELETE_19`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsProcess/deleteBatch

- 名称：工序管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_19`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsProcess/edit

- 名称：工序管理-编辑
- Operation ID：`editUsingPOST_19`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcess | body | 是 | tms_process对象 | tmsProcess |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsProcess/edit

- 名称：工序管理-编辑
- Operation ID：`editUsingPUT_19`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcess | body | 是 | tms_process对象 | tmsProcess |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsProcess/list

- 名称：工序管理-分页列表查询
- Operation ID：`queryPageListUsingGET_19`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| outputUnit | query | 否 | string | 产出单位(米) |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| processCode | query | 否 | string | 工序编码 |
| processName | query | 否 | string | 工序名称 |
| processType | query | 否 | string | 工序分类名称 |
| productionUnit | query | 否 | string | 投产单位(米) |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_process对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsProcess/queryById

- 名称：工序管理-通过id查询
- Operation ID：`queryByIdUsingGET_19`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_process对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsProcess/useList

- 名称：工序管理-分页列表查询
- Operation ID：`queryPageUseListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| outputUnit | query | 否 | string | 产出单位(米) |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| processCode | query | 否 | string | 工序编码 |
| processName | query | 否 | string | 工序名称 |
| processType | query | 否 | string | 工序分类名称 |
| productionUnit | query | 否 | string | 投产单位(米) |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_process对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 工艺路线

#### POST /jeecg-tms/tmsServer/tmsProcessRoute/add

- 名称：工艺路线-添加
- Operation ID：`addUsingPOST_20`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcessRoute | body | 是 | tms_process_route对象0 | tmsProcessRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsProcessRoute/delete

- 名称：工艺路线-通过id删除
- Operation ID：`deleteUsingDELETE_20`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |
| num | query | 否 | string | num |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsProcessRoute/deleteBatch

- 名称：工艺路线-批量删除
- Operation ID：`deleteBatchUsingDELETE_20`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsProcessRoute/edit

- 名称：工艺路线-编辑
- Operation ID：`editUsingPOST_20`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcessRoute | body | 是 | tms_process_route对象0 | tmsProcessRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsProcessRoute/edit

- 名称：工艺路线-编辑
- Operation ID：`editUsingPUT_20`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsProcessRoute | body | 是 | tms_process_route对象0 | tmsProcessRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsProcessRoute/list

- 名称：工艺路线-分页列表查询
- Operation ID：`queryPageListUsingGET_20`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endTime | query | 否 | string | - |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| processRouteCode | query | 否 | string | 工艺路线编码 |
| processRouteName | query | 否 | string | 工艺路线名称 |
| startTime | query | 否 | string | - |
| status | query | 否 | integer(int32) | 状态：1启用， 2禁用 |
| tmsProcessRouteProcessList[0].createBy | query | 否 | string | 创建人 |
| tmsProcessRouteProcessList[0].createTime | query | 否 | string(date-time) | 创建时间 |
| tmsProcessRouteProcessList[0].id | query | 否 | string | id |
| tmsProcessRouteProcessList[0].outputUnit | query | 否 | string | 产出单位(米) |
| tmsProcessRouteProcessList[0].processCode | query | 否 | string | 工序编码 |
| tmsProcessRouteProcessList[0].processId | query | 否 | string | 工序id |
| tmsProcessRouteProcessList[0].processName | query | 否 | string | 工序名称 |
| tmsProcessRouteProcessList[0].processRouteId | query | 否 | string | 工艺路线id |
| tmsProcessRouteProcessList[0].processType | query | 否 | string | 工序分类名称 |
| tmsProcessRouteProcessList[0].productionUnit | query | 否 | string | 投产单位(米) |
| tmsProcessRouteProcessList[0].sort | query | 否 | integer(int32) | 排序：10 20 30 40... |
| tmsProcessRouteProcessList[0].updateBy | query | 否 | string | 修改人 |
| tmsProcessRouteProcessList[0].updateTime | query | 否 | string(date-time) | 修改时间 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_process_route对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsProcessRoute/queryById

- 名称：工艺路线-通过id查询
- Operation ID：`queryByIdUsingGET_20`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_process_route对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 管制区日志

#### POST /jeecg-tms/tmsServer/tmsControlAreaLog/add

- 名称：管制区日志-添加
- Operation ID：`addUsingPOST_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsControlAreaLog | body | 是 | tms_control_area_log对象 | tmsControlAreaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsControlAreaLog/delete

- 名称：管制区日志-通过id删除
- Operation ID：`deleteUsingDELETE_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsControlAreaLog/deleteBatch

- 名称：管制区日志-批量删除
- Operation ID：`deleteBatchUsingDELETE_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsControlAreaLog/edit

- 名称：管制区日志-编辑
- Operation ID：`editUsingPOST_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsControlAreaLog | body | 是 | tms_control_area_log对象 | tmsControlAreaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsControlAreaLog/edit

- 名称：管制区日志-编辑
- Operation ID：`editUsingPUT_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsControlAreaLog | body | 是 | tms_control_area_log对象 | tmsControlAreaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsControlAreaLog/list

- 名称：管制区日志-分页列表查询
- Operation ID：`queryPageListUsingGET_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| controlAreaId | query | 否 | string | 管制区ID |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| id | query | 否 | string | 主键 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| reqCode | query | 否 | string | 请求编码 |
| status | query | 否 | string | 状态：1 请求进入，2 已进入，3 已退出管制区 |
| sysOrgCode | query | 否 | string | 所属部门 |
| taskCode | query | 否 | string | 任务请求编码 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |
| vehicleId | query | 否 | string | 车辆ID |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_control_area_log对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsControlAreaLog/queryById

- 名称：管制区日志-通过id查询
- Operation ID：`queryByIdUsingGET_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_control_area_log对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 广播模板

#### POST /jeecg-tms/tmsServer/tmsBroadcastTemplate/add

- 名称：广播模板-添加
- Operation ID：`addUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastTemplate | body | 是 | tms_broadcast_template对象 | tmsBroadcastTemplate |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsBroadcastTemplate/delete

- 名称：广播模板-通过id删除
- Operation ID：`deleteUsingDELETE_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsBroadcastTemplate/deleteBatch

- 名称：广播模板-批量删除
- Operation ID：`deleteBatchUsingDELETE_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsBroadcastTemplate/edit

- 名称：广播模板-编辑
- Operation ID：`editUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastTemplate | body | 是 | tms_broadcast_template对象 | tmsBroadcastTemplate |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsBroadcastTemplate/edit

- 名称：广播模板-编辑
- Operation ID：`editUsingPUT_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastTemplate | body | 是 | tms_broadcast_template对象 | tmsBroadcastTemplate |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBroadcastTemplate/list

- 名称：广播模板-分页列表查询
- Operation ID：`queryPageListUsingGET_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 模板编码 |
| content | query | 否 | string | 模板内容 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| id | query | 否 | string | 主键 |
| name | query | 否 | string | 模板名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | query | 否 | string | 所属部门 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_broadcast_template对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBroadcastTemplate/queryById

- 名称：广播模板-通过id查询
- Operation ID：`queryByIdUsingGET_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_broadcast_template对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 广播语

#### POST /jeecg-tms/tmsServer/tmsBroadcastSpeech/add

- 名称：广播语-添加
- Operation ID：`addUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastSpeech | body | 是 | tms_broadcast_speech对象 | tmsBroadcastSpeech |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsBroadcastSpeech/delete

- 名称：广播语-通过id删除
- Operation ID：`deleteUsingDELETE_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsBroadcastSpeech/deleteBatch

- 名称：广播语-批量删除
- Operation ID：`deleteBatchUsingDELETE_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsBroadcastSpeech/edit

- 名称：广播语-编辑
- Operation ID：`editUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastSpeech | body | 是 | tms_broadcast_speech对象 | tmsBroadcastSpeech |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsBroadcastSpeech/edit

- 名称：广播语-编辑
- Operation ID：`editUsingPUT_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBroadcastSpeech | body | 是 | tms_broadcast_speech对象 | tmsBroadcastSpeech |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBroadcastSpeech/getNameById

- 名称：广播语-分页列表查询
- Operation ID：`getNameByIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_broadcast_speech对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBroadcastSpeech/list

- 名称：广播语-分页列表查询
- Operation ID：`queryPageListUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 广播语编码 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| id | query | 否 | string | 主键 |
| isStrategyFlag | query | 否 | string | - |
| name | query | 否 | string | 广播语名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | query | 否 | string | 所属部门 |
| templateId | query | 否 | string | 广播模板ID |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_broadcast_speech对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBroadcastSpeech/queryById

- 名称：广播语-通过id查询
- Operation ID：`queryByIdUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_broadcast_speech对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 规则管理

#### POST /jeecg-tms/tmsServer/tmsRule/add

- 名称：规则管理-添加
- Operation ID：`addUsingPOST_23`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRule | body | 是 | tms_rule对象 | tmsRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsRule/delete

- 名称：规则管理-通过id删除
- Operation ID：`deleteUsingDELETE_23`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |
| num | query | 否 | string | num |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsRule/deleteBatch

- 名称：规则管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_23`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsRule/edit

- 名称：规则管理-编辑
- Operation ID：`editUsingPOST_23`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRule | body | 是 | tms_rule对象 | tmsRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsRule/edit

- 名称：规则管理-编辑
- Operation ID：`editUsingPUT_23`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRule | body | 是 | tms_rule对象 | tmsRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRule/list

- 名称：规则管理-分页列表查询
- Operation ID：`queryPageListUsingGET_23`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| actionIds | query | 否 | string | 策略动作id(id,id,id) |
| algorithmPackageBottom | query | 否 | string | 算法包(下架规则)：1 先进先出  2先进后出 |
| algorithmPackageTop | query | 否 | string | 算法包(上架规则)：1 先进先出  2先进后出 |
| conditionalCombinationId | query | 否 | string | 关联条件组id |
| conditionGroupCode | query | 否 | string | - |
| conditions[0].columnId | query | 否 | integer(int32) | 列ID |
| conditions[0].columnName | query | 否 | string | 列名称 |
| conditions[0].conditionalCombinationId | query | 否 | string | 所属条件组 |
| conditions[0].conditionBaseOperator | query | 否 | string | 条件运算符(等于、加、减、乘、除、余数、IF、左括号、右括号、与、或、非、包含) |
| conditions[0].conditionGroupId | query | 否 | string | 所属条件分组id |
| conditions[0].conditionKey | query | 否 | string | 条件key：(表名,字段, |
| conditions[0].conditionLogicalOperator | query | 否 | string | 与、或 |
| conditions[0].conditionValue | query | 否 | string | 条件值 |
| conditions[0].createBy | query | 否 | string | 创建人 |
| conditions[0].createTime | query | 否 | string(date-time) | 创建时间 |
| conditions[0].id | query | 否 | string | id |
| conditions[0].isQueryDatabase | query | 否 | string | 是否查询数据库：1 是，2 否 |
| conditions[0].moduleId | query | 否 | integer(int32) | 模块ID |
| conditions[0].queryDemand | query | 否 | string | 是否根据需求查询匹配条件：1是，2否 |
| conditions[0].sort | query | 否 | integer(int32) | 排序，或相关时起作用，判断条件优先级 |
| conditions[0].updateBy | query | 否 | string | 修改人 |
| conditions[0].updateTime | query | 否 | string(date-time) | 修改时间 |
| containerInitialize | query | 否 | string | 容器初始化 |
| containerStatus | query | 否 | string | 容器状态 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| customizedResults | query | 否 | string | 定制化结果id(id,id,id) |
| flowCardFlag | query | 否 | string | 流程卡标识新增（id,id,id |
| flowCardFlagCode | query | 否 | string | - |
| goodType | query | 否 | string | - |
| id | query | 否 | string | id |
| isReleaseContainer | query | 否 | string | 是否释放容器：1 是，2 否 |
| isTimeout | query | 否 | integer(int32) | 是否开启超时 1 是，2 否 |
| logicalAreaList[0].index | query | 否 | integer(int32) | - |
| logicalAreaList[0].label | query | 否 | string | - |
| logicalAreaList[0].logicalAreaId | query | 否 | string | - |
| logicalAreaNames | query | 否 | string | - |
| logicAreaCode | query | 否 | string | - |
| logicAreaId | query | 否 | string | 逻辑区id |
| logicAreaName | query | 否 | string | - |
| logicLocationStatus | query | 否 | string | 目标储位状态 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pattern | query | 否 | string | 模式：1 上料，2 下料 |
| priority | query | 否 | integer(int32) | 优先级 |
| ruleCode | query | 否 | string | 规则编码 |
| ruleName | query | 否 | string | 规则名称 |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleGroupId | query | 否 | string | 车辆分组id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_rule对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRule/queryById

- 名称：规则管理-通过id查询
- Operation ID：`queryByIdUsingGET_23`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_rule对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 规则上下架配置

#### POST /jeecg-tms/tmsServer/tmsRuleDict/add

- 名称：规则上下架配置-添加
- Operation ID：`addUsingPOST_24`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRuleDict | body | 是 | tms_rule_dict对象 | tmsRuleDict |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsRuleDict/delete

- 名称：规则上下架配置-通过id删除
- Operation ID：`deleteUsingDELETE_24`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsRuleDict/deleteBatch

- 名称：规则上下架配置-批量删除
- Operation ID：`deleteBatchUsingDELETE_24`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsRuleDict/edit

- 名称：规则上下架配置-编辑
- Operation ID：`editUsingPOST_24`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRuleDict | body | 是 | tms_rule_dict对象 | tmsRuleDict |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsRuleDict/edit

- 名称：规则上下架配置-编辑
- Operation ID：`editUsingPUT_24`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRuleDict | body | 是 | tms_rule_dict对象 | tmsRuleDict |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRuleDict/list

- 名称：规则上下架配置-分页列表查询
- Operation ID：`queryPageListUsingGET_24`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 规则编码 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| isOldRule | query | 否 | integer(int32) | 是否是老规则 1是 2 否 |
| isShow | query | 否 | string | 显示：1 显示，2 不显示 |
| name | query | 否 | string | 规则名称 |
| oldValue | query | 否 | string | 对应的，1，2，3，老版本兼容字段，新的不用 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| remark | query | 否 | string | 描述 |
| ruleConfig | query | 否 | string | 规则配置 |
| status | query | 否 | integer(int32) | 状态：1 启用，2 禁用 |
| type | query | 否 | string | 类型：1 上架，2 下架 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_rule_dict对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRuleDict/queryById

- 名称：规则上下架配置-通过id查询
- Operation ID：`queryByIdUsingGET_24`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_rule_dict对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 货型管理

#### POST /jeecg-tms/tmsServer/tmsGoodsType/add

- 名称：货型管理-添加
- Operation ID：`addUsingPOST_14`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsGoodsType | body | 是 | tms_goods_type对象 | tmsGoodsType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsGoodsType/delete

- 名称：货型管理-通过id删除
- Operation ID：`deleteUsingDELETE_14`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsGoodsType/deleteBatch

- 名称：货型管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_14`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsGoodsType/edit

- 名称：货型管理-编辑
- Operation ID：`editUsingPOST_14`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsGoodsType | body | 是 | tms_goods_type对象 | tmsGoodsType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsGoodsType/edit

- 名称：货型管理-编辑
- Operation ID：`editUsingPUT_14`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsGoodsType | body | 是 | tms_goods_type对象 | tmsGoodsType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsGoodsType/list

- 名称：货型管理-分页列表查询
- Operation ID：`queryPageListUsingGET_14`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| direction | query | 否 | string | 方向 |
| goodsHeight | query | 否 | string | 高 |
| goodsLength | query | 否 | string | 长 |
| goodsTypeCode | query | 否 | string | 货型编号 |
| goodsTypeName | query | 否 | string | 货型名称 |
| goodsWidth | query | 否 | string | 宽 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_goods_type对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsGoodsType/queryById

- 名称：货型管理-通过id查询
- Operation ID：`queryByIdUsingGET_14`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_goods_type对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 监控资源日志

#### POST /jeecg-tms/tmsServer/tmsMonitoringSourceLog/add

- 名称：监控资源日志-添加
- Operation ID：`addUsingPOST_16`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsMonitoringSourceLog | body | 是 | tms_monitoring_source_log对象 | tmsMonitoringSourceLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsMonitoringSourceLog/delete

- 名称：监控资源日志-通过id删除
- Operation ID：`deleteUsingDELETE_16`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsMonitoringSourceLog/deleteBatch

- 名称：监控资源日志-批量删除
- Operation ID：`deleteBatchUsingDELETE_16`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsMonitoringSourceLog/edit

- 名称：监控资源日志-编辑
- Operation ID：`editUsingPOST_16`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsMonitoringSourceLog | body | 是 | tms_monitoring_source_log对象 | tmsMonitoringSourceLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsMonitoringSourceLog/edit

- 名称：监控资源日志-编辑
- Operation ID：`editUsingPUT_16`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsMonitoringSourceLog | body | 是 | tms_monitoring_source_log对象 | tmsMonitoringSourceLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsMonitoringSourceLog/list

- 名称：监控资源日志-分页列表查询
- Operation ID：`queryPageListUsingGET_16`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| discoveryTime | query | 否 | string(date-time) | 发现时间 |
| id | query | 否 | string | id |
| monitoringId | query | 否 | string | 资源监控日志ID |
| newData | query | 否 | string | 监控到状态 |
| oldData | query | 否 | string | 监控前状态 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| resourceCode | query | 否 | string | 被监控的资源编码 |
| resourceId | query | 否 | string | 被监控的资源ID |
| resourceSource | query | 否 | string | 资源来源名称 |
| resourceType | query | 否 | string | 资源类型：储位，容器，车辆 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_monitoring_source_log对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsMonitoringSourceLog/queryById

- 名称：监控资源日志-通过id查询
- Operation ID：`queryByIdUsingGET_16`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_monitoring_source_log对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 流程卡管理

#### GET /jeecg-tms/tmsServer/tmsConditionTable/list

- 名称：查询所有可以作为条件的表
- Operation ID：`queryTableListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_condition_table对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionTableColumn/list

- 名称：查询所有可以作为条件的表
- Operation ID：`queryTableColumnListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| table | query | 否 | string | table |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_condition_table_column对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionTableColumn/listByTableId

- 名称：查询所有指定条件的表
- Operation ID：`listByTableIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| columnName | query | 否 | string | columnName |
| conditionTableId | query | 否 | string | conditionTableId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_condition_table_column对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionTableColumn/tableColumnById

- 名称：通过id查询唯一的列查询
- Operation ID：`queryTableColumnByIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 否 | integer(int32) | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_condition_table_column对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionTableColumn/tableColumnByName

- 名称：通过id查询唯一的列查询
- Operation ID：`queryTableColumnByNameUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| queryDemand | query | 否 | string | queryDemand |
| tableColumnName | query | 否 | string | tableColumnName |
| tableId | query | 否 | string | tableId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_condition_table_column对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms/tmsServer/tmsFlowCard/add

- 名称：流程卡管理-添加
- Operation ID：`addUsingPOST_13`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFlowCard | body | 是 | tms_flow_card对象 | tmsFlowCard |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms/tmsServer/tmsFlowCard/batchUpdateFlag

- 名称：流程卡管理-批量编辑标识
- Operation ID：`batchUpdateFlagUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| batchUpdateFlag | body | 是 | BatchUpdateFlag | batchUpdateFlag |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms/tmsServer/tmsFlowCard/checkFlowCard

- 名称：流程卡管理-批量编辑校验
- Operation ID：`checkFlowCardUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFlowCard | body | 是 | tms_flow_card对象11 | tmsFlowCard |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsFlowCard/delete

- 名称：流程卡管理-通过id删除
- Operation ID：`deleteUsingDELETE_13`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsFlowCard/deleteBatch

- 名称：流程卡管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_13`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsFlowCard/edit

- 名称：流程卡管理-编辑
- Operation ID：`editUsingPOST_13`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFlowCard | body | 是 | tms_flow_card对象 | tmsFlowCard |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsFlowCard/edit

- 名称：流程卡管理-编辑
- Operation ID：`editUsingPUT_13`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFlowCard | body | 是 | tms_flow_card对象 | tmsFlowCard |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsFlowCard/list

- 名称：流程卡管理-分页列表查询
- Operation ID：`queryPageListUsingGET_13`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| containerCode | query | 否 | string | - |
| containerId | query | 否 | string | 容器id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| flagCodes | query | 否 | string | - |
| flagEight | query | 否 | string | 标识8 |
| flagEleven | query | 否 | string | 标识11 |
| flagFive | query | 否 | string | 标识5 |
| flagFour | query | 否 | string | 标识4 |
| flagNine | query | 否 | string | 标识9 |
| flagOne | query | 否 | string | 标识1 |
| flagOneCode | query | 否 | string | - |
| flagSeven | query | 否 | string | 标识7 |
| flagSix | query | 否 | string | 标识6 |
| flagTen | query | 否 | string | 标识10 |
| flagThree | query | 否 | string | 标识3 |
| flagThreeCode | query | 否 | string | - |
| flagTips | query | 否 | string | - |
| flagTwelve | query | 否 | string | 标识12 |
| flagTwo | query | 否 | string | 标识2 |
| flagTwoCode | query | 否 | string | - |
| flowCardBusinessId | query | 否 | string | - |
| flowCardNumber | query | 否 | string | 流程卡号 |
| id | query | 否 | string | id |
| ids | query | 否 | array<string> | - |
| materialCode | query | 否 | string | 物料编码 |
| materialName | query | 否 | string | 物料名称 |
| materialNumber | query | 否 | number | 物料数量 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| serialNumber | query | 否 | integer(int32) | 顺序号 |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| workOrderId | query | 否 | string | 工单id |
| workOrderNumber | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_flow_card对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsFlowCard/queryById

- 名称：流程卡管理-通过id查询
- Operation ID：`queryByIdUsingGET_13`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_flow_card对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 路由管理

#### POST /jeecg-tms/tmsServer/tmsRouter/add

- 名称：路由管理-添加
- Operation ID：`addUsingPOST_22`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRouter | body | 是 | tms_router对象1 | tmsRouter |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsRouter/delete

- 名称：路由管理-通过id删除
- Operation ID：`deleteUsingDELETE_22`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsRouter/deleteBatch

- 名称：路由管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_22`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsRouter/edit

- 名称：路由管理-编辑
- Operation ID：`editUsingPOST_22`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRouter | body | 是 | tms_router对象1 | tmsRouter |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsRouter/edit

- 名称：路由管理-编辑
- Operation ID：`editUsingPUT_22`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsRouter | body | 是 | tms_router对象1 | tmsRouter |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRouter/list

- 名称：路由管理-分页列表查询
- Operation ID：`queryPageListUsingGET_22`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endStorageLocationCode | query | 否 | string | 终点库位 |
| endStorageLocationCodes | query | 否 | string | - |
| endStorageLocationId | query | 否 | string | 终点库位id |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| routerCode | query | 否 | string | 路由编号 |
| routerWeight | query | 否 | integer(int32) | 路由权数 |
| startStorageLocationCode | query | 否 | string | 起点库位 |
| startStorageLocationCodes | query | 否 | string | - |
| startStorageLocationId | query | 否 | string | 起点库位id |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| taskTypeRouteId | query | 否 | string | 任务类型路由ID |
| taskTypeRouteName | query | 否 | string | 任务类型名称 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_router对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsRouter/queryById

- 名称：路由管理-通过id查询
- Operation ID：`queryByIdUsingGET_22`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_router对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 逻辑区标签

#### POST /jeecg-tms/tmsServer/tmsLogicalAreaTag/add

- 名称：逻辑区标签-添加
- Operation ID：`addUsingPOST_15`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsLogicalAreaTag | body | 是 | tms_logical_area_tag对象 | tmsLogicalAreaTag |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsLogicalAreaTag/delete

- 名称：逻辑区标签-通过id删除
- Operation ID：`deleteUsingDELETE_15`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsLogicalAreaTag/deleteBatch

- 名称：逻辑区标签-批量删除
- Operation ID：`deleteBatchUsingDELETE_15`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsLogicalAreaTag/edit

- 名称：逻辑区标签-编辑
- Operation ID：`editUsingPOST_15`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsLogicalAreaTag | body | 是 | tms_logical_area_tag对象 | tmsLogicalAreaTag |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsLogicalAreaTag/edit

- 名称：逻辑区标签-编辑
- Operation ID：`editUsingPUT_15`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsLogicalAreaTag | body | 是 | tms_logical_area_tag对象 | tmsLogicalAreaTag |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsLogicalAreaTag/list

- 名称：逻辑区标签-分页列表查询
- Operation ID：`queryPageListUsingGET_15`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：0 禁用，1 启用 |
| tagCode | query | 否 | string | 逻辑区标签编码 |
| tagName | query | 否 | string | 逻辑区标签名称 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_logical_area_tag对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsLogicalAreaTag/queryById

- 名称：逻辑区标签-通过id查询
- Operation ID：`queryByIdUsingGET_15`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_logical_area_tag对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 逻辑区管理

#### POST /jeecg-tms/tmsServer/tmsTaskTypeRange/add

- 名称：逻辑区管理-添加
- Operation ID：`addUsingPOST_35`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFinalTaskTypeRange | body | 是 | tms_task_type_range对象1 | tmsFinalTaskTypeRange |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskTypeRange/delete

- 名称：逻辑区管理-通过id删除
- Operation ID：`deleteUsingDELETE_35`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskTypeRange/deleteBatch

- 名称：逻辑区管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_35`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskTypeRange/edit

- 名称：逻辑区管理-编辑
- Operation ID：`editUsingPOST_35`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFinalTaskTypeRange | body | 是 | tms_task_type_range对象1 | tmsFinalTaskTypeRange |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskTypeRange/edit

- 名称：逻辑区管理-编辑
- Operation ID：`editUsingPUT_35`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsFinalTaskTypeRange | body | 是 | tms_task_type_range对象1 | tmsFinalTaskTypeRange |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskTypeRange/list

- 名称：逻辑区管理-分页列表查询
- Operation ID：`queryPageListUsingGET_37`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| logicalAreaTagIds | query | 否 | string | 逻辑区标签ID组 |
| logicalAreaTagNames | query | 否 | string | 逻辑区标签名称组 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| rangeCode | query | 否 | string | 范围编码 |
| rangeName | query | 否 | string | 范围名称 |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationCode | query | 否 | string | 逻辑包含库位编码组 |
| storageLocationCodes | query | 否 | string | 逻辑包含库位编码组 |
| storageLocationIds | query | 否 | string | 逻辑包含库位ID组 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| userIds | query | 否 | string | 用户Ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_type_range对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskTypeRange/queryById

- 名称：逻辑区管理-通过id查询
- Operation ID：`queryByIdUsingGET_35`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_type_range对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 门

#### POST /jeecg-tms/tmsServer/tmsDoor/add

- 名称：门-添加
- Operation ID：`addUsingPOST_12`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDoor | body | 是 | tms_door对象 | tmsDoor |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsDoor/delete

- 名称：门-通过id删除
- Operation ID：`deleteUsingDELETE_12`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsDoor/deleteBatch

- 名称：门-批量删除
- Operation ID：`deleteBatchUsingDELETE_12`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsDoor/edit

- 名称：门-编辑
- Operation ID：`editUsingPOST_12`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDoor | body | 是 | tms_door对象 | tmsDoor |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsDoor/edit

- 名称：门-编辑
- Operation ID：`editUsingPUT_12`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDoor | body | 是 | tms_door对象 | tmsDoor |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDoor/list

- 名称：门-分页列表查询
- Operation ID：`queryPageListUsingGET_12`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| closeStatusOffset | query | 否 | integer(int32) | 关状态反馈点 |
| closeWriteOffset | query | 否 | integer(int32) | 关状态写入点 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建人 |
| doorName | query | 否 | string | 门名称 |
| id | query | 否 | string | id |
| ip | query | 否 | string | modbus ip |
| openStatusOffset | query | 否 | integer(int32) | 开状态反馈点 |
| openWriteOffset | query | 否 | integer(int32) | 开状态写入点 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| port | query | 否 | integer(int32) | modbus 端口 |
| slaveId | query | 否 | integer(int32) | modbus 从设备ID |
| sysOrgCode | query | 否 | string | 所属部门 |
| tier | query | 否 | integer(int32) | 门所在层 |
| type | query | 否 | string | 1电梯2卷帘门3输送线 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_door对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDoor/queryById

- 名称：门-通过id查询
- Operation ID：`queryByIdUsingGET_12`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_door对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 任务类型

#### POST /jeecg-tms/tmsServer/tmsTaskTypeRoute/add

- 名称：任务类型-添加
- Operation ID：`addUsingPOST_36`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskTypeRoute | body | 是 | tms_task_type_route对象 | tmsTaskTypeRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskTypeRoute/delete

- 名称：任务类型-通过id删除
- Operation ID：`deleteUsingDELETE_36`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskTypeRoute/deleteBatch

- 名称：任务类型-批量删除
- Operation ID：`deleteBatchUsingDELETE_36`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskTypeRoute/edit

- 名称：任务类型-编辑
- Operation ID：`editUsingPOST_36`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskTypeRoute | body | 是 | tms_task_type_route对象 | tmsTaskTypeRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskTypeRoute/edit

- 名称：任务类型-编辑
- Operation ID：`editUsingPUT_36`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskTypeRoute | body | 是 | tms_task_type_route对象 | tmsTaskTypeRoute |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskTypeRoute/list

- 名称：任务类型-分页列表查询
- Operation ID：`queryPageListUsingGET_38`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| name | query | 否 | string | 名称由电梯+路由组成 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| type | query | 否 | string | 类型 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_type_route对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskTypeRoute/queryById

- 名称：任务类型-通过id查询
- Operation ID：`queryByIdUsingGET_36`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_type_route对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 任务类型管理

#### POST /jeecg-tms/tmsServer/tmsTaskType/add

- 名称：任务类型管理-添加
- Operation ID：`addUsingPOST_34`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskType | body | 是 | tms_task_type对象1 | tmsTaskType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskType/delete

- 名称：任务类型管理-通过id删除
- Operation ID：`deleteUsingDELETE_34`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskType/deleteBatch

- 名称：任务类型管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_34`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskType/edit

- 名称：任务类型管理-编辑
- Operation ID：`editUsingPOST_34`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskType | body | 是 | tms_task_type对象1 | tmsTaskType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskType/edit

- 名称：任务类型管理-编辑
- Operation ID：`editUsingPUT_34`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskType | body | 是 | tms_task_type对象1 | tmsTaskType |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskType/list

- 名称：任务类型管理-分页列表查询
- Operation ID：`queryPageListUsingGET_36`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| currentStorageLocationCodes | query | 否 | string | - |
| id | query | 否 | string | id |
| isOpenTime | query | 否 | string | - |
| isOpenTiming | query | 否 | string | 是否开启定时 |
| isReleaseContainer | query | 否 | string | 是否释放容器：1 释放，2 不释放 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| priority | query | 否 | integer(int32) | 优先级 |
| rangeCode | query | 否 | string | - |
| rangeId | query | 否 | string | 范围ID |
| rangeName | query | 否 | string | - |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationIds | query | 否 | string | 所触发的库位ID组 |
| taskTypeCode | query | 否 | string | 任务类型编码 |
| taskTypeName | query | 否 | string | 任务类型名称 |
| taskTypePattern | query | 否 | string | 任务类型模式：1 呼料，2 叫料 |
| timeOutPeriod | query | 否 | integer(int32) | 超时时间,秒 |
| triggeringCondition | query | 否 | string | 触发条件(json) |
| triggeringCondition1.containerStatus | query | 否 | string | - |
| triggeringCondition1.ec | query | 否 | string | - |
| triggeringCondition1.endLocationStatus | query | 否 | string | - |
| triggeringCondition1.se | query | 否 | string | - |
| triggeringCondition1.startLocationStatus | query | 否 | string | - |
| triggeringSwitch | query | 否 | string | 触发开关(json) |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleScope | query | 否 | string | 车辆可选范围 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_type对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskType/queryById

- 名称：任务类型管理-通过id查询
- Operation ID：`queryByIdUsingGET_34`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_type对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 容器管理

#### POST /jeecg-tms/tmsServer/tmsContainer/add

- 名称：容器管理-添加
- Operation ID：`addUsingPOST_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsContainer | body | 是 | tms_container对象 | tmsContainer |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsContainer/delete

- 名称：容器管理-通过id删除
- Operation ID：`deleteUsingDELETE_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsContainer/deleteBatch

- 名称：容器管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsContainer/edit

- 名称：容器管理-编辑
- Operation ID：`editUsingPOST_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsContainer | body | 是 | tms_container对象 | tmsContainer |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsContainer/edit

- 名称：容器管理-编辑
- Operation ID：`editUsingPUT_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsContainer | body | 是 | tms_container对象 | tmsContainer |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsContainer/list

- 名称：容器管理-分页列表查询
- Operation ID：`queryPageListUsingGET_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessStatus | query | 否 | string | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| containerCode | query | 否 | string | 容器编码 |
| containerGood | query | 否 | string | 容器商品 |
| containerQuantity | query | 否 | integer(int32) | 容器数量 |
| containerStatus | query | 否 | string | 容器状态：0 空，1 满，2 满+1 |
| containerWeight | query | 否 | string | 容器重量 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| deleted | query | 否 | integer(int32) | - |
| flowCardCode | query | 否 | string | - |
| flowCardCodes | query | 否 | string | - |
| goodsTypeCode | query | 否 | string | - |
| goodsTypeId | query | 否 | string | 货型id |
| id | query | 否 | string | id |
| orderFlag | query | 否 | string | 工单标 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| processFlag | query | 否 | string | 工序标：0 镭射过油，1 丝印，2 翻纸工序，3 打包工序，4 首件签样，5 复合工序，6 单凹工序，7 切纸工序，8 模切工序，9 机检工序， 10 烫金工序，11 凹印工序，12 胶印工序，13 模切工序，14 打包工序 |
| storageLocationCode | query | 否 | string | - |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_container对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsContainer/queryById

- 名称：容器管理-通过id查询
- Operation ID：`queryByIdUsingGET_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_container对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 容器任务

#### POST /jeecg-tms/tmsServer/tmsTaskPoll/add

- 名称：容器任务-添加
- Operation ID：`addUsingPOST_33`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskPoll | body | 是 | tms_task_poll对象1 | tmsTaskPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms/tmsServer/tmsTaskPoll/cancel/{id}

- 名称：容器任务-取消
- Operation ID：`cancelUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | path | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskPoll/cancel/{id}

- 名称：容器任务-取消
- Operation ID：`cancelUsingPUT`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | path | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskPoll/delete

- 名称：容器任务-通过id删除
- Operation ID：`deleteUsingDELETE_33`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskPoll/deleteBatch

- 名称：容器任务-批量删除
- Operation ID：`deleteBatchUsingDELETE_33`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskPoll/edit

- 名称：容器任务-编辑
- Operation ID：`editUsingPOST_33`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskPoll | body | 是 | tms_task_poll对象1 | tmsTaskPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskPoll/edit

- 名称：容器任务-编辑
- Operation ID：`editUsingPUT_33`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskPoll | body | 是 | tms_task_poll对象1 | tmsTaskPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskPoll/list

- 名称：容器任务-分页列表查询
- Operation ID：`queryPageListUsingGET_34`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessConfigId | query | 否 | string | 业务配置ID |
| buttonCode | query | 否 | string | 按钮编码 |
| conditionalCombinationCode | query | 否 | string | - |
| conditionalCombinationId | query | 否 | string | 条件组id |
| containerCode | query | 否 | string | - |
| containerId | query | 否 | string | 容器id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| dispatch | query | 否 | string | 是否调度：1 未调度，2已调度 |
| endCavernCode | query | 否 | string | - |
| endCavernName | query | 否 | string | - |
| endLocationCode | query | 否 | string | - |
| endLocationId | query | 否 | string | 目标点位id |
| endLocationName | query | 否 | string | - |
| goodType | query | 否 | string | 货型 |
| groupStatus | query | 否 | string | 任务组状态：10 创建，20 进行中，50 完成，60 取消，80 终止 |
| id | query | 否 | string | id |
| isException | query | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | query | 否 | string(date-time) | 任务下发时间 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pidCode | query | 否 | string | 任务父编号 |
| ruleCode | query | 否 | string | - |
| ruleId | query | 否 | string | 规则ID |
| ruleName | query | 否 | string | - |
| startCavernCode | query | 否 | string | - |
| startCavernName | query | 否 | string | - |
| startLocationCode | query | 否 | string | - |
| startLocationId | query | 否 | string | 起始点位id |
| startLocationName | query | 否 | string | - |
| status | query | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskCode | query | 否 | string | 任务编号 |
| taskMode | query | 否 | string | - |
| taskOverTime | query | 否 | string(date-time) | 任务完成时间 |
| taskPriority | query | 否 | string | 优先级 |
| taskSource | query | 否 | string | 任务来源 |
| taskType | query | 否 | string | 任务类型 |
| taskTypeId | query | 否 | string | 任务类型id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_poll对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskPoll/poolList

- 名称：容器任务-分页列表查询
- Operation ID：`queryPoolPageListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessConfigId | query | 否 | string | 业务配置ID |
| buttonCode | query | 否 | string | 按钮编码 |
| conditionalCombinationCode | query | 否 | string | - |
| conditionalCombinationId | query | 否 | string | 条件组id |
| containerCode | query | 否 | string | - |
| containerId | query | 否 | string | 容器id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| dispatch | query | 否 | string | 是否调度：1 未调度，2已调度 |
| endCavernCode | query | 否 | string | - |
| endCavernName | query | 否 | string | - |
| endLocationCode | query | 否 | string | - |
| endLocationId | query | 否 | string | 目标点位id |
| endLocationName | query | 否 | string | - |
| goodType | query | 否 | string | 货型 |
| groupStatus | query | 否 | string | 任务组状态：10 创建，20 进行中，50 完成，60 取消，80 终止 |
| id | query | 否 | string | id |
| isException | query | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | query | 否 | string(date-time) | 任务下发时间 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pidCode | query | 否 | string | 任务父编号 |
| ruleCode | query | 否 | string | - |
| ruleId | query | 否 | string | 规则ID |
| ruleName | query | 否 | string | - |
| startCavernCode | query | 否 | string | - |
| startCavernName | query | 否 | string | - |
| startLocationCode | query | 否 | string | - |
| startLocationId | query | 否 | string | 起始点位id |
| startLocationName | query | 否 | string | - |
| status | query | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskCode | query | 否 | string | 任务编号 |
| taskMode | query | 否 | string | - |
| taskOverTime | query | 否 | string(date-time) | 任务完成时间 |
| taskPriority | query | 否 | string | 优先级 |
| taskSource | query | 否 | string | 任务来源 |
| taskType | query | 否 | string | 任务类型 |
| taskTypeId | query | 否 | string | 任务类型id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_poll对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskPoll/queryById

- 名称：容器任务-通过id查询
- Operation ID：`queryByIdUsingGET_33`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_poll对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 容器任务时间记录

#### GET /jeecg-tms/tmsServer/tmsTaskPollStatus/list

- 名称：容器任务时间记录-分页列表查询
- Operation ID：`queryPageListUsingGET_35`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| status | query | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskPollId | query | 否 | string | TMS任务id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_task_poll_status对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 设备储位绑定

#### POST /jeecg-tms/tmsServer/tmsStorageLocationButton/add

- 名称：设备储位绑定-添加
- Operation ID：`addUsingPOST_28`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocationButton | body | 是 | tms_storage_location_button对象 | tmsStorageLocationButton |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsStorageLocationButton/delete

- 名称：设备储位绑定-通过id删除
- Operation ID：`deleteUsingDELETE_28`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsStorageLocationButton/deleteBatch

- 名称：设备储位绑定-批量删除
- Operation ID：`deleteBatchUsingDELETE_28`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsStorageLocationButton/edit

- 名称：设备储位绑定-编辑
- Operation ID：`editUsingPOST_28`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocationButton | body | 是 | tms_storage_location_button对象 | tmsStorageLocationButton |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsStorageLocationButton/edit

- 名称：设备储位绑定-编辑
- Operation ID：`editUsingPUT_28`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsStorageLocationButton | body | 是 | tms_storage_location_button对象 | tmsStorageLocationButton |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageLocationButton/list

- 名称：设备储位绑定-分页列表查询
- Operation ID：`queryPageListUsingGET_29`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| beeperIp | query | 否 | string | 按钮IP |
| buttonCode | query | 否 | string | 按钮编码 |
| buttonType | query | 否 | string | 按钮类型 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| materAreaCode | query | 否 | string | 区域编号 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| storageLocationId | query | 否 | string | 库位id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_storage_location_button对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsStorageLocationButton/queryById

- 名称：设备储位绑定-通过id查询
- Operation ID：`queryByIdUsingGET_28`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_storage_location_button对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 深度组

#### POST /jeecg-tms/tmsServer/tmsDepthGroup/add

- 名称：深度组-添加
- Operation ID：`addUsingPOST_11`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDepthGroup | body | 是 | tms_depth_group对象1 | tmsDepthGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsDepthGroup/delete

- 名称：深度组-通过id删除
- Operation ID：`deleteUsingDELETE_11`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsDepthGroup/deleteBatch

- 名称：深度组-批量删除
- Operation ID：`deleteBatchUsingDELETE_11`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsDepthGroup/edit

- 名称：深度组-编辑
- Operation ID：`editUsingPOST_11`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDepthGroup | body | 是 | tms_depth_group对象 | tmsDepthGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsDepthGroup/edit

- 名称：深度组-编辑
- Operation ID：`editUsingPUT_11`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDepthGroup | body | 是 | tms_depth_group对象 | tmsDepthGroup |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDepthGroup/generateQrCode

- 名称：深度组-生成二维码
- Operation ID：`generateQrCodeUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDepthGroup/getLocListByDepthCode/{depthGroupCode}

- 名称：深度储位数据查询
- Operation ID：`getLocListByDepthCodeUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| depthGroupCode | path | 是 | string | depthGroupCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«DepthGroupLocation»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDepthGroup/list

- 名称：深度组-分页列表查询
- Operation ID：`queryPageListUsingGET_11`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessId | query | 否 | string | - |
| caBusinessId | query | 否 | string | - |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| depthGroupCode | query | 否 | string | 深度组编码 |
| depthOne | query | 否 | integer(int32) | 深度1，默认左 |
| depthTwo | query | 否 | integer(int32) | - |
| direction | query | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flagFive | query | 否 | string | - |
| flagFour | query | 否 | string | - |
| flagOne | query | 否 | string | - |
| flagThree | query | 否 | string | - |
| flagTwo | query | 否 | string | - |
| freeFlag | query | 否 | integer(int32) | - |
| groupByZ | query | 否 | string | - |
| hitTheShelfFlag | query | 否 | integer(int32) | - |
| hitTheShelfOrder | query | 否 | integer(int32) | 上架顺序 |
| id | query | 否 | string | id |
| orderByZ | query | 否 | string | - |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| qrCode | query | 否 | string | - |
| qrCodeStatus | query | 否 | integer(int32) | - |
| singleOrDouble | query | 否 | string | 单双向：1 单，2 双 |
| soldOutFlag | query | 否 | integer(int32) | - |
| soldOutOrder | query | 否 | integer(int32) | 下架顺序 |
| storageCavernCode | query | 否 | string | - |
| storageCavernId | query | 否 | string | - |
| storageCavernName | query | 否 | string | - |
| storageLocationCode | query | 否 | string | - |
| storageLocationId | query | 否 | string | - |
| storageLocationStatus | query | 否 | string | - |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| warehouseCode | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_depth_group对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDepthGroup/queryById

- 名称：深度组-通过id查询
- Operation ID：`queryByIdUsingGET_11`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_depth_group对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 条件管理

#### POST /jeecg-tms/tmsServer/tmsCondition/add

- 名称：条件管理-添加
- Operation ID：`addUsingPOST_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsCondition | body | 是 | tms_condition对象 | tmsCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsCondition/delete

- 名称：条件管理-通过id删除
- Operation ID：`deleteUsingDELETE_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsCondition/deleteBatch

- 名称：条件管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsCondition/edit

- 名称：条件管理-编辑
- Operation ID：`editUsingPOST_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsCondition | body | 是 | tms_condition对象 | tmsCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsCondition/edit

- 名称：条件管理-编辑
- Operation ID：`editUsingPUT_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsCondition | body | 是 | tms_condition对象 | tmsCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsCondition/list

- 名称：条件管理-分页列表查询
- Operation ID：`queryPageListUsingGET_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| conditionalCombinationId | query | 否 | string | 所属条件组 |
| conditionBaseOperator | query | 否 | string | 条件运算符(等于、加、减、乘、除、余数、IF、左括号、右括号、与、或、非、包含) |
| conditionGroupId | query | 否 | string | 所属条件分组id |
| conditionKey | query | 否 | string | 条件key：(表名,字段, |
| conditionLogicalOperator | query | 否 | string | 与、或 |
| conditionValue | query | 否 | string | 条件值 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| isQueryDatabase | query | 否 | string | 是否查询数据库：1 是，2 否 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| queryDemand | query | 否 | string | 是否根据需求查询匹配条件：1是，2否 |
| sort | query | 否 | integer(int32) | 排序，或相关时起作用，判断条件优先级 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_condition对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsCondition/queryById

- 名称：条件管理-通过id查询
- Operation ID：`queryByIdUsingGET_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_condition对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 条件组管理

#### POST /jeecg-tms/tmsServer/tmsConditionalCombination/add

- 名称：条件组管理-添加
- Operation ID：`addUsingPOST_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConditionalCombination | body | 是 | tms_conditional_combination对象1Req | tmsConditionalCombination |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsConditionalCombination/delete

- 名称：条件组管理-通过id删除
- Operation ID：`deleteUsingDELETE_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |
| num | query | 否 | string | num |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsConditionalCombination/deleteBatch

- 名称：条件组管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsConditionalCombination/edit

- 名称：条件组管理-编辑
- Operation ID：`editUsingPOST_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConditionalCombination | body | 是 | tms_conditional_combination对象1Req | tmsConditionalCombination |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsConditionalCombination/edit

- 名称：条件组管理-编辑
- Operation ID：`editUsingPUT_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConditionalCombination | body | 是 | tms_conditional_combination对象1Req | tmsConditionalCombination |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionalCombination/list

- 名称：条件组管理-分页列表查询
- Operation ID：`queryPageListUsingGET_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 条件组编码 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| name | query | 否 | string | 条件组名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_conditional_combination对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConditionalCombination/queryById

- 名称：条件组管理-通过id查询
- Operation ID：`queryByIdUsingGET_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_conditional_combination对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 系统开关

#### GET /jeecg-tms/tmsCase/closeFQ

- 名称：关闭分切送空
- Operation ID：`closeFQUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsCase/closeTaskPoll

- 名称：关闭任务池
- Operation ID：`closeTaskPollUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsCase/closeTimeOut

- 名称：关闭超时
- Operation ID：`closeTimeOutUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsCase/openFQ

- 名称：开启分切送空
- Operation ID：`openFQUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsCase/openTaskPoll

- 名称：开启任务池
- Operation ID：`openTaskPollUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsCase/openTimeOut

- 名称：开启超时
- Operation ID：`openTimeOutUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 系统配置

#### POST /jeecg-tms/tmsServer/tmsConfig/add

- 名称：系统配置-添加
- Operation ID：`addUsingPOST_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConfig | body | 是 | tms_config对象 | tmsConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsConfig/delete

- 名称：系统配置-通过id删除
- Operation ID：`deleteUsingDELETE_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsConfig/deleteBatch

- 名称：系统配置-批量删除
- Operation ID：`deleteBatchUsingDELETE_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsConfig/edit

- 名称：系统配置-编辑
- Operation ID：`editUsingPOST_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConfig | body | 是 | tms_config对象 | tmsConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsConfig/edit

- 名称：系统配置-编辑
- Operation ID：`editUsingPUT_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsConfig | body | 是 | tms_config对象 | tmsConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConfig/list

- 名称：系统配置-分页列表查询
- Operation ID：`queryPageListUsingGET_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| isShow | query | 否 | string | 1 显示 2 不显示 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| paramKey | query | 否 | string | 参数key |
| paramValue | query | 否 | string | 参数值 |
| remark | query | 否 | string | 描述 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_config对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConfig/queryAll

- 名称：系统配置-查询全部
- Operation ID：`queryAllUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_config对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsConfig/queryById

- 名称：系统配置-通过id查询
- Operation ID：`queryByIdUsingGET_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_config对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms/tmsServer/tmsConfig/updateAll

- 名称：系统配置-修改全部
- Operation ID：`updateAllUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| paramsMap | body | 是 | object | paramsMap |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 小车任务

#### POST /jeecg-tms/tmsServer/tmsTask/add

- 名称：小车任务-添加
- Operation ID：`addUsingPOST_32`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTask | body | 是 | tms_task对象0 | tmsTask |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTask/delete

- 名称：小车任务-通过id删除
- Operation ID：`deleteUsingDELETE_32`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTask/deleteBatch

- 名称：小车任务-批量删除
- Operation ID：`deleteBatchUsingDELETE_32`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTask/edit

- 名称：小车任务-编辑
- Operation ID：`editUsingPOST_32`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTask | body | 是 | tms_task对象0 | tmsTask |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTask/edit

- 名称：小车任务-编辑
- Operation ID：`editUsingPUT_32`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTask | body | 是 | tms_task对象0 | tmsTask |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTask/list

- 名称：小车任务-分页列表查询
- Operation ID：`queryPageListUsingGET_33`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessConfigId | query | 否 | string | 业务配置ID |
| conditionalCombinationCode | query | 否 | string | - |
| conditionalCombinationId | query | 否 | string | 条件组id |
| containerCode | query | 否 | string | - |
| containerId | query | 否 | string | 容器id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endCavernCode | query | 否 | string | - |
| endCavernName | query | 否 | string | - |
| endLocationCode | query | 否 | string | - |
| endLocationId | query | 否 | string | 目标点位id |
| endLocationName | query | 否 | string | - |
| id | query | 否 | string | id |
| isException | query | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | query | 否 | string(date-time) | 任务下发时间 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pidCode | query | 否 | string | 任务父编号 |
| ruleCode | query | 否 | string | - |
| ruleId | query | 否 | string | 规则ID |
| ruleName | query | 否 | string | - |
| startCavernCode | query | 否 | string | - |
| startCavernName | query | 否 | string | - |
| startLocationCode | query | 否 | string | - |
| startLocationId | query | 否 | string | 起始点位id |
| startLocationName | query | 否 | string | - |
| status | query | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | query | 否 | string | 任务编号 |
| taskMode | query | 否 | string | - |
| taskOverTime | query | 否 | string(date-time) | 任务完成时间 |
| taskPollId | query | 否 | string | 任务池id |
| taskPriority | query | 否 | string | 任务优先级 |
| taskSource | query | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | query | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | query | 否 | string | 任务类型id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleCode | query | 否 | string | - |
| vehicleId | query | 否 | string | - |
| vehicleTypeCode | query | 否 | string | - |
| vehicleTypeName | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTask/queryById

- 名称：小车任务-通过id查询
- Operation ID：`queryByIdUsingGET_32`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 需求池

#### POST /jeecg-tms/tmsServer/tmsDemandPoll/add

- 名称：需求池-添加
- Operation ID：`addUsingPOST_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandPoll | body | 是 | tms_demand_poll对象 | tmsDemandPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsDemandPoll/delete

- 名称：需求池-通过id删除
- Operation ID：`deleteUsingDELETE_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsDemandPoll/deleteBatch

- 名称：需求池-批量删除
- Operation ID：`deleteBatchUsingDELETE_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsDemandPoll/edit

- 名称：需求池-编辑
- Operation ID：`editUsingPOST_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandPoll | body | 是 | tms_demand_poll对象 | tmsDemandPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsDemandPoll/edit

- 名称：需求池-编辑
- Operation ID：`editUsingPUT_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandPoll | body | 是 | tms_demand_poll对象 | tmsDemandPoll |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDemandPoll/list

- 名称：需求池-分页列表查询
- Operation ID：`queryPageListUsingGET_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| cancelTime | query | 否 | string(date-time) | - |
| category | query | 否 | string | - |
| commandSourceSystem | query | 否 | string | - |
| containerCode | query | 否 | string | - |
| createTime | query | 否 | string(date-time) | - |
| currentCavernCode | query | 否 | string | - |
| currentCavernName | query | 否 | string | - |
| currentLocCode | query | 否 | string | - |
| currentLogicalCode | query | 否 | string | - |
| currentLogicalName | query | 否 | string | - |
| demandId | query | 否 | string | - |
| flagEight | query | 否 | string | - |
| flagEleven | query | 否 | string | - |
| flagFive | query | 否 | string | - |
| flagFour | query | 否 | string | - |
| flagNine | query | 否 | string | - |
| flagOne | query | 否 | string | - |
| flagSeven | query | 否 | string | - |
| flagSix | query | 否 | string | - |
| flagTen | query | 否 | string | - |
| flagThree | query | 否 | string | - |
| flagTwelve | query | 否 | string | - |
| flagTwo | query | 否 | string | - |
| flowCardNo | query | 否 | string | - |
| goodsTypeCode | query | 否 | string | - |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pattern | query | 否 | string | - |
| priority | query | 否 | integer(int32) | - |
| status | query | 否 | string | - |
| targetCavernCode | query | 否 | string | - |
| targetCavernName | query | 否 | string | - |
| targetLocCode | query | 否 | string | - |
| targetLogicalAreaCode | query | 否 | string | - |
| targetLogicalCode | query | 否 | string | - |
| targetLogicalName | query | 否 | string | - |
| targetStorageLocationCode | query | 否 | string | - |
| taskType | query | 否 | string | - |
| updateTime | query | 否 | string(date-time) | - |
| upstreamTaskNo | query | 否 | string | - |
| workOrderNo | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«TmsDemandPollVO»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDemandPoll/queryById

- 名称：需求池-通过id查询
- Operation ID：`queryByIdUsingGET_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_demand_poll对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 需求条件配置

#### POST /jeecg-tms/tmsServer/tmsDemandCondition/add

- 名称：需求条件配置-添加
- Operation ID：`addUsingPOST_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandCondition | body | 是 | tms_demand_condition对象 | tmsDemandCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsDemandCondition/delete

- 名称：需求条件配置-通过id删除
- Operation ID：`deleteUsingDELETE_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsDemandCondition/deleteBatch

- 名称：需求条件配置-批量删除
- Operation ID：`deleteBatchUsingDELETE_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsDemandCondition/edit

- 名称：需求条件配置-编辑
- Operation ID：`editUsingPOST_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandCondition | body | 是 | tms_demand_condition对象 | tmsDemandCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsDemandCondition/edit

- 名称：需求条件配置-编辑
- Operation ID：`editUsingPUT_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsDemandCondition | body | 是 | tms_demand_condition对象 | tmsDemandCondition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDemandCondition/list

- 名称：需求条件配置-分页列表查询
- Operation ID：`queryPageListUsingGET_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| flagFive | query | 否 | string | 流程卡标识5 |
| flagOne | query | 否 | string | 流程卡标识1 |
| flagThree | query | 否 | string | 流程卡标识3 |
| flagTwo | query | 否 | string | 流程卡标识2 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| storageLocationIds | query | 否 | string | 储位范围ID，逗号拼接 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_demand_condition对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsDemandCondition/queryById

- 名称：需求条件配置-通过id查询
- Operation ID：`queryByIdUsingGET_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_demand_condition对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 业务配置

#### POST /jeecg-tms/tmsServer/tmsBusinessConfig/add

- 名称：业务配置-添加
- Operation ID：`addUsingPOST_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBusinessConfig | body | 是 | tms_business_config对象 | tmsBusinessConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsBusinessConfig/delete

- 名称：业务配置-通过id删除
- Operation ID：`deleteUsingDELETE_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsBusinessConfig/deleteBatch

- 名称：业务配置-批量删除
- Operation ID：`deleteBatchUsingDELETE_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsBusinessConfig/edit

- 名称：业务配置-编辑
- Operation ID：`editUsingPOST_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBusinessConfig | body | 是 | tms_business_config对象 | tmsBusinessConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsBusinessConfig/edit

- 名称：业务配置-编辑
- Operation ID：`editUsingPUT_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBusinessConfig | body | 是 | tms_business_config对象 | tmsBusinessConfig |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBusinessConfig/list

- 名称：业务配置-分页列表查询
- Operation ID：`queryPageListUsingGET_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessConfigCode | query | 否 | string | 业务类型编码 |
| businessConfigName | query | 否 | string | 业务类型名称 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| status | query | 否 | string | 状态：1 正常，2 禁用 |
| strategyId | query | 否 | string | 策略id |
| taskTypeId | query | 否 | string | 任务类型id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_business_config对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsBusinessConfig/queryById

- 名称：业务配置-通过id查询
- Operation ID：`queryByIdUsingGET_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_business_config对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 异常信息管理

#### POST /jeecg-tms/tmsServer/tmsTaskAbnormal/add

- 名称：异常信息管理-添加
- Operation ID：`addUsingPOST_31`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskAbnormal | body | 是 | tms_task_abnormal对象 | tmsTaskAbnormal |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskAbnormal/delete

- 名称：异常信息管理-通过id删除
- Operation ID：`deleteUsingDELETE_31`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskAbnormal/deleteBatch

- 名称：异常信息管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_31`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskAbnormal/edit

- 名称：异常信息管理-编辑
- Operation ID：`editUsingPOST_31`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskAbnormal | body | 是 | tms_task_abnormal对象 | tmsTaskAbnormal |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskAbnormal/edit

- 名称：异常信息管理-编辑
- Operation ID：`editUsingPUT_31`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskAbnormal | body | 是 | tms_task_abnormal对象 | tmsTaskAbnormal |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskAbnormal/list

- 名称：异常信息管理-分页列表查询
- Operation ID：`queryPageListUsingGET_32`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| abnormalFlag | query | 否 | string | - |
| abnormalType | query | 否 | string | 异常类型 |
| beginTime | query | 否 | string(date-time) | 告警开始时间 |
| businessConfigId | query | 否 | string | 业务配置ID |
| code | query | 否 | string | 异常记录编码 |
| containerId | query | 否 | string | 容器ID |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endStorageLocationId | query | 否 | string | 终点储位编码 |
| equipmentCoding | query | 否 | string | 设备编码：呼叫器为IP+区域，车辆为车辆编号 |
| id | query | 否 | string | id |
| object | query | 否 | string | 报警对象 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| remark | query | 否 | string | - |
| startStorageLocationId | query | 否 | string | 起始储位ID |
| taskCode | query | 否 | string | 任务编码 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| warnContent | query | 否 | string | 告警内容 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_abnormal对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskAbnormal/queryById

- 名称：异常信息管理-通过id查询
- Operation ID：`queryByIdUsingGET_31`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_abnormal对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### AGV异常日志

#### POST /jeecg-tms/tmsServer/tmsAgvError/add

- 名称：AGV异常日志-添加
- Operation ID：`addUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsAgvError | body | 是 | tms_agv_error对象 | tmsAgvError |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsAgvError/delete

- 名称：AGV异常日志-通过id删除
- Operation ID：`deleteUsingDELETE`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsAgvError/deleteBatch

- 名称：AGV异常日志-批量删除
- Operation ID：`deleteBatchUsingDELETE`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsAgvError/edit

- 名称：AGV异常日志-编辑
- Operation ID：`editUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsAgvError | body | 是 | tms_agv_error对象 | tmsAgvError |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsAgvError/edit

- 名称：AGV异常日志-编辑
- Operation ID：`editUsingPUT`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsAgvError | body | 是 | tms_agv_error对象 | tmsAgvError |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsAgvError/list

- 名称：AGV异常日志-分页列表查询
- Operation ID：`queryPageListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| agvCode | query | 否 | string | 车辆编码 |
| containerCode | query | 否 | string | 容器编码 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| reqCode | query | 否 | string | RCS请求编码 |
| taskCode | query | 否 | string | 任务编码 |
| type | query | 否 | integer(int32) | 操作类型: 1 取消, 2 完成 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_agv_error对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsAgvError/queryById

- 名称：AGV异常日志-通过id查询
- Operation ID：`queryByIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_agv_error对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### PDA日志

#### POST /jeecg-tms/tmsServer/tmsPdaLog/add

- 名称：PDA日志-添加
- Operation ID：`addUsingPOST_18`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaLog | body | 是 | tms_pda_log���� | tmsPdaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsPdaLog/delete

- 名称：PDA日志-通过id删除
- Operation ID：`deleteUsingDELETE_18`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsPdaLog/deleteBatch

- 名称：PDA日志-批量删除
- Operation ID：`deleteBatchUsingDELETE_18`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsPdaLog/edit

- 名称：PDA日志-编辑
- Operation ID：`editUsingPOST_18`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaLog | body | 是 | tms_pda_log���� | tmsPdaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsPdaLog/edit

- 名称：PDA日志-编辑
- Operation ID：`editUsingPUT_18`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaLog | body | 是 | tms_pda_log���� | tmsPdaLog |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsPdaLog/list

- 名称：PDA日志-分页列表查询
- Operation ID：`queryPageListUsingGET_18`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| ip | query | 否 | string | ip |
| operationModule | query | 否 | string | 操作模块 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pdaLogId | query | 否 | string | pda日志ID |
| remark | query | 否 | string | 备注 |
| requestParams | query | 否 | string | 请求参数 |
| requestUrl | query | 否 | string | 请求地址 |
| returnedValue | query | 否 | string | 接口返回值 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |
| userId | query | 否 | string | 操作用户账号 |
| userName | query | 否 | string | 操作用户名 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_pda_log����»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsPdaLog/queryById

- 名称：PDA日志-通过id查询
- Operation ID：`queryByIdUsingGET_18`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_pda_log����» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### TMS任务组

#### POST /jeecg-tms/tmsServer/tmsTaskUpstream/add

- 名称：TMS任务组-添加
- Operation ID：`addUsingPOST_37`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskUpstream | body | 是 | tms_task_poll对象 | tmsTaskUpstream |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-tms/tmsServer/tmsTaskUpstream/delete

- 名称：TMS任务组-通过id删除
- Operation ID：`deleteUsingDELETE_37`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-tms/tmsServer/tmsTaskUpstream/deleteBatch

- 名称：TMS任务组-批量删除
- Operation ID：`deleteBatchUsingDELETE_37`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-tms/tmsServer/tmsTaskUpstream/edit

- 名称：TMS任务组-编辑
- Operation ID：`editUsingPOST_37`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskUpstream | body | 是 | tms_task_poll对象 | tmsTaskUpstream |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-tms/tmsServer/tmsTaskUpstream/edit

- 名称：TMS任务组-编辑
- Operation ID：`editUsingPUT_37`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsTaskUpstream | body | 是 | tms_task_poll对象 | tmsTaskUpstream |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskUpstream/list

- 名称：TMS任务组-分页列表查询
- Operation ID：`queryPageListUsingGET_39`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessConfigId | query | 否 | string | 业务配置ID |
| conditionalCombinationCode | query | 否 | string | - |
| conditionalCombinationId | query | 否 | string | 条件组id |
| containerCode | query | 否 | string | - |
| containerId | query | 否 | string | 容器id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| endCavernCode | query | 否 | string | - |
| endCavernName | query | 否 | string | - |
| endLocationCode | query | 否 | string | - |
| endLocationId | query | 否 | string | 目标点位id |
| endLocationName | query | 否 | string | - |
| id | query | 否 | string | id |
| isException | query | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | query | 否 | string(date-time) | 任务下发时间 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| pidCode | query | 否 | string | 任务父编号 |
| ruleCode | query | 否 | string | - |
| ruleId | query | 否 | string | 规则ID |
| ruleName | query | 否 | string | - |
| startCavernCode | query | 否 | string | - |
| startCavernName | query | 否 | string | - |
| startLocationCode | query | 否 | string | - |
| startLocationId | query | 否 | string | 起始点位id |
| startLocationName | query | 否 | string | - |
| status | query | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | query | 否 | string | 任务编号 |
| taskMode | query | 否 | string | - |
| taskOverTime | query | 否 | string(date-time) | 任务完成时间 |
| taskPollId | query | 否 | string | 任务池id |
| taskPriority | query | 否 | string | 任务优先级 |
| taskSource | query | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | query | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | query | 否 | string | 任务类型id |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |
| vehicleCode | query | 否 | string | 执行车辆编号 |
| vehicleId | query | 否 | string | - |
| vehicleTypeCode | query | 否 | string | - |
| vehicleTypeName | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_task_upstream对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms/tmsServer/tmsTaskUpstream/queryById

- 名称：TMS任务组-通过id查询
- Operation ID：`queryByIdUsingGET_37`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_poll对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

## 数据模型

### 接口返回对象«IPage«tms_agv_error对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_agv_error对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_broadcast_speech对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_broadcast_speech对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_broadcast_template对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_broadcast_template对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_business_config对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_business_config对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_condition对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_condition对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_conditional_combination对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_conditional_combination对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_config对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_config对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_container对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_container对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_control_area_log对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_control_area_log对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_demand_condition对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_demand_condition对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_depth_group对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_depth_group对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_door对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_door对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_flow_card对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_flow_card对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_goods_type对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_goods_type对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_logical_area_tag对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_logical_area_tag对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_monitoring_source_log对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_monitoring_source_log对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_operation_rule对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_operation_rule对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_pda_log����»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_pda_log����» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_process_route对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_process_route对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_process对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_process对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_query_demand_log对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_query_demand_log对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_router对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_router对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_rule_dict对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_rule_dict对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_rule对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_rule对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_send_http_log对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_send_http_log对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_storage_cavern_type对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_storage_cavern_type对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_storage_cavern对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_storage_cavern对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_storage_location_button对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_storage_location_button对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_storage_location对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_storage_location对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_strategy对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_strategy对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_abnormal对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_abnormal对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_poll对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_poll对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_type_range对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_type_range对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_type_route对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_type_route对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_type对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_type对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task_upstream对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task_upstream对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_task对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_task对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_vehicle_group对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_vehicle_group对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_vehicle_type对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_vehicle_type对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_vehicle对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_vehicle对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_warehouse对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_warehouse对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_work_order对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_work_order对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«TmsDemandPollVO»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«TmsDemandPollVO» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«TmsLocStatement»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«TmsLocStatement» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«DepthGroupLocation»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<DepthGroupLocation> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_condition_table_column对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_condition_table_column对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_condition_table对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_condition_table对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_config对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_config对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_task_poll_status对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_task_poll_status对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_vehicle_group对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_vehicle_group对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«string»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | string | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_agv_error对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_agv_error对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_broadcast_speech对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_broadcast_speech对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_broadcast_template对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_broadcast_template对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_business_config对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_business_config对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_condition_table_column对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_condition_table_column对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_condition对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_condition对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_conditional_combination对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_conditional_combination对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_config对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_config对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_container对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_container对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_control_area_log对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_control_area_log对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_demand_condition对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_demand_condition对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_demand_poll对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_demand_poll对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_depth_group对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_depth_group对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_door对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_door对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_flow_card对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_flow_card对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_goods_type对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_goods_type对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_logical_area_tag对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_logical_area_tag对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_monitoring_source_log对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_monitoring_source_log对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_operation_rule对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_operation_rule对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_pda_log����»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_pda_log���� | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_process_route对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_process_route对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_process对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_process对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_query_demand_log对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_query_demand_log对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_router对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_router对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_rule_dict对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_rule_dict对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_rule对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_rule对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_send_http_log对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_send_http_log对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_storage_cavern_type对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_storage_cavern_type对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_storage_cavern对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_storage_cavern对象1 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_storage_location_button对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_storage_location_button对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_storage_location对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_storage_location对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_strategy对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_strategy对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task_abnormal对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task_abnormal对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task_poll对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task_poll对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task_type_range对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task_type_range对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task_type_route对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task_type_route对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task_type对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task_type对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_task对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_task对象1 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_vehicle_group对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_vehicle_group对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_vehicle_type对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_vehicle_type对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_vehicle对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_vehicle对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_warehouse对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_warehouse对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_work_order对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_work_order对象0 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 条件对象

条件

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| columnId | 否 | integer(int32) | 列ID |
| columnName | 否 | string | 列名称 |
| conditionBaseOperator | 否 | string | 条件运算符(等于、加、减、乘、除、余数、IF、左括号、右括号、与、或、非、包含) |
| conditionGroupId | 否 | string | 所属条件分组id |
| conditionKey | 否 | string | 条件key：(表名,字段, |
| conditionLogicalOperator | 否 | string | 与、或 |
| conditionValue | 否 | string | 条件值 |
| conditionalCombinationId | 否 | string | 所属条件组 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isQueryDatabase | 否 | string | 是否查询数据库：1 是，2 否 |
| moduleId | 否 | integer(int32) | 模块ID |
| queryDemand | 否 | string | 是否根据需求查询匹配条件：1是，2否 |
| sort | 否 | integer(int32) | 排序，或相关时起作用，判断条件优先级 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### 条件分组对象Req

条件分组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| childrenGroups | 否 | array<条件分组对象Req> | 子分组列表 |
| conditionLogicalOperator | 否 | string | 与、或逻辑关系 |
| conditionalCombinationId | 否 | string | 所属条件组ID |
| conditions | 否 | array<条件对象> | 当前分组条件列表 |
| createBy | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| id | 否 | string | 条件分组ID |
| parentId | 否 | string | 父分组ID |
| sort | 否 | integer(int32) | 排序 |
| updateBy | 否 | string |  |
| updateTime | 否 | string(date-time) |  |

### 条件分组对象Res

条件分组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| allConditionsCount | 否 | integer(int32) |  |
| childrenGroups | 否 | array<条件分组对象Res> | 子分组列表 |
| conditionLogicalOperator | 否 | string | 与、或逻辑关系 |
| conditionalCombinationId | 否 | string | 所属条件组ID |
| conditions | 否 | array<条件对象> | 当前分组条件列表 |
| createBy | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| id | 否 | string | 条件分组ID |
| parentId | 否 | string | 父分组ID |
| sort | 否 | integer(int32) | 排序 |
| updateBy | 否 | string |  |
| updateTime | 否 | string(date-time) |  |

### BatchUpdateFlag

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| editFlag | 否 | string |  |
| flag | 否 | string |  |
| ids | 否 | string |  |

### DepthGroupLocation

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| l | 否 | integer(int32) |  |
| locationCode | 否 | string |  |
| r | 否 | integer(int32) |  |
| rowNumber | 否 | integer(int32) |  |

### IPage«tms_agv_error对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_agv_error对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_broadcast_speech对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_broadcast_speech对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_broadcast_template对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_broadcast_template对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_business_config对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_business_config对象0> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_condition对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_condition对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_conditional_combination对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_conditional_combination对象Res> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_config对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_config对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_container对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_container对象1> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_control_area_log对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_control_area_log对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_demand_condition对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_demand_condition对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_depth_group对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_depth_group对象0> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_door对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_door对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_flow_card对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_flow_card对象10> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_goods_type对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_goods_type对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_logical_area_tag对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_logical_area_tag对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_monitoring_source_log对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_monitoring_source_log对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_operation_rule对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_operation_rule对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_pda_log����»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_pda_log����> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_process_route对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_process_route对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_process对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_process对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_query_demand_log对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_query_demand_log对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_router对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_router对象0> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_rule_dict对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_rule_dict对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_rule对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_rule对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_send_http_log对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_send_http_log对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_storage_cavern_type对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_storage_cavern_type对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_storage_cavern对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_storage_cavern对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_storage_location_button对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_storage_location_button对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_storage_location对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_storage_location对象1> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_strategy对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_strategy对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_abnormal对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_abnormal对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_poll对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_poll对象0> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_type_range对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_type_range对象0> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_type_route对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_type_route对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_type对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_type对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task_upstream对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task_upstream对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_task对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_task对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_vehicle_group对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_vehicle_group对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_vehicle_type对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_vehicle_type对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_vehicle对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_vehicle对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_warehouse对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_warehouse对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_work_order对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_work_order对象1> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«TmsDemandPollVO»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<TmsDemandPollVO> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«TmsLocStatement»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<TmsLocStatement> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### LogicalAreaIndex

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| index | 否 | integer(int32) |  |
| label | 否 | string |  |
| logicalAreaId | 否 | string |  |

### tms_agv_error对象

AGV异常日志

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| agvCode | 否 | string | 车辆编码 |
| containerCode | 否 | string | 容器编码 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| reqCode | 否 | string | RCS请求编码 |
| taskCode | 否 | string | 任务编码 |
| type | 否 | integer(int32) | 操作类型: 1 取消, 2 完成 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_broadcast_speech对象

广播语

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 广播语编码 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| id | 否 | string | 主键 |
| isStrategyFlag | 否 | string |  |
| name | 否 | string | 广播语名称 |
| status | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | 否 | string | 所属部门 |
| templateId | 否 | string | 广播模板ID |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### tms_broadcast_template对象

广播模板

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 模板编码 |
| content | 否 | string | 模板内容 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| id | 否 | string | 主键 |
| name | 否 | string | 模板名称 |
| status | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | 否 | string | 所属部门 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### tms_business_config对象

业务配置

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigCode | 否 | string | 业务类型编码 |
| businessConfigName | 否 | string | 业务类型名称 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| strategyId | 否 | string | 策略id |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_business_config对象0

业务配置

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigCode | 否 | string | 业务类型编码 |
| businessConfigName | 否 | string | 业务类型名称 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| strategyCode | 否 | string |  |
| strategyId | 否 | string | 策略id |
| strategyName | 否 | string |  |
| taskTypeCode | 否 | string |  |
| taskTypeId | 否 | string | 任务类型id |
| taskTypeName | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_condition_table_column对象

条件字段使用表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| columnCode | 否 | string | 字段code |
| columnDictData | 否 | string | 数据来源：字典对应的码 |
| columnName | 否 | string | 字段名称 |
| conditionTableId | 否 | integer(int32) | 表id |
| id | 否 | integer(int32) | 字段id |
| isDict | 否 | integer(int32) | 是否来源于字典：1是，2否 |
| queryDemand | 否 | string | 是否根据需求查询匹配条件：1是，2否 |
| status | 否 | integer(int32) | 状态：1启用，2禁用 |

### tms_condition_table对象

条件使用表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| conditionTableCode | 否 | string | 表名 |
| conditionTableName | 否 | string | 表描述 |
| id | 否 | integer(int32) | id |
| isTable | 否 | integer(int32) | 是否是真实表：1是，2不是 |
| status | 否 | integer(int32) | 状态：1启用，2禁用 |
| type | 否 | integer(int32) | 所属 1 条件组 2 规则 3 条件组+规则 |

### tms_condition对象

条件

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| conditionBaseOperator | 否 | string | 条件运算符(等于、加、减、乘、除、余数、IF、左括号、右括号、与、或、非、包含) |
| conditionGroupId | 否 | string | 所属条件分组id |
| conditionKey | 否 | string | 条件key：(表名,字段, |
| conditionLogicalOperator | 否 | string | 与、或 |
| conditionValue | 否 | string | 条件值 |
| conditionalCombinationId | 否 | string | 所属条件组 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isQueryDatabase | 否 | string | 是否查询数据库：1 是，2 否 |
| queryDemand | 否 | string | 是否根据需求查询匹配条件：1是，2否 |
| sort | 否 | integer(int32) | 排序，或相关时起作用，判断条件优先级 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_conditional_combination对象0

条件组管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 条件组编码 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| name | 否 | string | 条件组名称 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_conditional_combination对象1Req

条件组管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 条件组编码 |
| conditionGroup | 否 | 条件分组对象Req |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| name | 否 | string | 条件组名称 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_conditional_combination对象Res

条件组管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 条件组编码 |
| conditionGroup | 否 | 条件分组对象Res |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| name | 否 | string | 条件组名称 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_config对象

tms_config

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isShow | 否 | string | 1 显示 2 不显示 |
| paramKey | 否 | string | 参数key |
| paramValue | 否 | string | 参数值 |
| remark | 否 | string | 描述 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_container对象

容器管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| containerCode | 否 | string | 容器编码 |
| containerGood | 否 | string | 容器商品 |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| containerStatus | 否 | string | 容器状态：0 空，1 满，2 满+1 |
| containerWeight | 否 | string | 容器重量 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deleted | 否 | integer(int32) |  |
| flowCardCode | 否 | string |  |
| flowCardCodes | 否 | string |  |
| goodsTypeCode | 否 | string |  |
| goodsTypeId | 否 | string | 货型id |
| id | 否 | string | id |
| orderFlag | 否 | string | 工单标 |
| processFlag | 否 | string | 工序标：0 镭射过油，1 丝印，2 翻纸工序，3 打包工序，4 首件签样，5 复合工序，6 单凹工序，7 切纸工序，8 模切工序，9 机检工序， 10 烫金工序，11 凹印工序，12 胶印工序，13 模切工序，14 打包工序 |
| storageLocationCode | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_container对象0

容器管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| containerCode | 否 | string | 容器编码 |
| containerGood | 否 | string | 容器商品 |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| containerStatus | 否 | string | 容器状态：0 空，1 满，2 满+1 |
| containerWeight | 否 | string | 容器重量 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deleted | 否 | integer(int32) |  |
| goodsTypeId | 否 | string | 货型id |
| id | 否 | string | id |
| orderFlag | 否 | string | 工单标 |
| processFlag | 否 | string | 工序标：0 镭射过油，1 丝印，2 翻纸工序，3 打包工序，4 首件签样，5 复合工序，6 单凹工序，7 切纸工序，8 模切工序，9 机检工序， 10 烫金工序，11 凹印工序，12 胶印工序，13 模切工序，14 打包工序 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_container对象1

容器管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| containerCode | 否 | string | 容器编码 |
| containerGood | 否 | string | 容器商品 |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| containerStatus | 否 | string | 容器状态：0 空，1 满，2 满+1 |
| containerWeight | 否 | string | 容器重量 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deleted | 否 | integer(int32) |  |
| flowCardCode | 否 | string |  |
| flowCardCodes | 否 | string |  |
| goodsTypeCode | 否 | string |  |
| goodsTypeId | 否 | string | 货型id |
| id | 否 | string | id |
| orderFlag | 否 | string | 工单标 |
| processFlag | 否 | string | 工序标：0 镭射过油，1 丝印，2 翻纸工序，3 打包工序，4 首件签样，5 复合工序，6 单凹工序，7 切纸工序，8 模切工序，9 机检工序， 10 烫金工序，11 凹印工序，12 胶印工序，13 模切工序，14 打包工序 |
| storageLocationCode | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_control_area_log对象

管制区日志

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| controlAreaId | 否 | string | 管制区ID |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| id | 否 | string | 主键 |
| reqCode | 否 | string | 请求编码 |
| status | 否 | string | 状态：1 请求进入，2 已进入，3 已退出管制区 |
| sysOrgCode | 否 | string | 所属部门 |
| taskCode | 否 | string | 任务请求编码 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |
| vehicleId | 否 | string | 车辆ID |

### tms_demand_condition对象

tms_demand_condition

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagFive | 否 | string | 流程卡标识5 |
| flagOne | 否 | string | 流程卡标识1 |
| flagThree | 否 | string | 流程卡标识3 |
| flagTwo | 否 | string | 流程卡标识2 |
| id | 否 | string | id |
| storageLocationIds | 否 | string | 储位范围ID，逗号拼接 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

### tms_demand_poll对象

tms_demand_poll

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| cancelTaskSystem | 否 | string | 取消任务系统 |
| cancelTime | 否 | string(date-time) | 取消时间 |
| category | 否 | string |  |
| commandSourceSystem | 否 | string | 指令来源系统 |
| comment | 否 | string | 备注（点对区下发任务时所扫描的信息） |
| containerCode | 否 | string | 容器编码 |
| containerId | 否 | string | 容器ID |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| currentLogicalAreaCode | 否 | string |  |
| currentLogicalAreaId | 否 | string |  |
| currentMachineId | 否 | string | 当前机台ID |
| currentProcessId | 否 | string | 当前工序ID |
| currentStorageCavernBusinessId | 否 | string | 当前储区业务ID |
| currentStorageCavernCode | 否 | string | 当前储区编码 |
| currentStorageCavernId | 否 | string | 当前储区ID |
| currentStorageLocationBusinessId | 否 | string | 当前储位业务ID |
| currentStorageLocationCode | 否 | string | 当前储位编码 |
| currentStorageLocationId | 否 | string | 当前储位ID |
| dateInProduced | 否 | string(date-time) | 生产日期 |
| demandId | 否 | string | 需求ID |
| demandType | 否 | string |  |
| flagEight | 否 | string |  |
| flagEleven | 否 | string |  |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagNine | 否 | string |  |
| flagOne | 否 | string |  |
| flagSeven | 否 | string |  |
| flagSix | 否 | string |  |
| flagTen | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwelve | 否 | string |  |
| flagTwo | 否 | string |  |
| flowCardId | 否 | string | 流程卡ID |
| flowCardNum | 否 | string | 流程卡号 |
| goodsTypeCode | 否 | string | 货型编码 |
| goodsTypeId | 否 | string | 货型ID |
| id | 否 | string | id |
| itemCharacter | 否 | string | 物料特性 |
| itemCode | 否 | string | 物料编码 |
| itemId | 否 | string | 物料ID |
| itemQty | 否 | integer(int32) | 物料数量 |
| lastProcessCode | 否 | string | 上工序编码 |
| lastProcessId | 否 | string | 上工序ID |
| nextProcessCode | 否 | string | 下工序编码 |
| nextProcessId | 否 | string | 下工序ID |
| pattern | 否 | string | 模式：1 上料， 2 下料， 3 点对点 |
| priority | 否 | integer(int32) | 优先级 |
| remark | 否 | string | 备注：显示失败原因等等 |
| sort | 否 | integer(int32) | 排序：本系统定义/承接上层系统 |
| status | 否 | string | 状态：1 待处理，2 已处理，3 已取消 |
| sysOrgCode | 否 | string | 所属部门 |
| targetLogicalAreaCode | 否 | string | 目的逻辑区编码 |
| targetLogicalAreaId | 否 | string | 目的逻辑区ID |
| targetMachineId | 否 | string | 目的机台ID |
| targetStorageCavernBusinessId | 否 | string | 目的储区业务ID |
| targetStorageCavernCode | 否 | string | 目的储区编码 |
| targetStorageCavernId | 否 | string | 目的储区ID |
| targetStorageLocationBusinessId | 否 | string | 目的储位业务ID |
| targetStorageLocationCode | 否 | string | 目的储位编码 |
| targetStorageLocationId | 否 | string | 目的储位ID |
| taskPollId | 否 | string | 容器任务池任务ID |
| taskType | 否 | string | 任务类型: 承接上层系统 |
| thisProcessCode | 否 | string | 本工序编码 |
| thisProcessId | 否 | string | 本工序ID |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |
| upstreamTaskNo | 否 | string | 上层系统任务单号 |
| workOrder | 否 | string | 工单 |

### tms_depth_group对象

tms_depth_group

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| depthGroupCode | 否 | string | 深度组编码 |
| depthOne | 否 | integer(int32) | 深度1，默认左 |
| depthTwo | 否 | integer(int32) |  |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagOne | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwo | 否 | string |  |
| freeFlag | 否 | integer(int32) |  |
| hitTheShelfFlag | 否 | integer(int32) |  |
| hitTheShelfOrder | 否 | integer(int32) | 上架顺序 |
| id | 否 | string | id |
| qrCode | 否 | string |  |
| qrCodeStatus | 否 | integer(int32) |  |
| singleOrDouble | 否 | string | 单双向：1 单，2 双 |
| soldOutFlag | 否 | integer(int32) |  |
| soldOutOrder | 否 | integer(int32) | 下架顺序 |
| storageLocationId | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_depth_group对象0

tms_depth_group

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessId | 否 | string |  |
| caBusinessId | 否 | string |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| depthGroupCode | 否 | string | 深度组编码 |
| depthOne | 否 | integer(int32) | 深度1，默认左 |
| depthTwo | 否 | integer(int32) |  |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagOne | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwo | 否 | string |  |
| freeFlag | 否 | integer(int32) |  |
| groupByZ | 否 | string |  |
| hitTheShelfFlag | 否 | integer(int32) |  |
| hitTheShelfOrder | 否 | integer(int32) | 上架顺序 |
| id | 否 | string | id |
| orderByZ | 否 | string |  |
| qrCode | 否 | string |  |
| qrCodeStatus | 否 | integer(int32) |  |
| singleOrDouble | 否 | string | 单双向：1 单，2 双 |
| soldOutFlag | 否 | integer(int32) |  |
| soldOutOrder | 否 | integer(int32) | 下架顺序 |
| storageCavernCode | 否 | string |  |
| storageCavernId | 否 | string |  |
| storageCavernName | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| storageLocationStatus | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseCode | 否 | string |  |

### tms_depth_group对象1

tms_depth_group

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessId | 否 | string |  |
| caBusinessId | 否 | string |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| depthGroupCode | 否 | string | 深度组编码 |
| depthOne | 否 | integer(int32) | 深度1，默认左 |
| depthTwo | 否 | integer(int32) |  |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagOne | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwo | 否 | string |  |
| freeFlag | 否 | integer(int32) |  |
| groupByZ | 否 | string |  |
| hitTheShelfFlag | 否 | integer(int32) |  |
| hitTheShelfOrder | 否 | integer(int32) | 上架顺序 |
| id | 否 | string | id |
| orderByZ | 否 | string |  |
| qrCode | 否 | string |  |
| qrCodeStatus | 否 | integer(int32) |  |
| singleOrDouble | 否 | string | 单双向：1 单，2 双 |
| soldOutFlag | 否 | integer(int32) |  |
| soldOutOrder | 否 | integer(int32) | 下架顺序 |
| storageCavernCode | 否 | string |  |
| storageCavernId | 否 | string |  |
| storageCavernName | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| storageLocationStatus | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseCode | 否 | string |  |

### tms_door对象

门

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| closeStatusOffset | 否 | integer(int32) | 关状态反馈点 |
| closeWriteOffset | 否 | integer(int32) | 关状态写入点 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建人 |
| doorName | 否 | string | 门名称 |
| id | 否 | string | id |
| ip | 否 | string | modbus ip |
| openStatusOffset | 否 | integer(int32) | 开状态反馈点 |
| openWriteOffset | 否 | integer(int32) | 开状态写入点 |
| port | 否 | integer(int32) | modbus 端口 |
| slaveId | 否 | integer(int32) | modbus 从设备ID |
| sysOrgCode | 否 | string | 所属部门 |
| tier | 否 | integer(int32) | 门所在层 |
| type | 否 | string | 1电梯2卷帘门3输送线 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### tms_flow_card对象

流程卡管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagCodes | 否 | string |  |
| flagEight | 否 | string | 标识8 |
| flagEleven | 否 | string | 标识11 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagOneCode | 否 | string |  |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagThreeCode | 否 | string |  |
| flagTips | 否 | string |  |
| flagTwelve | 否 | string | 标识12 |
| flagTwo | 否 | string | 标识2 |
| flagTwoCode | 否 | string |  |
| flowCardBusinessId | 否 | string |  |
| flowCardNumber | 否 | string | 流程卡号 |
| id | 否 | string | id |
| ids | 否 | array<string> |  |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| materialNumber | 否 | number | 物料数量 |
| serialNumber | 否 | integer(int32) | 顺序号 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderId | 否 | string | 工单id |
| workOrderNumber | 否 | string |  |

### tms_flow_card对象0

流程卡管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagEight | 否 | string | 标识8 |
| flagEleven | 否 | string | 标识11 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagTwelve | 否 | string | 标识12 |
| flagTwo | 否 | string | 标识2 |
| flowCardBusinessId | 否 | string |  |
| flowCardNumber | 否 | string | 流程卡号 |
| id | 否 | string | id |
| ids | 否 | array<string> |  |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| materialNumber | 否 | number | 物料数量 |
| serialNumber | 否 | integer(int32) | 顺序号 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderId | 否 | string | 工单id |

### tms_flow_card对象10

流程卡管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagCodes | 否 | string |  |
| flagEight | 否 | string | 标识8 |
| flagEleven | 否 | string | 标识11 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagOneCode | 否 | string |  |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagThreeCode | 否 | string |  |
| flagTips | 否 | string |  |
| flagTwelve | 否 | string | 标识12 |
| flagTwo | 否 | string | 标识2 |
| flagTwoCode | 否 | string |  |
| flowCardBusinessId | 否 | string |  |
| flowCardNumber | 否 | string | 流程卡号 |
| id | 否 | string | id |
| ids | 否 | array<string> |  |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| materialNumber | 否 | number | 物料数量 |
| serialNumber | 否 | integer(int32) | 顺序号 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderId | 否 | string | 工单id |
| workOrderNumber | 否 | string |  |

### tms_flow_card对象11

流程卡管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagEight | 否 | string | 标识8 |
| flagEleven | 否 | string | 标识11 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagTwelve | 否 | string | 标识12 |
| flagTwo | 否 | string | 标识2 |
| flowCardBusinessId | 否 | string |  |
| flowCardNumber | 否 | string | 流程卡号 |
| id | 否 | string | id |
| ids | 否 | array<string> |  |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| materialNumber | 否 | number | 物料数量 |
| serialNumber | 否 | integer(int32) | 顺序号 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderId | 否 | string | 工单id |

### tms_goods_type对象

货型管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| direction | 否 | string | 方向 |
| goodsHeight | 否 | string | 高 |
| goodsLength | 否 | string | 长 |
| goodsTypeCode | 否 | string | 货型编号 |
| goodsTypeName | 否 | string | 货型名称 |
| goodsWidth | 否 | string | 宽 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_logical_area_tag对象

逻辑区标签

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 状态：0 禁用，1 启用 |
| tagCode | 否 | string | 逻辑区标签编码 |
| tagName | 否 | string | 逻辑区标签名称 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

### tms_monitoring_source_log对象

tms_monitoring_source_log

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| discoveryTime | 否 | string(date-time) | 发现时间 |
| id | 否 | string | id |
| monitoringId | 否 | string | 资源监控日志ID |
| newData | 否 | string | 监控到状态 |
| oldData | 否 | string | 监控前状态 |
| resourceCode | 否 | string | 被监控的资源编码 |
| resourceId | 否 | string | 被监控的资源ID |
| resourceSource | 否 | string | 资源来源名称 |
| resourceType | 否 | string | 资源类型：储位，容器，车辆 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_operation_rule对象

操作型规则管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| broadcastSpeechId | 否 | string | 广播语事件ID |
| code | 否 | string | 操作型规则编码 |
| conditionalCombinationId | 否 | string | 关联条件组ID |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| id | 否 | string | 主键 |
| name | 否 | string | 操作型规则名称 |
| operationType | 否 | string | 操作类型：1 解绑 |
| status | 否 | string | 状态：0 禁用，1 启用 |
| sysOrgCode | 否 | string | 所属部门 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### tms_pda_log����

tms_pda_log

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| ip | 否 | string | ip |
| operationModule | 否 | string | 操作模块 |
| pdaLogId | 否 | string | pda日志ID |
| remark | 否 | string | 备注 |
| requestParams | 否 | string | 请求参数 |
| requestUrl | 否 | string | 请求地址 |
| returnedValue | 否 | string | 接口返回值 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |
| userId | 否 | string | 操作用户账号 |
| userName | 否 | string | 操作用户名 |

### tms_process_route_process对象

工艺路线单步表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| outputUnit | 否 | string | 产出单位(米) |
| processCode | 否 | string | 工序编码 |
| processId | 否 | string | 工序id |
| processName | 否 | string | 工序名称 |
| processRouteId | 否 | string | 工艺路线id |
| processType | 否 | string | 工序分类名称 |
| productionUnit | 否 | string | 投产单位(米) |
| sort | 否 | integer(int32) | 排序：10 20 30 40... |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_process_route对象

工艺路线

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| processRouteCode | 否 | string | 工艺路线编码 |
| processRouteName | 否 | string | 工艺路线名称 |
| status | 否 | integer(int32) | 状态：1启用， 2禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_process_route对象0

工艺路线

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endTime | 否 | string |  |
| id | 否 | string | id |
| processRouteCode | 否 | string | 工艺路线编码 |
| processRouteName | 否 | string | 工艺路线名称 |
| startTime | 否 | string |  |
| status | 否 | integer(int32) | 状态：1启用， 2禁用 |
| tmsProcessRouteProcessList | 否 | array<tms_process_route_process对象> |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_process对象

工序管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| outputUnit | 否 | string | 产出单位(米) |
| processCode | 否 | string | 工序编码 |
| processName | 否 | string | 工序名称 |
| processType | 否 | string | 工序分类名称 |
| productionUnit | 否 | string | 投产单位(米) |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_query_demand_log对象

tms_query_demand_log

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| demandId | 否 | string | 被查询需求池的需求ID |
| endTime | 否 | string(date-time) | 结束查询时间 |
| id | 否 | string | id |
| monitoringLogId | 否 | string | 监控资源日志ID |
| queryDemandId | 否 | string | 查询需求池日志ID |
| startTime | 否 | string(date-time) | 开始查询时间 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_router对象

tms_router

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endStorageLocationId | 否 | string | 终点库位id |
| id | 否 | string | id |
| routerCode | 否 | string | 路由编号 |
| routerWeight | 否 | integer(int32) | 路由权数 |
| sort | 否 | integer(int32) | 排序：用于权重相同时选择路由 |
| startStorageLocationId | 否 | string | 起点库位id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| taskTypeRouteId | 否 | string | 任务类型路由ID |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_router对象0

路由管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endStorageLocationCode | 否 | string | 终点库位 |
| endStorageLocationCodes | 否 | string |  |
| endStorageLocationId | 否 | string | 终点库位id |
| id | 否 | string | id |
| routerCode | 否 | string | 路由编号 |
| routerWeight | 否 | integer(int32) | 路由权数 |
| startStorageLocationCode | 否 | string | 起点库位 |
| startStorageLocationCodes | 否 | string |  |
| startStorageLocationId | 否 | string | 起点库位id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| taskTypeRouteId | 否 | string | 任务类型路由ID |
| taskTypeRouteName | 否 | string | 任务类型名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_router对象1

路由管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endStorageLocationCode | 否 | string | 终点库位 |
| endStorageLocationCodes | 否 | string |  |
| endStorageLocationId | 否 | string | 终点库位id |
| id | 否 | string | id |
| routerCode | 否 | string | 路由编号 |
| routerWeight | 否 | integer(int32) | 路由权数 |
| startStorageLocationCode | 否 | string | 起点库位 |
| startStorageLocationCodes | 否 | string |  |
| startStorageLocationId | 否 | string | 起点库位id |
| status | 否 | string | 状态：1 正常，2 禁用 |
| taskTypeRouteId | 否 | string | 任务类型路由ID |
| taskTypeRouteName | 否 | string | 任务类型名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_rule_dict对象

规则上下架配置

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 规则编码 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isOldRule | 否 | integer(int32) | 是否是老规则 1是 2 否 |
| isShow | 否 | string | 显示：1 显示，2 不显示 |
| name | 否 | string | 规则名称 |
| oldValue | 否 | string | 对应的，1，2，3，老版本兼容字段，新的不用 |
| remark | 否 | string | 描述 |
| ruleConfig | 否 | string | 规则配置 |
| status | 否 | integer(int32) | 状态：1 启用，2 禁用 |
| type | 否 | string | 类型：1 上架，2 下架 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_rule对象

规则管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| actionIds | 否 | string | 策略动作id(id,id,id) |
| algorithmPackageBottom | 否 | string | 算法包(下架规则)：1 先进先出  2先进后出 |
| algorithmPackageTop | 否 | string | 算法包(上架规则)：1 先进先出  2先进后出 |
| conditionGroupCode | 否 | string |  |
| conditionalCombinationId | 否 | string | 关联条件组id |
| conditions | 否 | array<条件对象> |  |
| containerInitialize | 否 | string | 容器初始化 |
| containerStatus | 否 | string | 容器状态 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| customizedResults | 否 | string | 定制化结果id(id,id,id) |
| flowCardFlag | 否 | string | 流程卡标识新增（id,id,id |
| flowCardFlagCode | 否 | string |  |
| goodType | 否 | string |  |
| id | 否 | string | id |
| isReleaseContainer | 否 | string | 是否释放容器：1 是，2 否 |
| isTimeout | 否 | integer(int32) | 是否开启超时 1 是，2 否 |
| logicAreaCode | 否 | string |  |
| logicAreaId | 否 | string | 逻辑区id |
| logicAreaName | 否 | string |  |
| logicLocationStatus | 否 | string | 目标储位状态 |
| logicalAreaList | 否 | array<LogicalAreaIndex> |  |
| logicalAreaNames | 否 | string |  |
| pattern | 否 | string | 模式：1 上料，2 下料 |
| priority | 否 | integer(int32) | 优先级 |
| ruleCode | 否 | string | 规则编码 |
| ruleName | 否 | string | 规则名称 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleGroupId | 否 | string | 车辆分组id |

### tms_rule对象0

规则管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| actionIds | 否 | string | 策略动作id(id,id,id) |
| algorithmPackageBottom | 否 | string | 算法包(下架规则)：1 先进先出  2先进后出 |
| algorithmPackageTop | 否 | string | 算法包(上架规则)：1 先进先出  2先进后出 |
| conditionalCombinationId | 否 | string | 关联条件组id |
| containerInitialize | 否 | string | 容器初始化 |
| containerStatus | 否 | string | 容器状态 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| customizedResults | 否 | string | 定制化结果id(id,id,id) |
| flowCardFlag | 否 | string | 流程卡标识新增（id,id,id |
| goodType | 否 | string |  |
| id | 否 | string | id |
| isReleaseContainer | 否 | string | 是否释放容器：1 是，2 否 |
| isTimeout | 否 | integer(int32) | 是否开启超时 1 是，2 否 |
| logicAreaId | 否 | string | 逻辑区id |
| logicLocationStatus | 否 | string | 目标储位状态 |
| pattern | 否 | string | 模式：1 上料，2 下料 |
| priority | 否 | integer(int32) | 优先级 |
| ruleCode | 否 | string | 规则编码 |
| ruleName | 否 | string | 规则名称 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleGroupId | 否 | string | 车辆分组id |

### tms_send_http_log对象

tms_send_http_log

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| i18nCode | 否 | string |  |
| id | 否 | string | id |
| remark | 否 | string | 备注 |
| requestParams | 否 | string | 请求参数 |
| requestUrl | 否 | string | 请求地址 |
| returnedValue | 否 | string | 接口返回值 |
| taskId | 否 | string | 任务id |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

### tms_storage_cavern_type对象

储区类型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| equipmentDomain | 否 | string | 设备域名 |
| equipmentIp | 否 | string | 设备IP |
| equipmentPort | 否 | string | 设备端口 |
| id | 否 | string | id |
| remakr | 否 | string | 备注 |
| status | 否 | string | 状态：1 启用，2 禁用 |
| storageLocationTheir | 否 | string | 储位所属 1储区，2容器 |
| type | 否 | string | 类型：1 设备，2 人工 |
| typeCode | 否 | string | 库区类型编码 |
| typeName | 否 | string | 库区类型名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_storage_cavern对象

储区管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessId | 否 | string | 库区业务id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| id | 否 | string | id |
| singleOrDouble | 否 | string | 深度组方向：1 单向，2 双向 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | 否 | string | 库区编码 |
| storageCavernName | 否 | string | 库区名称 |
| storageCavernType | 否 | string | 库区类型 |
| typeName | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseCode | 否 | string |  |
| warehouseId | 否 | string | 仓库id |
| warehouseName | 否 | string |  |
| workshop | 否 | string |  |

### tms_storage_cavern对象0

储区管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessId | 否 | string | 库区业务id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| id | 否 | string | id |
| singleOrDouble | 否 | string | 深度组方向：1 单向，2 双向 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | 否 | string | 库区编码 |
| storageCavernName | 否 | string | 库区名称 |
| storageCavernType | 否 | string | 库区类型 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseId | 否 | string | 仓库id |
| workshop | 否 | string |  |

### tms_storage_cavern对象1

储区管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessId | 否 | string | 库区业务id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| id | 否 | string | id |
| singleOrDouble | 否 | string | 深度组方向：1 单向，2 双向 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | 否 | string | 库区编码 |
| storageCavernName | 否 | string | 库区名称 |
| storageCavernType | 否 | string | 库区类型 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseId | 否 | string | 仓库id |
| workshop | 否 | string |  |

### tms_storage_location_button对象

tms_storage_location_button

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| beeperIp | 否 | string | 按钮IP |
| buttonCode | 否 | string | 按钮编码 |
| buttonType | 否 | string | 按钮类型 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| materAreaCode | 否 | string | 区域编号 |
| storageLocationId | 否 | string | 库位id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_storage_location对象

储位管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| associativeContainerBindTime | 否 | string(date-time) | 关联容器的最新绑定时间 |
| associativeContainerUnbindTime | 否 | string(date-time) | 关联容器的最新解绑时间 |
| bay | 否 | string | BAY |
| businessId | 否 | string | 储位业务ID |
| cameraCode | 否 | string | 摄像头编码 |
| cavernBusinessId | 否 | string | 储区业务ID |
| channel | 否 | string | 通道 |
| columnNumber | 否 | integer(int32) | 列 |
| containerCode | 否 | string | 容器编码 |
| containerCodeList | 否 | string | 容器编码组 |
| containerId | 否 | string | 容器id |
| containerIdT | 否 | string |  |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| coordinateX | 否 | string | 坐标X |
| coordinateY | 否 | string | 坐标y |
| coordinateZ | 否 | string | 坐标z |
| cover | 否 | string | 面 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deep | 否 | string | 深 |
| deliveryTime | 否 | string(date-time) | 放货时间 |
| depthCode | 否 | string | 深度组编码 |
| depthDirection | 否 | string | 深度组方向：1 单向，2 双向 |
| depthOne | 否 | integer(int32) | 深度组1 |
| depthTwo | 否 | integer(int32) | 深度组2 |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flag | 否 | string | 标识 |
| flag2 | 否 | string | 标识2 |
| hitTheShelfOrder | 否 | integer(int32) | 上架顺序 |
| id | 否 | string | id |
| isFreeze | 否 | string | 是否冻结：1 冻结，2 没冻结 |
| isGenerateQrCode | 否 | string | 是否生成储位码：1 不生成，2 生成 |
| isRetainContainer | 否 | string | 是否保留容器：1 是，2 否 |
| isScanOrCheck | 否 | string | 是否扫描校验：1 是，2 否 |
| lattice | 否 | string | 格 |
| length | 否 | string | 长 |
| maximumBoxQuantity | 否 | integer(int32) | 最大箱数量 |
| maximumCubage | 否 | string | 最大容积 |
| maximumLoadBearing | 否 | string | 最大承重 |
| maximumTrayQuantity | 否 | integer(int32) | 最大托盘数量 |
| mixedBatchQuantity | 否 | integer(int32) | 混放批次数量 |
| mixedQuantity | 否 | integer(int32) | 混放数量 |
| onlyGodKnows | 否 | string |  |
| residueBoxQuantity | 否 | integer(int32) | 剩余箱数量 |
| residueTrayQuantity | 否 | integer(int32) | 剩余托盘数量 |
| restrictionRule | 否 | string | 限制规则 |
| rowNumber | 否 | integer(int32) | 行 |
| soldOutOrder | 否 | integer(int32) | 下架顺序 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | 否 | string | 储区编码 |
| storageCavernId | 否 | string | 储区id |
| storageCavernName | 否 | string | 储区名称 |
| storageLocationCode | 否 | string | 储位编码 |
| storageLocationName | 否 | string | 储位名称 |
| storageLocationQrCode | 否 | string | 储位二维码 |
| storageLocationStatus | 否 | string | 储位状态：0 占用，1 空闲，2 预占，3 超时 |
| storageLocationTheir | 否 | string | 储位所属：库区类型选择容器区，储位所属默认未容器 |
| storageLocationTheir1 | 否 | string |  |
| storageLocationType | 否 | string | 储位类型编码 |
| tier | 否 | string | 层 |
| typeName | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| volumeVacancyRate | 否 | string | 体积空置率 |
| warehouseCode | 否 | string | 仓库编码 |
| warehouseId | 否 | string | 仓库id |
| warehouseName | 否 | string | 仓库名称 |
| weightVacancyRate | 否 | string | 重量空置率 |
| width | 否 | string | 宽 |

### tms_storage_location对象0

tms_storage_location

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| associativeContainerBindTime | 否 | string(date-time) | 关联容器的最新绑定时间 |
| associativeContainerUnbindTime | 否 | string(date-time) | 关联容器的最新解绑时间 |
| bay | 否 | string | BAY |
| businessId | 否 | string | 业务ID, 与其他系统对接储位信息 |
| cameraCode | 否 | string | 摄像头编码 |
| channel | 否 | string | 通道 |
| columnNumber | 否 | integer(int32) | 列 |
| containerId | 否 | string | 容器id |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| coordinateX | 否 | string | 坐标X |
| coordinateY | 否 | string | 坐标y |
| coordinateZ | 否 | string | 坐标z |
| cover | 否 | string | 面 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deep | 否 | string | 深 |
| deliveryTime | 否 | string(date-time) | 放货时间 |
| flag | 否 | string | 标识 |
| flag2 | 否 | string | 标识2 |
| id | 否 | string | id |
| isFreeze | 否 | string | 是否冻结：1 冻结，2 没冻结 |
| isGenerateQrCode | 否 | string | 是否生成储位码：1 不生成，2 生成 |
| isRetainContainer | 否 | string | 是否保留容器：1 是，2 否 |
| isScanOrCheck | 否 | string | 是否扫描校验：1 是，2 否 |
| lattice | 否 | string | 格 |
| length | 否 | string | 长 |
| maximumBoxQuantity | 否 | integer(int32) | 最大箱数量 |
| maximumCubage | 否 | string | 最大容积 |
| maximumLoadBearing | 否 | string | 最大承重 |
| maximumTrayQuantity | 否 | integer(int32) | 最大托盘数量 |
| mixedBatchQuantity | 否 | integer(int32) | 混放批次数量 |
| mixedQuantity | 否 | integer(int32) | 混放数量 |
| residueBoxQuantity | 否 | integer(int32) | 剩余箱数量 |
| residueTrayQuantity | 否 | integer(int32) | 剩余托盘数量 |
| restrictionRule | 否 | string | 限制规则 |
| rowNumber | 否 | integer(int32) | 行 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernId | 否 | string | 储区id |
| storageLocationCode | 否 | string | 储位编码 |
| storageLocationName | 否 | string | 储位名称 |
| storageLocationQrCode | 否 | string | 储位二维码 |
| storageLocationStatus | 否 | string | 储位状态：0 占用，1 空闲，2 预占，3 超时 |
| storageLocationTheir | 否 | string | 储位所属：库区类型选择容器区，储位所属默认未容器 |
| storageLocationType | 否 | string | 储位类型编码 |
| tier | 否 | string | 层 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| volumeVacancyRate | 否 | string | 体积空置率 |
| warehouseId | 否 | string | 仓库id |
| weightVacancyRate | 否 | string | 重量空置率 |
| width | 否 | string | 宽 |

### tms_storage_location对象1

储位管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| associativeContainerBindTime | 否 | string(date-time) | 关联容器的最新绑定时间 |
| associativeContainerUnbindTime | 否 | string(date-time) | 关联容器的最新解绑时间 |
| bay | 否 | string | BAY |
| businessId | 否 | string | 储位业务ID |
| cameraCode | 否 | string | 摄像头编码 |
| cavernBusinessId | 否 | string | 储区业务ID |
| channel | 否 | string | 通道 |
| columnNumber | 否 | integer(int32) | 列 |
| containerCode | 否 | string | 容器编码 |
| containerCodeList | 否 | string | 容器编码组 |
| containerId | 否 | string | 容器id |
| containerIdT | 否 | string |  |
| containerQuantity | 否 | integer(int32) | 容器数量 |
| coordinateX | 否 | string | 坐标X |
| coordinateY | 否 | string | 坐标y |
| coordinateZ | 否 | string | 坐标z |
| cover | 否 | string | 面 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| deep | 否 | string | 深 |
| deliveryTime | 否 | string(date-time) | 放货时间 |
| depthCode | 否 | string | 深度组编码 |
| depthDirection | 否 | string | 深度组方向：1 单向，2 双向 |
| depthOne | 否 | integer(int32) | 深度组1 |
| depthTwo | 否 | integer(int32) | 深度组2 |
| direction | 否 | string | 取放货方向：1 单进单出，2 双进双出，3 一边进一边出 |
| flag | 否 | string | 标识 |
| flag2 | 否 | string | 标识2 |
| hitTheShelfOrder | 否 | integer(int32) | 上架顺序 |
| id | 否 | string | id |
| isFreeze | 否 | string | 是否冻结：1 冻结，2 没冻结 |
| isGenerateQrCode | 否 | string | 是否生成储位码：1 不生成，2 生成 |
| isRetainContainer | 否 | string | 是否保留容器：1 是，2 否 |
| isScanOrCheck | 否 | string | 是否扫描校验：1 是，2 否 |
| lattice | 否 | string | 格 |
| length | 否 | string | 长 |
| maximumBoxQuantity | 否 | integer(int32) | 最大箱数量 |
| maximumCubage | 否 | string | 最大容积 |
| maximumLoadBearing | 否 | string | 最大承重 |
| maximumTrayQuantity | 否 | integer(int32) | 最大托盘数量 |
| mixedBatchQuantity | 否 | integer(int32) | 混放批次数量 |
| mixedQuantity | 否 | integer(int32) | 混放数量 |
| onlyGodKnows | 否 | string |  |
| residueBoxQuantity | 否 | integer(int32) | 剩余箱数量 |
| residueTrayQuantity | 否 | integer(int32) | 剩余托盘数量 |
| restrictionRule | 否 | string | 限制规则 |
| rowNumber | 否 | integer(int32) | 行 |
| soldOutOrder | 否 | integer(int32) | 下架顺序 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageCavernCode | 否 | string | 储区编码 |
| storageCavernId | 否 | string | 储区id |
| storageCavernName | 否 | string | 储区名称 |
| storageLocationCode | 否 | string | 储位编码 |
| storageLocationName | 否 | string | 储位名称 |
| storageLocationQrCode | 否 | string | 储位二维码 |
| storageLocationStatus | 否 | string | 储位状态：0 占用，1 空闲，2 预占，3 超时 |
| storageLocationTheir | 否 | string | 储位所属：库区类型选择容器区，储位所属默认未容器 |
| storageLocationTheir1 | 否 | string |  |
| storageLocationType | 否 | string | 储位类型编码 |
| tier | 否 | string | 层 |
| typeName | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| volumeVacancyRate | 否 | string | 体积空置率 |
| warehouseCode | 否 | string | 仓库编码 |
| warehouseId | 否 | string | 仓库id |
| warehouseName | 否 | string | 仓库名称 |
| weightVacancyRate | 否 | string | 重量空置率 |
| width | 否 | string | 宽 |

### tms_strategy_action对象

tms_strategy_action

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| broadcastSpeechId | 否 | string | 广播语ID |
| businessStatus | 否 | string | 业务状态：0 可用(该容器可被业务分配)，1 占用(该容器已被业务占用)，2 禁用(该容器号已不可被使用) |
| containerStatus | 否 | string | 容器状态：0 空，1 满，2 满+1 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endStorageLocationStatus | 否 | string | 终点库位状态：0 占用，1 空闲，2 锁定 |
| id | 否 | string | id |
| routerWeight | 否 | integer(int32) | 路由权重 |
| startStorageLocationStatus | 否 | string | 起点库位状态：0 占用，1 空闲，2 锁定 |
| strategyId | 否 | string | 策略ID |
| taskStatus | 否 | string | 任务状态：10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| templateName | 否 | string |  |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_strategy对象

tms_strategy

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| actions | 否 | array<tms_strategy_action对象> |  |
| containerInitStatus | 否 | string | 容器初始状态：0 空，1 满，2 满+1 |
| createBy | 否 | string | 创建人 |
| createContainer | 否 | string | 是否创建容器：1 创建，2 不创建 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagOne | 否 | string | 标识1 |
| flageTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 启用，2 禁用 |
| strategyCode | 否 | string | 策略编码 |
| strategyName | 否 | string | 策略名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_strategy对象0

tms_strategy

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerInitStatus | 否 | string | 容器初始状态：0 空，1 满，2 满+1 |
| createBy | 否 | string | 创建人 |
| createContainer | 否 | string | 是否创建容器：1 创建，2 不创建 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagOne | 否 | string | 标识1 |
| flageTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 启用，2 禁用 |
| strategyCode | 否 | string | 策略编码 |
| strategyName | 否 | string | 策略名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_strategy对象1

tms_strategy

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| actions | 否 | array<tms_strategy_action对象> |  |
| containerInitStatus | 否 | string | 容器初始状态：0 空，1 满，2 满+1 |
| createBy | 否 | string | 创建人 |
| createContainer | 否 | string | 是否创建容器：1 创建，2 不创建 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagOne | 否 | string | 标识1 |
| flageTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| status | 否 | string | 状态：1 启用，2 禁用 |
| strategyCode | 否 | string | 策略编码 |
| strategyName | 否 | string | 策略名称 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_task_abnormal对象

异常信息管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| abnormalFlag | 否 | string |  |
| abnormalType | 否 | string | 异常类型 |
| beginTime | 否 | string(date-time) | 告警开始时间 |
| businessConfigId | 否 | string | 业务配置ID |
| code | 否 | string | 异常记录编码 |
| containerId | 否 | string | 容器ID |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endStorageLocationId | 否 | string | 终点储位编码 |
| equipmentCoding | 否 | string | 设备编码：呼叫器为IP+区域，车辆为车辆编号 |
| id | 否 | string | id |
| object | 否 | string | 报警对象 |
| remark | 否 | string |  |
| startStorageLocationId | 否 | string | 起始储位ID |
| taskCode | 否 | string | 任务编码 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warnContent | 否 | string | 告警内容 |

### tms_task_poll_status对象

tms_task_poll_status

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskPollId | 否 | string | TMS任务id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_task_poll对象

TMS任务组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| conditionalCombinationId | 否 | string | 条件组id |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endLocationId | 否 | string | 目标点位id |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleId | 否 | string | 规则ID |
| startLocationId | 否 | string | 起始点位id |
| status | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | 否 | string | 任务编号 |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPollId | 否 | string | 任务池id |
| taskPriority | 否 | string | 任务优先级 |
| taskSource | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string | 执行车辆编号 |

### tms_task_poll对象0

TMS任务组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| buttonCode | 否 | string | 按钮编码 |
| conditionalCombinationCode | 否 | string |  |
| conditionalCombinationId | 否 | string | 条件组id |
| containerCode | 否 | string |  |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| dispatch | 否 | string | 是否调度：1 未调度，2已调度 |
| endCavernCode | 否 | string |  |
| endCavernName | 否 | string |  |
| endLocationCode | 否 | string |  |
| endLocationId | 否 | string | 目标点位id |
| endLocationName | 否 | string |  |
| goodType | 否 | string | 货型 |
| groupStatus | 否 | string | 任务组状态：10 创建，20 进行中，50 完成，60 取消，80 终止 |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleCode | 否 | string |  |
| ruleId | 否 | string | 规则ID |
| ruleName | 否 | string |  |
| startCavernCode | 否 | string |  |
| startCavernName | 否 | string |  |
| startLocationCode | 否 | string |  |
| startLocationId | 否 | string | 起始点位id |
| startLocationName | 否 | string |  |
| status | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskCode | 否 | string | 任务编号 |
| taskMode | 否 | string |  |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPriority | 否 | string | 优先级 |
| taskSource | 否 | string | 任务来源 |
| taskType | 否 | string | 任务类型 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_task_poll对象1

TMS任务组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| buttonCode | 否 | string | 按钮编码 |
| conditionalCombinationId | 否 | string | 条件组id |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| dispatch | 否 | string | 是否调度：1 未调度，2已调度 |
| endLocationId | 否 | string | 目标点位id |
| goodType | 否 | string | 货型 |
| groupStatus | 否 | string | 任务组状态：10 创建，20 进行中，50 完成，60 取消，80 终止 |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleId | 否 | string | 规则ID |
| startLocationId | 否 | string | 起始点位id |
| status | 否 | string | 任务状态 10 创建，20 待执行，30 执行中，40 已离开，50 已完成，60 已取消，70 异常 |
| taskCode | 否 | string | 任务编号 |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPriority | 否 | string | 优先级 |
| taskSource | 否 | string | 任务来源 |
| taskType | 否 | string | 任务类型 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_task_type_range对象

tms_task_type_range

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isShow | 否 | string | 是否PDA显示：1 是，2 否 |
| logicalAreaTagIds | 否 | string | 逻辑区标签ID组 |
| rangeCode | 否 | string | 范围编码 |
| rangeName | 否 | string | 范围名称 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationIds | 否 | string | 逻辑包含库位ID组 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| userIds | 否 | string | 用户ID组 |

### tms_task_type_range对象0

tms_task_type_range

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| logicalAreaTagIds | 否 | string | 逻辑区标签ID组 |
| logicalAreaTagNames | 否 | string | 逻辑区标签名称组 |
| rangeCode | 否 | string | 范围编码 |
| rangeName | 否 | string | 范围名称 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationCode | 否 | string | 逻辑包含库位编码组 |
| storageLocationCodes | 否 | string | 逻辑包含库位编码组 |
| storageLocationIds | 否 | string | 逻辑包含库位ID组 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| userIds | 否 | string | 用户Ids |

### tms_task_type_range对象1

tms_task_type_range

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| logicalAreaTagIds | 否 | string | 逻辑区标签ID组 |
| logicalAreaTagNames | 否 | string | 逻辑区标签名称组 |
| rangeCode | 否 | string | 范围编码 |
| rangeName | 否 | string | 范围名称 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationCode | 否 | string | 逻辑包含库位编码组 |
| storageLocationCodes | 否 | string | 逻辑包含库位编码组 |
| storageLocationIds | 否 | string | 逻辑包含库位ID组 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| userIds | 否 | string | 用户Ids |

### tms_task_type_route对象

任务类型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| name | 否 | string | 名称由电梯+路由组成 |
| type | 否 | string | 类型 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### tms_task_type对象

任务类型管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| currentStorageLocationCodes | 否 | string |  |
| id | 否 | string | id |
| isOpenTime | 否 | string |  |
| isOpenTiming | 否 | string | 是否开启定时 |
| isReleaseContainer | 否 | string | 是否释放容器：1 释放，2 不释放 |
| priority | 否 | integer(int32) | 优先级 |
| rangeCode | 否 | string |  |
| rangeId | 否 | string | 范围ID |
| rangeName | 否 | string |  |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationIds | 否 | string | 所触发的库位ID组 |
| taskTypeCode | 否 | string | 任务类型编码 |
| taskTypeName | 否 | string | 任务类型名称 |
| taskTypePattern | 否 | string | 任务类型模式：1 呼料，2 叫料 |
| timeOutPeriod | 否 | integer(int32) | 超时时间,秒 |
| triggeringCondition | 否 | string | 触发条件(json) |
| triggeringCondition1 | 否 | TriggeringCondition |  |
| triggeringSwitch | 否 | string | 触发开关(json) |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleScope | 否 | string | 车辆可选范围 |

### tms_task_type对象0

tms_task_type

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| isOpenTiming | 否 | string | 是否开启定时 |
| isReleaseContainer | 否 | string | 是否释放容器：1 释放，2 不释放 |
| priority | 否 | integer(int32) | 优先级 |
| rangeId | 否 | string | 范围ID |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationIds | 否 | string | 所触发的库位ID组 |
| taskTypeCode | 否 | string | 任务类型编码 |
| taskTypeName | 否 | string | 任务类型名称 |
| taskTypePattern | 否 | string | 任务类型模式：1 呼料，2 叫料 |
| timeOutPeriod | 否 | integer(int32) | 超时时间,秒 |
| triggeringCondition | 否 | string | 触发条件(json) |
| triggeringSwitch | 否 | string | 触发开关(json) |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleScope | 否 | string | 车辆可选范围 |

### tms_task_type对象1

任务类型管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| currentStorageLocationCodes | 否 | string |  |
| id | 否 | string | id |
| isOpenTime | 否 | string |  |
| isOpenTiming | 否 | string | 是否开启定时 |
| isReleaseContainer | 否 | string | 是否释放容器：1 释放，2 不释放 |
| priority | 否 | integer(int32) | 优先级 |
| rangeCode | 否 | string |  |
| rangeId | 否 | string | 范围ID |
| rangeName | 否 | string |  |
| status | 否 | string | 状态：1 正常，2 禁用 |
| storageLocationIds | 否 | string | 所触发的库位ID组 |
| taskTypeCode | 否 | string | 任务类型编码 |
| taskTypeName | 否 | string | 任务类型名称 |
| taskTypePattern | 否 | string | 任务类型模式：1 呼料，2 叫料 |
| timeOutPeriod | 否 | integer(int32) | 超时时间,秒 |
| triggeringCondition | 否 | string | 触发条件(json) |
| triggeringCondition1 | 否 | TriggeringCondition |  |
| triggeringSwitch | 否 | string | 触发开关(json) |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleScope | 否 | string | 车辆可选范围 |

### tms_task_upstream对象

TMS上游任务池

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| conditionalCombinationCode | 否 | string |  |
| conditionalCombinationId | 否 | string | 条件组id |
| containerCode | 否 | string |  |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endCavernCode | 否 | string |  |
| endCavernName | 否 | string |  |
| endLocationCode | 否 | string |  |
| endLocationId | 否 | string | 目标点位id |
| endLocationName | 否 | string |  |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleCode | 否 | string |  |
| ruleId | 否 | string | 规则ID |
| ruleName | 否 | string |  |
| startCavernCode | 否 | string |  |
| startCavernName | 否 | string |  |
| startLocationCode | 否 | string |  |
| startLocationId | 否 | string | 起始点位id |
| startLocationName | 否 | string |  |
| status | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | 否 | string | 任务编号 |
| taskMode | 否 | string |  |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPollId | 否 | string | 任务池id |
| taskPriority | 否 | string | 任务优先级 |
| taskSource | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string | 执行车辆编号 |
| vehicleId | 否 | string |  |
| vehicleTypeCode | 否 | string |  |
| vehicleTypeName | 否 | string |  |

### tms_task对象

tms_task

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| conditionalCombinationCode | 否 | string |  |
| conditionalCombinationId | 否 | string | 条件组id |
| containerCode | 否 | string |  |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endCavernCode | 否 | string |  |
| endCavernName | 否 | string |  |
| endLocationCode | 否 | string |  |
| endLocationId | 否 | string | 目标点位id |
| endLocationName | 否 | string |  |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleCode | 否 | string |  |
| ruleId | 否 | string | 规则ID |
| ruleName | 否 | string |  |
| startCavernCode | 否 | string |  |
| startCavernName | 否 | string |  |
| startLocationCode | 否 | string |  |
| startLocationId | 否 | string | 起始点位id |
| startLocationName | 否 | string |  |
| status | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | 否 | string | 任务编号 |
| taskMode | 否 | string |  |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPollId | 否 | string | 任务池id |
| taskPriority | 否 | string | 任务优先级 |
| taskSource | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string |  |
| vehicleId | 否 | string |  |
| vehicleTypeCode | 否 | string |  |
| vehicleTypeName | 否 | string |  |

### tms_task对象0

tms_task

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| conditionalCombinationId | 否 | string | 条件组id |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endLocationId | 否 | string | 目标点位id |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleId | 否 | string | 规则ID |
| startLocationId | 否 | string | 起始点位id |
| status | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | 否 | string | 任务编号 |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPollId | 否 | string | 任务池id |
| taskPriority | 否 | string | 任务优先级 |
| taskSource | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string | 执行车辆编号 |

### tms_task对象1

tms_task

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessConfigId | 否 | string | 业务配置ID |
| conditionalCombinationId | 否 | string | 条件组id |
| containerId | 否 | string | 容器id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endLocationId | 否 | string | 目标点位id |
| id | 否 | string | id |
| isException | 否 | integer(int32) | 是否异常 1是 2否 |
| issueTime | 否 | string(date-time) | 任务下发时间 |
| pidCode | 否 | string | 任务父编号 |
| ruleId | 否 | string | 规则ID |
| startLocationId | 否 | string | 起始点位id |
| status | 否 | string | 任务状态 0 制单中，1 已制单，2 执行中，4 已取消,5 已完成 |
| taskCode | 否 | string | 任务编号 |
| taskOverTime | 否 | string(date-time) | 任务完成时间 |
| taskPollId | 否 | string | 任务池id |
| taskPriority | 否 | string | 任务优先级 |
| taskSource | 否 | string | 任务来源 1 分切按钮，2 按钮A， 3 按钮B |
| taskType | 否 | string | 任务类型 1 分切机台下料，2 分切太送空，3 普通前往待命点，4 普通前往下一机台，5 打包台6任务类型1， 7 打包台6任务类型2 |
| taskTypeId | 否 | string | 任务类型id |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string | 执行车辆编号 |

### tms_vehicle_group对象

车辆分组管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 状态 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleGroupCode | 否 | string | 车辆分组编码 |
| vehicleGroupName | 否 | string | 车辆分组 |

### tms_vehicle_type对象

车型管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| status | 否 | string | 状态 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleTypeCode | 否 | string | 车型编码 |
| vehicleTypeName | 否 | string | 车型名称 |

### tms_vehicle对象

车辆管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| mapCode | 否 | string | 车辆所在地图 |
| posX | 否 | string | 车辆X坐标 |
| posY | 否 | string | 车辆Y坐标 |
| runStatus | 否 | string | 车辆运行状态 |
| status | 否 | string | 状态 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| vehicleCode | 否 | string | 车辆编码 |
| vehicleGroupCodes | 否 | string |  |
| vehicleGroupId | 否 | string | 车辆分组 |
| vehicleGroupName | 否 | string | 车辆分组 |
| vehicleKw | 否 | string | 车辆电量 |
| vehicleSource | 否 | string | 车辆来源 |
| vehicleTypeCode | 否 | string | 车辆类型编码 |
| vehicleTypeId | 否 | string | 车型 |
| vehicleTypeName | 否 | string | 车辆类型名称 |

### tms_warehouse对象

仓库管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| contacts | 否 | string | 联系人 |
| contactsNumber | 否 | string | 联系电话 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | 主键 |
| status | 否 | string | 状态：1 正常，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| warehouseAddress | 否 | string | 仓库地址 |
| warehouseCode | 否 | string | 仓库编码 |
| warehouseName | 否 | string | 仓库名称 |

### tms_work_order对象

工单管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：1 开始，2 完工 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endTime | 否 | string |  |
| flagEight | 否 | string | 标识8 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| processCodeGroup | 否 | string | 工序组（工艺路线）code |
| processRouteCode | 否 | string |  |
| processRouteId | 否 | string | 工艺路线ID |
| startTime | 否 | string |  |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderNumber | 否 | string | 工单号 |

### tms_work_order对象0

工单管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：1 开始，2 完工 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| flagEight | 否 | string | 标识8 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| processRouteId | 否 | string | 工艺路线ID |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderNumber | 否 | string | 工单号 |

### tms_work_order对象1

工单管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string | 业务状态：1 开始，2 完工 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| endTime | 否 | string |  |
| flagEight | 否 | string | 标识8 |
| flagFive | 否 | string | 标识5 |
| flagFour | 否 | string | 标识4 |
| flagNine | 否 | string | 标识9 |
| flagOne | 否 | string | 标识1 |
| flagSeven | 否 | string | 标识7 |
| flagSix | 否 | string | 标识6 |
| flagTen | 否 | string | 标识10 |
| flagThree | 否 | string | 标识3 |
| flagTwo | 否 | string | 标识2 |
| id | 否 | string | id |
| materialCode | 否 | string | 物料编码 |
| materialName | 否 | string | 物料名称 |
| processCodeGroup | 否 | string | 工序组（工艺路线）code |
| processRouteCode | 否 | string |  |
| processRouteId | 否 | string | 工艺路线ID |
| startTime | 否 | string |  |
| status | 否 | string | 状态：1 启用，2 禁用 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |
| workOrderNumber | 否 | string | 工单号 |

### TmsDemandPollVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| cancelTime | 否 | string(date-time) |  |
| category | 否 | string |  |
| commandSourceSystem | 否 | string |  |
| containerCode | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| currentCavernCode | 否 | string |  |
| currentCavernName | 否 | string |  |
| currentLocCode | 否 | string |  |
| currentLogicalCode | 否 | string |  |
| currentLogicalName | 否 | string |  |
| demandId | 否 | string |  |
| flagEight | 否 | string |  |
| flagEleven | 否 | string |  |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagNine | 否 | string |  |
| flagOne | 否 | string |  |
| flagSeven | 否 | string |  |
| flagSix | 否 | string |  |
| flagTen | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwelve | 否 | string |  |
| flagTwo | 否 | string |  |
| flowCardNo | 否 | string |  |
| goodsTypeCode | 否 | string |  |
| pattern | 否 | string |  |
| priority | 否 | integer(int32) |  |
| status | 否 | string |  |
| targetCavernCode | 否 | string |  |
| targetCavernName | 否 | string |  |
| targetLocCode | 否 | string |  |
| targetLogicalAreaCode | 否 | string |  |
| targetLogicalCode | 否 | string |  |
| targetLogicalName | 否 | string |  |
| targetStorageLocationCode | 否 | string |  |
| taskType | 否 | string |  |
| updateTime | 否 | string(date-time) |  |
| upstreamTaskNo | 否 | string |  |
| workOrderNo | 否 | string |  |

### TmsLocStatement

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| cavernCode | 否 | string |  |
| containerCode | 否 | string |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| depthCode | 否 | string |  |
| flagEight | 否 | string |  |
| flagEleven | 否 | string |  |
| flagFive | 否 | string |  |
| flagFour | 否 | string |  |
| flagNine | 否 | string |  |
| flagOne | 否 | string |  |
| flagSeven | 否 | string |  |
| flagSix | 否 | string |  |
| flagTen | 否 | string |  |
| flagThree | 否 | string |  |
| flagTwelve | 否 | string |  |
| flagTwo | 否 | string |  |
| flowCardNo | 否 | string |  |
| id | 否 | string | 储位ID |
| ids | 否 | array<string> |  |
| locBusinessStatus | 否 | string |  |
| locCode | 否 | string |  |
| locStatus | 否 | string |  |
| locType | 否 | string |  |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |
| warehouseCode | 否 | string |  |
| workOrderNo | 否 | string |  |

### TriggeringCondition

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerStatus | 否 | string |  |
| ec | 否 | string |  |
| endLocationStatus | 否 | string |  |
| se | 否 | string |  |
| startLocationStatus | 否 | string |  |

