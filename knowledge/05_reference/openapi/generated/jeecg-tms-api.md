# TMS 对外及终端接口明细

> 来源：`../raw/jeecg-tms-api.swagger.json`。本文由生成器自动生成，请勿手工修改生成区内容。

## 服务信息

- 服务标识：`jeecg-tms-api`
- 网关地址：`http://111.160.91.170:59999`
- Base Path：`/jeecg-tms-api`
- 鉴权头：`X-Access-Token`
- 路径数：109
- 接口操作数：109
- 数据模型数：101

## 控制器索引

| 控制器/标签 | 接口数 |
|---|---:|
| 储位 - Controller | 1 |
| 储位历史记录 - Controller | 3 |
| 大屏接口 | 1 |
| 点对区 - Controller | 5 |
| 海康小车相关接口 | 5 |
| 货型管理 - Controller | 1 |
| 逻辑区 - Controller | 1 |
| 逻辑区标签 - Controller | 1 |
| 企微消息校验 | 1 |
| 事件接口 | 1 |
| 提升机相关接口 | 6 |
| 未来小车相关接口 | 2 |
| 小车相关接口 | 1 |
| 校验规则 - Controller | 2 |
| AGV开关门回调任务 | 1 |
| MES-Controller | 13 |
| Pad-点对点 | 5 |
| Pad-Controller | 28 |
| Pda-Controller | 8 |
| Test-Controller | 15 |
| test-modbus | 3 |
| WCS-Controller | 2 |
| WMS-Controller | 3 |

## 接口清单

### 储位 - Controller

#### GET /jeecg-tms-api/tms/api/pad/getLocationByLogicalAreaId/{logicalAreaId}

- 名称：根据逻辑区ID获取所有储位
- Operation ID：`getLocationByLogicalAreaIdUsingGET_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| logicalAreaId | path | 是 | string | logicalAreaId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«List«LocationVO»»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 储位历史记录 - Controller

#### POST /jeecg-tms-api/tms/api/pad/addGoodsTypeHistoryRecord

- 名称：保存用户历史选择的货型
- Operation ID：`addGoodsTypeHistoryRecordUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| addHistoryRecordList | body | 是 | array<AddHistoryRecord> | addHistoryRecordList |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/addHistoryRecord

- 名称：保存用户历史选择库位
- Operation ID：`addHistoryRecordUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| addHistoryRecordList | body | 是 | array<AddHistoryRecord> | addHistoryRecordList |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getHistoryRecord

- 名称：获取用户历史选择库位
- Operation ID：`getHistoryRecordUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| source | query | 是 | string | source |
| userId | query | 是 | string | userId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«Map«string,List«HistoryRecordVO»»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 大屏接口

#### GET /jeecg-tms-api/tms/api/screen/getStorageCavernData

- 名称：获取大屏数据
- Operation ID：`getStorageCavernDataUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| name | query | 否 | string | name |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«StorageCavernVo»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 点对区 - Controller

#### POST /jeecg-tms-api/tms/api/pad/pointToAreaBindTask

- 名称：点对区(绑定)任务下发
- Operation ID：`pointToAreaBindTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pointToAreaTaskVO | body | 是 | 点对区任务下发VO对象 | pointToAreaTaskVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pointToAreaColumnSelectValidate

- 名称：点对区(绑定)列选储位校验
- Operation ID：`pointToAreaColumnSelectValidateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| depthGroupCodes | body | 是 | array<string> | depthGroupCodes |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pointToAreaLocationValidate

- 名称：点对区(绑定)确定储位校验
- Operation ID：`pointToAreaLocationValidateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCodes | body | 是 | array<string> | locationCodes |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pointToAreaSelectValidate

- 名称：点对区(绑定)选择储位
- Operation ID：`pointToAreaSelectValidateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pointToAreaLocationValidateVo | body | 是 | 点对区选择储位校验参数 | pointToAreaLocationValidateVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pointToAreaTask

- 名称：点对区任务下发
- Operation ID：`pointToAreaTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pointToAreaTaskVO | body | 是 | 点对区任务下发VO对象 | pointToAreaTaskVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 海康小车相关接口

#### POST /jeecg-tms-api/service/rest/agvCallbackService/warnCallback

- 名称：AGV异常回调任务
- Operation ID：`agvErrorCallbackUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| agvErrorCallbackDTO | body | 是 | AgvErrorCallbackDTO | agvErrorCallbackDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | AgvResultDTO«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/agv/agvCallback

- 名称：海康AGV回调任务
- Operation ID：`agvCallbackFunctionUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| callbackDto | body | 是 | CallbackDTO | callbackDto |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | AgvResultDTO«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/agv/notifyTrafficTask

- 名称：RCS申请交通管制
- Operation ID：`notifyTrafficTaskUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| rcsNotifyTrafficTaskDTO | body | 是 | RcsNotifyTrafficTaskDTO | rcsNotifyTrafficTaskDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | AgvResultDTO«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/agv/readModbus

- 名称：读Modbus
- Operation ID：`notifyTrafficTaskUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| functionCode | query | 否 | string | functionCode |
| ip | query | 否 | string | ip |
| offset | query | 否 | integer(int32) | offset |
| port | query | 否 | integer(int32) | port |
| slaveId | query | 否 | integer(int32) | slaveId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/agv/writeModbus

- 名称：写Modbus
- Operation ID：`notifyTrafficTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| functionCode | query | 否 | string | functionCode |
| ip | query | 否 | string | ip |
| numberValue | query | 否 | integer(int32) | numberValue |
| offset | query | 否 | integer(int32) | offset |
| port | query | 否 | integer(int32) | port |
| slaveId | query | 否 | integer(int32) | slaveId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 货型管理 - Controller

#### GET /jeecg-tms-api/tms/api/pad/getGoodsTypeList

- 名称：获取货型列表
- Operation ID：`getLocationByLogicalAreaIdUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«GoodsTypeVO»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 逻辑区 - Controller

