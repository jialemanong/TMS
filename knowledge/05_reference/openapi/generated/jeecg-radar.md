# 雷达/RFID/报警灯接口明细

> 来源：`../raw/jeecg-radar.swagger.json`。本文由生成器自动生成，请勿手工修改生成区内容。

## 服务信息

- 服务标识：`jeecg-radar`
- 网关地址：`http://111.160.91.170:59999`
- Base Path：`/jeecg-radar`
- 鉴权头：`X-Access-Token`
- 路径数：17
- 接口操作数：17
- 数据模型数：10

## 控制器索引

| 控制器/标签 | 接口数 |
|---|---:|
| 报警灯接口 | 3 |
| 车载rfid接口 | 5 |
| 雷达测试接口 | 4 |
| 摄像头测试接口 | 2 |
| rfid服务 | 3 |

## 接口清单

### 报警灯接口

#### GET /jeecg-radar/alarm-light/control

- 名称：报警灯控制
- Operation ID：`alarmLightControlUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| command | query | 是 | array<string> | command |
| deviceCode | query | 是 | string | deviceCode |
| ip | query | 是 | string | ip |
| port | query | 是 | integer(int32) | port |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/alarm-light/disconnect

- 名称：断开报警灯
- Operation ID：`disconnectAlarmLightUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| deviceCode | query | 是 | string | deviceCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/alarm-light/get-connected-alarm-light

- 名称：获取当前连接的报警灯
- Operation ID：`getConnectedAlarmLightUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«Map«string,object»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 车载rfid接口

#### GET /jeecg-radar/vce-rfid/getDevices

- 名称：获取连接的设备列表
- Operation ID：`getDevicesUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | string | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/vce-rfid/inventory

- 名称：开始持续盘点
- Operation ID：`inventoryUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| deviceCode | query | 是 | string | deviceCode |
| ip | query | 是 | string | ip |
| port | query | 是 | integer(int32) | port |
| timeout | query | 是 | integer(int32) | timeout |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/vce-rfid/inventoryByServer

- 名称：开始持续盘点(服务端)
- Operation ID：`inventoryByServerUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| deviceCode | query | 是 | string | deviceCode |
| timeout | query | 是 | integer(int32) | timeout |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/vce-rfid/inventoryOnce

- 名称：开始单次盘点
- Operation ID：`inventoryOnceUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| deviceCode | query | 是 | string | deviceCode |
| ip | query | 是 | string | ip |
| port | query | 是 | integer(int32) | port |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/vce-rfid/inventoryOnceByServer

- 名称：开始单次盘点(服务端)
- Operation ID：`inventoryOnceByServerUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| deviceCode | query | 是 | string | deviceCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 雷达测试接口

#### POST /jeecg-radar/radar/addDevice/{id}

- 名称：添加设备
- Operation ID：`addDeviceUsingPOST_1`
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
| 200 | string | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-radar/radar/deleteDevice/{id}

- 名称：删除设备
- Operation ID：`deleteDeviceUsingPOST_1`
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
| 200 | string | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-radar/radar/getRadarDevicesWithLocations

- 名称：获取雷达设备列表
- Operation ID：`getRadarDevicesWithLocationsUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | array<RadarDevice> | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-radar/radar/sendCommand/{id}

- 名称：发送指令
- Operation ID：`sendCommandUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| commandCode | query | 否 | string | commandCode |
| id | path | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | string | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 摄像头测试接口

#### POST /jeecg-radar/camera/addDevice/{id}

- 名称：添加设备
- Operation ID：`addDeviceUsingPOST`
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
| 200 | string | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-radar/camera/deleteDevice/{id}

- 名称：删除设备
- Operation ID：`deleteDeviceUsingPOST`
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
| 200 | string | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### rfid服务

#### POST /jeecg-radar/rfid/queryBatchRfid

- 名称：满垛群读RFID
- Operation ID：`queryBatchRfidUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| queryMachineRfVO | body | 是 | QueryRfDTO | queryMachineRfVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«List«string»» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-radar/rfid/queryMachineRfid

- 名称：查询机台rf容器信息
- Operation ID：`queryMachineRfidUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| queryMachineRfVO | body | 是 | QueryRfDTO | queryMachineRfVO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«ResponseMachineRfDTO» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-radar/rfid/testRfid

- 名称：测试RFID
- Operation ID：`testRfidUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| rfIdTestDTO | body | 是 | RfIdTestDTO | rfIdTestDTO |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

## 数据模型

### 接口返回对象«List«string»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | array<string> | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«Map«string,object»»

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

### 接口返回对象«ResponseMachineRfDTO»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | ResponseMachineRfDTO | 返回数据对象 |
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

### QueryRfDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| locationCode | 否 | string |  |

### RadarDevice

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| connectStatus | 否 | integer(int32) |  |
| deviceCode | 否 | string |  |
| deviceIp | 否 | string |  |
| deviceName | 否 | string |  |
| devicePort | 否 | integer(int32) |  |
| deviceType | 否 | integer(int32) |  |
| id | 否 | string |  |
| locationIndex | 否 | integer(int32) |  |
| locations | 否 | array<RadarDeviceLocation> |  |
| systemSource | 否 | string |  |
| timeOutHeart | 否 | integer(int32) |  |
| timeOutRw | 否 | integer(int32) |  |

### RadarDeviceLocation

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| deviceCode | 否 | string |  |
| id | 否 | string |  |
| interfaceCode | 否 | string |  |
| interfaceType | 否 | integer(int32) |  |
| intervalTime | 否 | integer(int32) |  |
| lastReportedValue | 否 | string |  |
| locationCode | 否 | string |  |
| locationId | 否 | string |  |
| nreadDefault | 否 | string |  |
| sameValueCount | 否 | integer(int32) |  |
| yreadAddress | 否 | string |  |
| yreadDefault | 否 | string |  |
| yreadValue | 否 | string |  |

### ResponseMachineRfDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| containerNo | 否 | string |  |
| deviceCode | 否 | string |  |
| locationCode | 否 | string |  |

### RfIdTestDTO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| ip | 否 | string |  |
| port | 否 | integer(int32) |  |
| registerQuantity | 否 | integer(int32) |  |
| slaveId | 否 | integer(int32) |  |
| startOffSet | 否 | integer(int32) |  |

