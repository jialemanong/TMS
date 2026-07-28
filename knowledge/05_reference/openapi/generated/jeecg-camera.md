# 摄像头/明眸接口明细

> 来源：`../raw/jeecg-camera.swagger.json`。本文由生成器自动生成，请勿手工修改生成区内容。

## 服务信息

- 服务标识：`jeecg-camera`
- 网关地址：`http://111.160.91.170:59999`
- Base Path：`/jeecg-camera`
- 鉴权头：`X-Access-Token`
- 路径数：2
- 接口操作数：2
- 数据模型数：1

## 控制器索引

| 控制器/标签 | 接口数 |
|---|---:|
| 超脑 | 2 |

## 接口清单

### 超脑

#### POST /jeecg-camera/camera/mockInform

- 名称：模拟明眸通知
- Operation ID：`mockInformUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ruleName | query | 否 | string | ruleName |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-camera/camera/monitoring/{state}

- 名称：布防撤防
- Operation ID：`monitoringUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| state | path | 是 | string | 布防撤防指令,0 撤防, 1 布防 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

## 数据模型

### 接口返回对象«string»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | string | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