#### GET /jeecg-tms-api/tms/api/pad/getLogicalAreaByTagId/{tagId}

- 名称：根据逻辑区标签ID获取该标签下的逻辑区
- Operation ID：`getLogicalAreaByTagIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tagId | path | 是 | string | tagId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«LogicalAreaVO»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 逻辑区标签 - Controller

#### GET /jeecg-tms-api/tms/api/pad/getLogicalAreaTagList

- 名称：获取逻辑区标签接口
- Operation ID：`getLogicalAreaTagListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«LogicalAreaTagVO»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 企微消息校验

#### GET /jeecg-tms-api/tms/api/wx/message

- 名称：企微接收消息API
- Operation ID：`verifyMessageUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | - | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 事件接口

#### POST /jeecg-tms-api/tms/api/event

- 名称：事件触发
- Operation ID：`processHandlerUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| task | body | 是 | tms_task对象 | task |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 提升机相关接口

#### POST /jeecg-tms-api/tms/api/wcs/alarmCallback

- 名称：异常报警反馈
- Operation ID：`alarmCallbackUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| alarmCode | query | 否 | string | - |
| alarmMessage | query | 否 | string | - |
| containerCode | query | 否 | string | - |
| locationId | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/elevator/test/callDown

- 名称：测试-提升机下呼
- Operation ID：`testCallDownUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | query | 否 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/elevator/test/callUp

- 名称：测试-提升机上呼
- Operation ID：`testCallUpUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | query | 否 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/elevator/test/closeDoor

- 名称：测试-提升机关门
- Operation ID：`testCloseDoorUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | query | 否 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/elevator/test/isAtFloor

- 名称：测试-提升机是否在某层
- Operation ID：`testIsAtFloorUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| floor | query | 否 | integer(int32) | floor |
| locationCode | query | 否 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/elevatorCallback

- 名称：提升机回告
- Operation ID：`agvCallbackFunctionUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsCallBackDto | body | 是 | TmsCallBackDto | tmsCallBackDto |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 未来小车相关接口

#### POST /jeecg-tms-api/tms/api/agv/visAgvCallback

- 名称：未来AGV回调任务
- Operation ID：`agvCallbackFunctionUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| visionnavCallbackDTO | body | 是 | VisionnavCallbackDTO | visionnavCallbackDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/agv/visWarnCallback

- 名称：AGV异常回调任务
- Operation ID：`agvErrorCallbackUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| agvErrorCallbackDTO | body | 是 | AgvErrorCallbackDTO | agvErrorCallbackDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | AgvResultDTO«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 小车相关接口

#### GET /jeecg-tms-api/tms/api/large/screen/getAgvStatus

- 名称：AGV小车视图
- Operation ID：`getAgvStatusUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pageNum | query | 否 | integer(int32) | pageNum |
| pageSize | query | 否 | integer(int32) | pageSize |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«Page«AgvStatusVo»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 校验规则 - Controller

#### GET /jeecg-tms-api/tms/api/pad/checkStorageLocationForGroup/{locationCode}

- 名称：校验集团取货规则2
- Operation ID：`getLocationByLogicalAreaIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | path | 是 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/verifyReleaseCargoRules/{locationCode}

- 名称：放货规则
- Operation ID：`verifyReleaseCargoRulesUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | path | 是 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### AGV开关门回调任务

#### POST /jeecg-tms-api/tms/api/liftDoorBackService/liftDoorCallback

- 名称：AGV开关门回调任务
- Operation ID：`liftDoorCallbackUsingPOST`
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
| 200 | AgvResultDTO«T» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### MES-Controller

#### POST /jeecg-tms-api/tms/api/mes/bind

- 名称：绑定容器
- Operation ID：`bindUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesBindDTO | body | 是 | MESBindDTO | mesBindDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/mes/blankingCacheQuery

- 名称：TEST-触发MES下料缓存
- Operation ID：`blankingCacheQueryUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | query | 否 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/cancelDemand

- 名称：取消需求
- Operation ID：`cancelDemandUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesCancelDTO | body | 是 | MESCancelDTO | mesCancelDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/mes/getFlowCardInfo

- 名称：MES根据容器编码查询流程卡信息
- Operation ID：`getFlowCardInfoUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| containerNo | query | 否 | string | - |
| reqTaskCode | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«FlowCardInfoVo» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/mes/getLocationListByLogicalAreaId

- 名称：TEST-触发MES同步
- Operation ID：`getSyncInfoByBusinessIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| businessId | query | 否 | string | businessId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/mes/getProductInfoByFlowCard

- 名称：通过流程卡号查询产品信息
- Operation ID：`getProductInfoByFlowCardUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| flowCard | query | 否 | string | flowCard |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/mesPushTask

- 名称：机台呼叫上料/下料任务接口
- Operation ID：`mesPushTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesPushTaskDTO | body | 是 | MESPushTaskDTO | mesPushTaskDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/mesSyncFlowCardInfo

- 名称：流程卡信息同步接口
- Operation ID：`mesSyncFlowCardInfoUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesSyncFlowCardInfoDTO | body | 是 | MESSyncFlowCardInfoDTO | mesSyncFlowCardInfoDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/mesSyncLocStatus

- 名称：解绑接口
- Operation ID：`mesSyncLocStatusUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesSyncLocStatus | body | 是 | MESSyncLocStatusDTO | mesSyncLocStatus |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/mesSyncOrderInfo

