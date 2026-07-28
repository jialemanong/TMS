# TMS 接口知识库总览

> 接口事实以 `raw/*.swagger.json` 为准；`generated/*.md` 为可检索明细。采集日期：2026-07-28。

## 接口规模

| 服务 | 业务定位 | Base Path | 路径数 | 操作数 | 模型数 | 明细 |
|---|---|---|---:|---:|---:|---|
| jeecg-tms | TMS 核心后台 | `/jeecg-tms` | 283 | 327 | 225 | [查看](generated/jeecg-tms.md) |
| jeecg-tms-api | TMS 对外及终端 | `/jeecg-tms-api` | 109 | 109 | 101 | [查看](generated/jeecg-tms-api.md) |
| jeecg-camera | 摄像头/明眸 | `/jeecg-camera` | 2 | 2 | 1 | [查看](generated/jeecg-camera.md) |
| jeecg-radar | 雷达/RFID/报警灯 | `/jeecg-radar` | 17 | 17 | 10 | [查看](generated/jeecg-radar.md) |
| jeecg-system | 系统管理与权限 | `/jeecg-system` | 84 | 95 | 31 | [查看](generated/jeecg-system.md) |

合计：495 条路径，550 个接口操作，368 个数据模型。

## 查询路由

| 查询目标 | 优先文档 |
|---|---|
| 后台基础数据、任务池、规则、配置、报表 | `generated/jeecg-tms.md` |
| PAD/PDA、MES/WMS/WCS、AGV回调、提升机 | `generated/jeecg-tms-api.md` |
| 明眸/摄像头通知 | `generated/jeecg-camera.md` |
| 雷达、RFID、报警灯 | `generated/jeecg-radar.md` |
| 登录、权限、数据字典、系统基础能力 | `generated/jeecg-system.md` |

## 使用边界

1. Swagger 描述反映接口声明，不等同于完整业务规则；业务断言仍应联合状态机、流程和约束规则。
2. 所有服务均声明 `X-Access-Token` 请求头，但公开回调是否免鉴权需以环境配置和实测为准。
3. 文档未统一声明服务协议，示例网关使用当前文档站点的 HTTP 地址。
4. `Test-Controller`、测试 Modbus、模拟通知和系统开关接口具有环境风险，自动化默认不得在生产环境执行。
5. Swagger 的通用 `200` 响应不代表业务成功，测试需继续断言响应体中的成功标识、业务码和数据状态。