- 名称：工单信息同步接口
- Operation ID：`mesSyncOrderInfoUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesSyncOrderInfoDTO | body | 是 | MESSyncOrderInfoDTO | mesSyncOrderInfoDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/mesSyncProcessInfo

- 名称：工序信息同步接口
- Operation ID：`mesSyncProcessInfoUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesSyncProcessInfoDTO | body | 是 | MESSyncProcessInfoDTO | mesSyncProcessInfoDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/searchFlowCardCount

- 名称：流程卡库存容器数量
- Operation ID：`searchFlowCardCountUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| mesFlagDTO | body | 是 | MESFlagDTO | mesFlagDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«JoinMESFLowCardVo»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/mes/syncTrayInfo

- 名称：MES同步卡板信息至TMS
- Operation ID：`syncTrayInfoUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| syncTrayInfo | body | 是 | SyncTrayInfo | syncTrayInfo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### Pad-点对点

#### POST /jeecg-tms-api/tms/api/pad/endIf

- 名称：判断终点
- Operation ID：`endIfUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| quickHandlingVo | body | 是 | QuickHandlingVo | quickHandlingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/findTargetAreaListByStart

- 名称：根据起点获取终点库区库位列表
- Operation ID：`findTargetAreaListByStartUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| quickHandlingVo | body | 是 | QuickHandlingVo | quickHandlingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/findTargetLocationListByCavernId

- 名称：根据库区获取可选库位
- Operation ID：`findTargetLocationListByCavernIdUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pointOptionalLocationQuery | body | 是 | PointOptionalLocationQuery | pointOptionalLocationQuery |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pointToPointMultiple

- 名称：点对点搬运
- Operation ID：`pointToPointMultipleUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| quickHandlingVo | body | 是 | QuickHandlingVo | quickHandlingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/startIf

- 名称：判断起点
- Operation ID：`startIfUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| quickHandlingVo | body | 是 | QuickHandlingVo | quickHandlingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### Pad-Controller

#### POST /jeecg-tms-api/tms/api/pad/batchRelease

- 名称：批量释放
- Operation ID：`batchReleaseUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCodeList | body | 是 | array<string> | locationCodeList |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/batchReleaseColumnSelectValidate

- 名称：批量释放  列选校验
- Operation ID：`batchReleaseColumnSelectValidateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCodeList | body | 是 | array<string> | locationCodeList |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«string»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/batchReleaseSelectValidate

- 名称：批量释放  选择/取消选择 储位校验
- Operation ID：`batchReleaseSelectValidateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pointToAreaLocationValidateVo | body | 是 | 点对区选择储位校验参数 | pointToAreaLocationValidateVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/binding

- 名称：绑定库位
- Operation ID：`bindingUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsBindingLocationVo | body | 是 | TmsBindingLocationVo | tmsBindingLocationVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/blankingTask

- 名称：下料任务
- Operation ID：`blankingTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| blankingTaskParam | body | 是 | BlankingTaskParam | blankingTaskParam |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/cancelDemand/{demandId}

- 名称：取消需求
- Operation ID：`cancelDemandUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/getEndLocationRouteByStart

- 名称：根据起点获取终点可达路由
- Operation ID：`getEndLocationRouteByStartUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| quickHandlingVo | body | 是 | QuickHandlingVo | quickHandlingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_storage_location对象»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getFlowCardListByContainer/{containerId}

- 名称：查询容器的流程卡号和工单
- Operation ID：`getFlowCardListByContainerUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| containerId | path | 是 | string | containerId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«流程卡号和工单号»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getInfoByTrayCode/{trayCode}

- 名称：通过托盘码获取详细资料
- Operation ID：`getInfoByTrayCodeUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| trayCode | path | 是 | string | trayCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/getLogicAreaByCode/{logicAreaCode}

- 名称：根据逻辑区编码查询逻辑区数据
- Operation ID：`getLogicAreaByCodeUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| logicAreaCode | path | 是 | string | logicAreaCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_task_type_range对象» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getOrderCodeByFlowCardId/{id}

- 名称：根据流程卡id查询工单号
- Operation ID：`getOrderCodeByFlowCardIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | path | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«流程卡号和工单号»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getOrderCodeByFlowCardNumber/{flowCardNumber}

- 名称：根据流程卡号获取绑定的工单号
- Operation ID：`getOrderCodeByFlowCardNumberUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| flowCardNumber | path | 是 | string | flowCardNumber |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«流程卡号和工单号» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/getPermissionByUserId

- 名称：获取此用户的菜单
- Operation ID：`getPermissionByUserIdUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| userId | query | 否 | string | userId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getProcessList

- 名称：获取工序列表
- Operation ID：`getProcessListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getStorageCavernList

- 名称：获取库区列表
- Operation ID：`getStorageCavernListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getStorageLocationInfo/{locationId}

- 名称：根据库位ID获取库位详情
- Operation ID：`getStorageLocationInfoUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationId | path | 是 | string | locationId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getStorageLocationList/{cavernId}

- 名称：根据库区ID获取库位列表
- Operation ID：`getStorageLocationListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| cavernId | path | 是 | string | cavernId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getTmsContainerList

- 名称：TMS容器列表
- Operation ID：`getTmsContainerListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pageNo | query | 否 | integer(int32) | - |
| pageSize | query | 否 | integer(int32) | - |
| searchKey | query | 否 | string | 容器号/流程卡号 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«容器列表模型»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getTmsDemand/{demandId}

- 名称：TMS需求池详情
- Operation ID：`getTmsDemandUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«需求详情模型» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/getTmsDemandList

- 名称：TMS需求池列表
- Operation ID：`getTmsDemandListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createTime | query | 否 | string(date-time) | 创建时间 |
| pageNo | query | 否 | integer(int32) | - |
| pageSize | query | 否 | integer(int32) | - |
| searchKey | query | 否 | string | 上游业务号/工单/流程卡号 |
| status | query | 否 | string | 需求状态，1-待处理，2-已处理，3-已取消 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«需求池列表模型»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/getTmsTaskList

- 名称：TMS任务列表
- Operation ID：`getTmsTaskListUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| searchTmsTaskListVo | body | 是 | SearchTmsTaskListVo | searchTmsTaskListVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«任务列表模型»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/loadingTask

- 名称：上料任务
- Operation ID：`loadingTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| genTmsTask | body | 是 | GenTmsTask | genTmsTask |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/login

- 名称：登录接口
- Operation ID：`loginUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| creationTime | query | 否 | integer(int64) | - |
| id | query | 否 | string | - |
| lastAccessedTime | query | 否 | integer(int64) | - |
| maxInactiveInterval | query | 否 | integer(int32) | - |
| new | query | 否 | boolean | - |
| tmsPdaLoginVo | body | 是 | 登录对象 | tmsPdaLoginVo |
| valueNames | query | 否 | array<string> | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«JSONObject» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/newCheckStorageLocationStatus

- 名称：新校验库位状态接口
- Operation ID：`newCheckStorageLocationStatusUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| checkStorageLocationStatusVo | body | 是 | CheckStorageLocationStatusVo | checkStorageLocationStatusVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/release/{locationCode}

- 名称：释放库位
- Operation ID：`releaseUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| locationCode | path | 是 | string | locationCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/updateDepthGroupParams

- 名称：修改深度组属性
- Operation ID：`updateDepthGroupParamsUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| depthUpdateVo | body | 是 | DepthUpdateVo | depthUpdateVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/validateCancelDemand/{demandId}

- 名称：取消需求校验
- Operation ID：`validateTaskStatusUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/verifyUpdateDepthGroupParams

- 名称：修改属性校验
- Operation ID：`verifyUpdateDepthGroupParamsUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| depthUpdateVo | body | 是 | DepthUpdateVo | depthUpdateVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### Pda-Controller

#### POST /jeecg-tms-api/tms/api/pad/pda/cancelDemand/{demandId}

- 名称：取消需求
- Operation ID：`cancelDemandUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/getFlowCardListByContainer/{containerId}

- 名称：查询容器的流程卡号和工单
- Operation ID：`getFlowCardListByContainerUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| containerId | path | 是 | string | containerId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«流程卡号和工单号»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/pad/pda/getPermissionByUserId

- 名称：菜单列表
- Operation ID：`getPermissionByUserIdUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| userId | query | 否 | string | userId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/getTmsContainerList

- 名称：TMS容器列表
- Operation ID：`getTmsContainerListUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| pageNo | query | 否 | integer(int32) | - |
| pageSize | query | 否 | integer(int32) | - |
| searchKey | query | 否 | string | 容器号/流程卡号 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«容器列表模型»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/getTmsDemand/{demandId}

- 名称：TMS需求池详情
- Operation ID：`getTmsDemandUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«需求详情模型» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/getTmsDemandList

- 名称：TMS需求池列表
- Operation ID：`getTmsDemandListUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createTime | query | 否 | string(date-time) | 创建时间 |
| pageNo | query | 否 | integer(int32) | - |
| pageSize | query | 否 | integer(int32) | - |
| searchKey | query | 否 | string | 上游业务号/工单/流程卡号 |
| status | query | 否 | string | 需求状态，1-待处理，2-已处理，3-已取消 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«需求池列表模型»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/getTmsTaskList

- 名称：TMS任务列表
- Operation ID：`getTmsTaskListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createTime | query | 否 | string(date-time) | - |
| pageNo | query | 否 | integer(int32) | - |
| pageSize | query | 否 | integer(int32) | - |
| searchKey | query | 否 | string | - |
| taskStatus | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«任务列表模型»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/pad/pda/validateCancelDemand/{demandId}

- 名称：取消需求校验
- Operation ID：`validateTaskStatusUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | path | 是 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### Test-Controller

#### POST /jeecg-tms-api/tms/api/test/conditionEvaluator

- 名称：开发 - conditionEvaluator
- Operation ID：`conditionEvaluatorUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| combinationId | query | 否 | string | combinationId |
| demandId | query | 否 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«条件分组对象» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/test/conditionEvaluatorOld

- 名称：开发 - conditionEvaluatorOld
- Operation ID：`conditionEvaluatorOldUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| demandId | query | 否 | string | demandId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«tms_conditional_combination对象»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/test/fixCondition

- 名称：开发 - fixCondition
- Operation ID：`fixConditionUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«EvaluateResult» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/getStorageLocation/{id}

- 名称：开发 - 测试新增字段忽略
- Operation ID：`getStorageLocationUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | path | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_storage_location对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/test/testDepthInfoByLocIds

- 名称：开发 - 测试根据储位查询深度组信息
- Operation ID：`testDepthInfoByLocIdsUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| args | body | 是 | array<string> | args |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«DepthInfo»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/test/testFlagUpdate

- 名称：开发 - 测试标识更新
- Operation ID：`testFlagUpdateUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| args | body | 是 | array<string> | args |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testHighPrecisionDate

- 名称：开发 - 测试插入高精度时间
- Operation ID：`testHighPrecisionDateUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testProcessRoute

- 名称：开发 - 测试工艺路线是否存在
- Operation ID：`testProcessRouteUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| route | query | 否 | string | route |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_process_route对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testRedisLock

- 名称：开发 - 测试Redis Lock
- Operation ID：`testRedisUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| key | query | 否 | string | key |
| releaseTime | query | 否 | integer(int64) | releaseTime |
| value | query | 否 | string | value |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testTTS

- 名称：开发 - 测试tts微服务调用
- Operation ID：`testTTSUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testWeChat

- 名称：开发 - 测试wechat微服务调用
- Operation ID：`testWeChatUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| content | query | 否 | string | content |
| user | query | 否 | string | user |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«JSONObject» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/testWXTZ

- 名称：开发 - 测试企微通知
- Operation ID：`testWXTZUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| content | query | 否 | string | content |
| user | query | 否 | string | user |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«JSONObject» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-tms-api/tms/api/test/triggerDemandPollQueryByContainer

- 名称：容器 - 触发需求池查询
- Operation ID：`triggerDemandPollQueryByContainerUsingGET`
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

#### GET /jeecg-tms-api/tms/api/test/triggerDemandPollQueryLocation

- 名称：库位 - 触发需求池查询
- Operation ID：`triggerDemandPollQueryLocationUsingGET`
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

#### GET /jeecg-tms-api/tms/api/test/triggerTmsTaskPoll/{taskPollId}

- 名称：触发容器未执行任务
- Operation ID：`triggerTmsTaskPollUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| taskPollId | path | 是 | string | taskPollId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### test-modbus

#### POST /jeecg-tms-api/tms/api/testModbus/testModbus

- 名称：开发 - 通用测试modbus读写[type=0写;type=1读]
- Operation ID：`testModbusUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| testRollingDoorVO | body | 是 | TestRollingDoorVO | testRollingDoorVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/testModbus/testRollingDoor

- 名称：开发 - 测试卷帘门调度
- Operation ID：`testRollingDoorUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| testRollingDoorVO | body | 是 | TestRollingDoorVO | testRollingDoorVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/testModbus/testRollingDoorRead

- 名称：开发 - 测试卷帘门读取门开状态
- Operation ID：`testRollingDoorReadUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| testRollingDoorVO | body | 是 | TestRollingDoorVO | testRollingDoorVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«boolean» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### WCS-Controller

#### POST /jeecg-tms-api/tms/api/wcs/syncConveyorLine

- 名称：WCS同步输送线口值
- Operation ID：`syncConveyorLineUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| syncConveyorLineVo | body | 是 | SyncConveyorLineVo | syncConveyorLineVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wcs/unbind

- 名称：WCS释放储位
- Operation ID：`unbindUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| unbindRequest | body | 是 | UnbindRequest | unbindRequest |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### WMS-Controller

#### POST /jeecg-tms-api/tms/api/wms/createTask

- 名称：下发搬运任务
- Operation ID：`createTaskUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| taskVo | body | 是 | TaskVo | taskVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wms/unbind

- 名称：请求解绑
- Operation ID：`unbindUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| unBindVo | body | 是 | UnBindVo | unBindVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-tms-api/tms/api/wms/wmsBindAndUnbind

- 名称：MES绑定托盘码与储位和解绑储位
- Operation ID：`wmsBindAndUnbindUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| wmsBindingVo | body | 是 | WmsBindingVo | wmsBindingVo |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

## 数据模型

### 登录对象

登录对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| blankingAreaId | 否 | string | 下料区ID |
| loadingAreaId | 否 | string | 上料区ID |
| passWord | 否 | string | 密码 |
| thisProcessId | 否 | string | 工序ID |
| thisProcessName | 否 | string | 工序名称 |
| userName | 否 | string | 账号 |

### 点对区任务下发VO对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| comment | 否 | string | 备注 |
| endAreaId | 否 | string | 终点逻辑区ID |
| goodsTypeId | 否 | string | 货型ID |
| startLocationCode | 否 | string | 起点储位编码 |
| startLocationId | 否 | string | 起点储位ID |

### 点对区选择储位校验参数

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| clickedLocationCode | 否 | string | 当前点击的储位编码 |
| operateType | 否 | string | 操作类型 1:选中 0:取消选中 |
| selectedLocationCodes | 否 | array<string> | 已选中的储位编码 |

### 接口返回对象«流程卡号和工单号»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | 流程卡号和工单号 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«条件分组对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | 条件分组对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«需求详情模型»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | 需求详情模型 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«boolean»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | boolean | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«EvaluateResult»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | EvaluateResult | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«FlowCardInfoVo»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | FlowCardInfoVo | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«任务列表模型»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«任务列表模型» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«容器列表模型»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«容器列表模型» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«需求池列表模型»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«需求池列表模型» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«JSONObject»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | object | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«流程卡号和工单号»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<流程卡号和工单号> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«DepthInfo»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<DepthInfo> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«GoodsTypeVO»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<GoodsTypeVO> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«JoinMESFLowCardVo»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<JoinMESFLowCardVo> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«List«LocationVO»»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<array<LocationVO>> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«LogicalAreaTagVO»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<LogicalAreaTagVO> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«LogicalAreaVO»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<LogicalAreaVO> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«StorageCavernVo»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<StorageCavernVo> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«string»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<string> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_conditional_combination对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_conditional_combination对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«List«tms_storage_location对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<tms_storage_location对象> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«Map«string,List«HistoryRecordVO»»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | object | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«object»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | object | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«Page«AgvStatusVo»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | Page«AgvStatusVo» | 返回数据对象 |
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

### 接口返回对象«T»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | T | 返回数据对象 |
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

### 接口返回对象«tms_storage_location对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_storage_location对象 | 返回数据对象 |
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

### 流程卡号和工单号

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| flowCardNumber | 否 | string | 流程卡号 |
| workOrderNumber | 否 | string | 工单号 |

### 流程卡信息

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| flowCardNumber | 否 | string | 流程卡编号 |
| id | 否 | string | 流程卡ID |
| workOrderNumber | 否 | string | 工单编号 |

### 任务列表模型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string | 容器号 |
| createTime | 否 | string(date-time) | 创建时间 |
| demandId | 否 | string | 需求ID |
| endLocationCode | 否 | string | 终点储位 |
| endStorageCavernName | 否 | string | 终点储区 |
| flowCardNumber | 否 | string | 流程卡号 |
| startLocationCode | 否 | string | 起点储位 |
| startStorageCavernName | 否 | string | 起点储区 |
| status | 否 | string | 任务状态 |
| tmsTaskCode | 否 | string | TMS任务号 |
| trayCode | 否 | string |  |
| upstreamTaskNo | 否 | string | 上游任务号 |
| vehicleTaskCode | 否 | string | 车辆任务号 |

### 容器列表模型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string | 容器号 |
| containerId | 否 | string | 容器id |
| flowCardNumber | 否 | string | 流程卡号 |
| goodsTypeName | 否 | string | 货型 |
| status | 否 | string | 容器业务状态：0 可用，1 占用，2 禁用 |
| storageLocationCode | 否 | string | 所在储位 |
| tmsTaskCode | 否 | string | TMS任务号 |
| upstreamTaskNo | 否 | string | 上游业务号 |

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

### 条件分组对象

条件分组

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| allConditionsCount | 否 | integer(int32) |  |
| childrenGroups | 否 | array<条件分组对象> | 子分组列表 |
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

### 需求池列表模型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string | 容器号 |
| createTime | 否 | string(date-time) | 创建日期 |
| demandId | 否 | string | 需求id |
| endLocationCode | 否 | string | 终点储位 |
| endStorageCavernName | 否 | string | 终点储区 |
| flowCardNumber | 否 | string | 流程卡号 |
| startLocationCode | 否 | string | 起点储位 |
| startStorageCavernName | 否 | string | 起点储区 |
| status | 否 | string | 需求状态，1-待处理，2-已处理，3-已取消 |
| tmsTaskCode | 否 | string | TMS任务号 |
| upstreamTaskNo | 否 | string | 上游业务号 |
| workOrderNumber | 否 | string | 工单号 |

### 需求详情模型

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| comment | 否 | string | 备注 |
| containerCode | 否 | string | 容器号 |
| createTime | 否 | string(date-time) | 创建日期 |
| endLocationCode | 否 | string | 终点储位 |
| endLogicalAreaName | 否 | string | 终点逻辑区 |
| endStorageCavernName | 否 | string | 终点储区 |
| flowCardNumber | 否 | string | 流程卡号 |
| goodsTypeName | 否 | string | 货型 |
| startLocationCode | 否 | string | 起点储位 |
| startLogicalAreaName | 否 | string | 起点逻辑区 |
| startStorageCavernName | 否 | string | 起点储区 |
| status | 否 | string | 需求状态，1-待处理，2-已处理，3-已取消 |
| tmsTaskCode | 否 | string | TMS任务号 |
| upstreamTaskNo | 否 | string | 上游业务号 |
| workOrderNumber | 否 | string | 工单号 |

### AddHistoryRecord

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| goodsTypeId | 否 | string |  |
| source | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| type | 否 | string |  |
| userId | 否 | string |  |

### AgvErrorCallbackDataDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| beginTime | 否 | string |  |
| robotCode | 否 | string |  |
| taskCode | 否 | string |  |
| warnContent | 否 | string |  |

### AgvErrorCallbackDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| clientCode | 否 | string |  |
| data | 否 | array<AgvErrorCallbackDataDTO> |  |
| reqCode | 否 | string |  |
| reqTime | 否 | string |  |
| tokenCode | 否 | string |  |

### AgvResultDTO«T»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string |  |
| message | 否 | string |  |
| reqCode | 否 | string |  |

### AgvStatusVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| battery | 否 | string |  |
| carStatus | 否 | string |  |
| carType | 否 | string |  |
| dayTaskNum | 否 | integer(int64) |  |
| exclType | 否 | string |  |
| mapCode | 否 | string |  |
| monthTaskNum | 否 | integer(int64) |  |
| path | 否 | array<string> |  |
| podCode | 否 | string |  |
| podDir | 否 | string |  |
| posX | 否 | string |  |
| posY | 否 | string |  |
| robotCode | 否 | string |  |
| robotDir | 否 | string |  |
| robotIp | 否 | string |  |
| speed | 否 | string |  |
| status | 否 | string |  |
| stop | 否 | string |  |
| type | 否 | string |  |

### BlankingTaskParam

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| currentProcessId | 否 | string |  |
| floCardNo | 否 | string |  |
| nextProcessId | 否 | string |  |
| sort | 否 | integer(int32) |  |
| storageLocationId | 否 | string |  |
| workOrderNo | 否 | string |  |

### CallbackDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| cooX | 否 | string |  |
| cooY | 否 | string |  |
| currentPositionCode | 否 | string |  |
| data | 否 | object |  |
| mapCode | 否 | string |  |
| mapDataCode | 否 | string |  |
| method | 否 | string |  |
| podCode | 否 | string |  |
| podDir | 否 | string |  |
| reqCode | 否 | string |  |
| reqTime | 否 | string |  |
| robotCode | 否 | string |  |
| taskCode | 否 | string |  |
| wbCode | 否 | string |  |

### CheckStorageLocationStatusVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| reqCode | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| taskType | 否 | string |  |
| type | 否 | string |  |

### DepthInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| depthGroupCode | 否 | string |  |
| direction | 否 | string |  |
| freeFlag | 否 | integer(int32) |  |
| hitTheShelfFlag | 否 | integer(int32) |  |
| hitTheShelfOrder | 否 | integer(int32) |  |
| ids | 否 | array<string> |  |
| singleOrDouble | 否 | string |  |
| soldOutFlag | 否 | integer(int32) |  |
| soldOutOrder | 否 | integer(int32) |  |
| subLocInfoList | 否 | array<DepthSubLocInfo> |  |

### DepthSubLocInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| l | 否 | integer(int32) |  |
| locationId | 否 | string |  |
| r | 否 | integer(int32) |  |

### DepthUpdateVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| depthGroupCode | 否 | string |  |
| processId | 否 | string |  |

### EvaluateResult

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| failedConditions | 否 | array<tms_condition对象> |  |
| result | 否 | boolean |  |

### FlowCardInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| flowCardBusinessId | 否 | string |  |
| flowCardNumber | 否 | string |  |
| materialCode | 否 | string |  |
| materialName | 否 | string |  |
| materialNumber | 否 | number |  |
| operateTime | 否 | string(date-time) |  |
| orderCode | 否 | string |  |
| otherInfo | 否 | string |  |
| packageNum | 否 | string |  |
| sourceSystem | 否 | string |  |
| status | 否 | string |  |
| undulate | 否 | string |  |

### FlowCardInfoVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerNo | 否 | string |  |
| flowCardNumber | 否 | string |  |
| reqTaskCode | 否 | string |  |

### GenTmsTask

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| downMaterialStorageCavernId | 否 | string |  |
| lastProcessId | 否 | string |  |
| materialName | 否 | string |  |
| mes | 否 | boolean |  |
| nextProcessId | 否 | string |  |
| pattern | 否 | string |  |
| quantity | 否 | string |  |
| reqCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| thisProcessId | 否 | string |  |
| trayCode | 否 | string |  |
| upMaterialStorageCavernId | 否 | string |  |
| workOrderNumber | 否 | string |  |

### GoodsTypeVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| goodsTypeCode | 否 | string |  |
| id | 否 | string |  |

### HistoryRecordVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| goodsTypeId | 否 | string |  |
| goodsTypeName | 否 | string |  |
| id | 否 | string |  |
| status | 否 | string |  |
| storageLocationStatus | 否 | string |  |

### IPage«任务列表模型»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<任务列表模型> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«容器列表模型»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<容器列表模型> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«需求池列表模型»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<需求池列表模型> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### JoinMESFLowCardVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| count | 否 | integer(int64) |  |
| packageNum | 否 | string |  |
| undulate | 否 | string |  |

### LocationVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| columnNumber | 否 | integer(int32) |  |
| depthGroupCode | 否 | string |  |
| depthOne | 否 | integer(int32) |  |
| depthTwo | 否 | integer(int32) |  |
| direction | 否 | string |  |
| hitTheShelfOrder | 否 | integer(int32) |  |
| id | 否 | string |  |
| rowNumber | 否 | integer(int32) |  |
| soldOutOrder | 否 | integer(int32) |  |
| status | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationStatus | 否 | string |  |

### LogicalAreaTagVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| id | 否 | string |  |
| tagName | 否 | string |  |

### LogicalAreaVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| id | 否 | string |  |
| logicalAreaName | 否 | string |  |

### MESBindDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerNo | 否 | string |  |
| storageLocationCode | 否 | string |  |

### MESCancelDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| upStreamTaskNo | 否 | string |  |

### MESFlagDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| lastProcessCode | 否 | string |  |
| orderCode | 否 | string |  |
| packageNum | 否 | string |  |
| undulate | 否 | string |  |

### MESPushTaskDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerNo | 否 | string |  |
| containerTaskCode | 否 | string |  |
| currentProcessCode | 否 | string |  |
| equipmentCode | 否 | string |  |
| flowCard | 否 | string |  |
| goodTypeCode | 否 | string |  |
| lastProcessCode | 否 | string |  |
| mesCreateTime | 否 | string |  |
| mesUpdateTime | 否 | string |  |
| nextProcessCode | 否 | string |  |
| orderInfo | 否 | array<OrderAndFlowCardVO> |  |
| packageNum | 否 | string |  |
| pattern | 否 | string |  |
| section | 否 | string |  |
| storageLocationCode | 否 | string |  |
| targetCavernCode | 否 | string |  |
| targetLocationCode | 否 | string |  |
| taskCode | 否 | string |  |
| tasktype | 否 | string |  |
| tmsReqTaskCode | 否 | string |  |
| undulate | 否 | string |  |

### MESSyncFlowCardInfoDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| flowCardInfos | 否 | array<FlowCardInfo> |  |

### MESSyncLocStatusDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| locBusinessId | 否 | string |  |
| operateTime | 否 | string(date-time) |  |
| taskCode | 否 | string |  |

### MESSyncOrderInfoDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| orderInfos | 否 | array<OrderInfo> |  |

### MESSyncProcessInfoDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| processInfos | 否 | array<ProcessInfo> |  |

### OrderAndFlowCardVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| flowCard | 否 | string |  |
| flowCardBusinessId | 否 | string |  |
| orderCode | 否 | string |  |

### OrderInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| businessStatus | 否 | string |  |
| materialCode | 否 | string |  |
| materialName | 否 | string |  |
| operateTime | 否 | string(date-time) |  |
| orderCode | 否 | string |  |
| processRoute | 否 | string |  |
| sourceSystem | 否 | string |  |
| status | 否 | string |  |

### OrderItem

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| asc | 否 | boolean |  |
| column | 否 | string |  |

### Page«AgvStatusVo»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| countId | 否 | string |  |
| current | 否 | integer(int64) |  |
| maxLimit | 否 | integer(int64) |  |
| optimizeCountSql | 否 | boolean |  |
| orders | 否 | array<OrderItem> |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<AgvStatusVo> |  |
| searchCount | 否 | boolean |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### PointOptionalLocationQuery

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| cavernId | 否 | string |  |
| optionalLocationIds | 否 | string |  |

### ProcessInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| operateTime | 否 | string(date-time) |  |
| processCode | 否 | string |  |
| processName | 否 | string |  |
| processType | 否 | string |  |
| sourceSystem | 否 | string |  |
| status | 否 | string |  |

### QuickHandlingVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| endStorageLocationCode | 否 | string |  |
| endStorageLocationId | 否 | string |  |
| materialName | 否 | string |  |
| nextProcessId | 否 | string |  |
| pattern | 否 | string |  |
| reqCode | 否 | string |  |
| startStorageLocationCode | 否 | string |  |
| startStorageLocationId | 否 | string |  |
| thisProcessId | 否 | string |  |
| trayCode | 否 | string |  |
| workOrderNumber | 否 | string |  |

### RcsNotifyTrafficTaskDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| agvCode | 否 | string |  |
| method | 否 | string |  |
| reqCode | 否 | string |  |
| taskCode | 否 | string |  |
| trafficId | 否 | string |  |

### SearchTmsTaskListVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createTime | 否 | string(date-time) |  |
| pageNo | 否 | integer(int32) |  |
| pageSize | 否 | integer(int32) |  |
| searchKey | 否 | string |  |
| taskStatus | 否 | string |  |

### StorageCavernVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| disable | 否 | integer(int32) |  |
| free | 否 | integer(int64) |  |
| occupy | 否 | integer(int64) |  |
| preoccupy | 否 | integer(int64) |  |
| storageCavernName | 否 | string |  |
| storageLocationData | 否 | array<array<StorageLocationVo>> |  |
| total | 否 | integer(int32) |  |

### StorageLocationVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| flowCardNumber | 否 | string |  |
| status | 否 | string |  |
| storageLocationStatus | 否 | string |  |
| x | 否 | integer(int32) |  |
| y | 否 | integer(int32) |  |

### SyncConveyorLineVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| conveyorLineValue | 否 | string |  |
| locationId | 否 | string |  |

### SyncTrayInfo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| Basic_ItemCode | 否 | string |  |
| Basic_ItemName | 否 | string |  |
| Basic_ProcessCode | 否 | string |  |
| Basic_ProcessName | 否 | string |  |
| Next_ProcessCode | 否 | string |  |
| Next_ProcessName | 否 | string |  |
| Order_WorkOrderCode | 否 | string |  |
| Pallet_id | 否 | string |  |
| ReqAmount | 否 | number |  |

### T

_无字段定义。_

### TaskVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| sourceLocation | 否 | string |  |
| targetCavern | 否 | string |  |
| targetLocation | 否 | string |  |
| taskCode | 否 | string |  |
| taskStatus | 否 | string |  |
| updateTime | 否 | string(date-time) |  |

### TestRollingDoorVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| functionCode | 否 | string |  |
| ip | 否 | string |  |
| numberValue | 否 | integer(int32) |  |
| offset | 否 | integer(int32) |  |
| port | 否 | integer(int32) |  |
| readFunctionCode | 否 | string |  |
| slaveId | 否 | integer(int32) |  |
| systemConfig | 否 | integer(int32) |  |
| type | 否 | string |  |

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

### tms_conditional_combination对象

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

### tms_storage_location对象

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

### tms_task对象

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

### TmsBindingLocationVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| flowCardNumber | 否 | string |  |
| lastProcessId | 否 | string |  |
| lastProcessName | 否 | string |  |
| nextProcessId | 否 | string |  |
| nextProcessName | 否 | string |  |
| storageLocationCode | 否 | string |  |
| storageLocationId | 否 | string |  |
| thisProcessId | 否 | string |  |
| thisProcessName | 否 | string |  |
| workOrderNumber | 否 | string |  |

### TmsCallBackDto

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| method | 否 | string |  |
| taskCode | 否 | string |  |

### UnbindRequest

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| locationId | 否 | string |  |
| taskCode | 否 | string |  |

### UnBindVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerCode | 否 | string |  |
| createTime | 否 | string(date-time) |  |
| taskCode | 否 | string |  |
| updateTime | 否 | string(date-time) |  |

### VisionnavCallbackDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| agvId | 否 | string | 指令执行状态 0:已接收; 1:开始执行; 2:执行完成; 3:执行错误; 4:指令被终止; 6:指令过期 |
| agvName | 否 | string | 执行此指令的车辆编号 |
| endTime | 否 | string | 指令结束（完成、取消或者终止）时间 |
| errors | 否 | array<object> | 指令处理异常码数组，指令处理异常时有效,非车辆异常码 |
| id | 否 | string | 上位系统的指令编号 |
| result | 否 | object | 完成结果 |
| stage | 否 | integer(int32) | stage=0表示初始状态，等于1表示已取货，等于2表示已放货，等于3表示已取货和已放货 |
| startTime | 否 | string | 指令开始时间 |
| state | 否 | integer(int32) | 上位系统的指令编号 |

### WmsBindingVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| storageLocationBusinessId | 否 | string |  |
| trayCode | 否 | string |  |
| type | 否 | string |  |

