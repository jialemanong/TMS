# TMS API自动化代码开发规范

> 规范级别：强制
>
> 适用系统：TMS
>
> 技术栈：Python + pytest + requests
>
> 基座目录：`auto_test/`
>
> 业务知识入口：`knowledge/KNOWLEDGE_INDEX.md`

## 一、适用范围与原则

本规范适用于TMS后台接口、PAD/PDA接口以及TMS与MES、WMS、WCS、RCS和设备系统之间的接口自动化。

所有测试代码必须遵守以下原则：

1. 业务定义、状态流转和约束优先从 `knowledge/KNOWLEDGE_INDEX.md` 路由查询。
2. 知识库没有明确说明的行为必须标记“知识库未明确说明”，禁止自行推断。
3. 测试代码只描述测试场景，不重复实现HTTP、配置、日志和报告基础设施。
4. 地址、Token、账号和密码只能来自配置或环境变量，禁止写入代码和测试数据。
5. 接口成功不能只以HTTP 200判断，必须同时验证业务响应和业务状态。

## 二、工程分层

```text
auto_test/
├── conftest.py                 pytest全局fixture和报告钩子
├── config/
│   └── env.yaml                多环境配置模板
├── core/
│   ├── api_client.py           requests统一封装
│   ├── browser_base.py         Playwright基础封装
│   └── reporter.py             JSON/JSONL结构化报告
├── test_api/
│   ├── data/                   复杂请求数据，按模块划分
│   └── test_tms/               TMS业务接口用例
├── test_ui/                    UI业务用例
├── utils/
│   └── logger.py               结构化日志与敏感信息脱敏
└── requirements.txt
```

分层职责：

| 层级 | 允许内容 | 禁止内容 |
|---|---|---|
| `config` | 环境模板、非敏感默认配置、环境变量占位符 | 真实账号、密码、Token、生产地址 |
| `core` | 通用请求、异常、日志、报告能力 | TMS业务场景和业务断言 |
| `test_api/data` | 可复用请求模板和参数数据 | HTTP调用逻辑、凭证 |
| `test_api/test_tms` | 场景编排、调用ApiClient、业务断言 | 裸用requests、自建Session |
| `utils` | 与业务无关的通用工具 | 业务流程实现 |

## 三、命名规范

### 3.1 文件和目录

- 测试文件：`test_tms_<模块>_<能力>.py`
- 数据文件：`<模块>_<场景>.yaml` 或 `<模块>_<场景>.json`
- 公共辅助模块：使用小写下划线命名

示例：

```text
test_tms_transport_order_create.py
test_tms_demand_cancel.py
transport_order_valid_payload.json
```

### 3.2 测试函数

- 格式：`test_<业务动作>_<场景或预期>`
- 正常：`test_create_transport_order_success`
- 异常：`test_create_transport_order_missing_required_field`
- 边界：`test_query_transport_order_page_size_boundary`

测试名称必须表达业务行为，禁止使用 `test_001`、`test_demo` 等无语义名称。

### 3.3 类和变量

- 测试类可选，命名为 `Test<Module><Capability>`。
- 请求体使用 `payload`，查询参数使用 `params`，响应使用 `response`。
- 业务标识使用明确名称，例如 `demand_id`、`task_code`，禁止使用 `data1`、`temp`。

## 四、Fixture使用规则

现有公共fixture定义于 `auto_test/conftest.py`：

| Fixture | Scope | 用途 |
|---|---|---|
| `environment_name` | session | 当前环境名称 |
| `settings` | session | 合并并展开环境变量后的配置 |
| `artifact_dir` | session | 本次执行产物目录 |
| `api_client` | session | 全局统一ApiClient |
| `browser_base` | function | UI基础浏览器封装 |

API用例必须通过参数注入 `api_client`：

```python
import pytest

from auto_test.core.api_client import ApiClient


@pytest.mark.api_tms
@pytest.mark.knowledge("knowledge/对应业务文档.md")
@pytest.mark.scenario("明确的TMS业务场景")
def test_example_success(api_client: ApiClient):
    """场景：填写实际场景；前置：填写前置；预期：填写业务结果。"""
    response = api_client.post("/path/from-openapi", json={"field": "value"})
    assert response.status_code == 200
```

规则：

1. 禁止在用例中实例化 `requests.Session` 或 `ApiClient`。
2. 禁止用例自行读取 `env.yaml`；配置由fixture统一注入。
3. 需要新增公共fixture时，应先确认是否具备跨模块复用价值。
4. 资源型fixture必须使用 `yield` 并在结束阶段清理测试数据。
5. Fixture不得隐式创建不可追踪的业务数据；创建的数据必须能被用例或报告识别。

## 五、ApiClient调用标准

所有HTTP调用必须使用 `auto_test.core.api_client.ApiClient`：

```python
response = api_client.get("/resource", params={"id": resource_id})
response = api_client.post("/resource", json=payload)
response = api_client.put("/resource", json=payload)
response = api_client.patch("/resource", json=payload)
response = api_client.delete("/resource", params={"id": resource_id})
body = api_client.json(response)
```

禁止：

```python
requests.get(...)
requests.post(...)
requests.Session()
```

基座统一负责：

- Base URL拼接。
- `X-Access-Token` 注入。
- 连接与读取超时。
- SSL校验配置。
- 请求和响应结构化日志。
- Header、参数和请求体敏感字段脱敏。
- 网络异常封装为 `ApiRequestError`。
- 非JSON响应解析异常封装为 `ApiResponseDecodeError`。
- HTTP 401后的Token刷新扩展点和最多一次重试。

用例不得绕开上述能力。若基座缺少通用能力，应提出基座修改建议，不得在单个用例中复制实现。

## 六、测试场景组织

每个接口至少评估以下场景：

| 类型 | 覆盖内容 |
|---|---|
| 正常 | 合法参数、正确权限、核心业务结果 |
| 必填 | 缺失、空字符串、null |
| 类型 | 非法类型、格式错误 |
| 边界 | 最小值、最大值、分页边界、长度边界 |
| 枚举 | 合法枚举、未知枚举 |
| 权限 | 未登录、Token失效、角色无权、数据越权 |
| 幂等 | 重复请求、相同业务主键、回放 |
| 并发 | 重复创建、资源竞争、状态冲突 |
| 状态 | 合法状态、非法跳转、已完成或已取消对象 |
| 外部依赖 | 超时、失败、重复回调、乱序回调 |

实际场景必须以知识库和OpenAPI为依据，不能为了补齐表格而编造业务行为。

复杂数据使用 `pytest.mark.parametrize` 或抽离到 `test_api/data`，禁止在测试函数中堆放大段JSON。

## 七、断言标准

### 7.1 两层必选断言

每个业务接口用例至少包含：

1. 协议层：HTTP状态码、必要响应头、响应可解析性。
2. 业务层：业务成功标识或业务码、关键字段、状态或资源变化。

```python
response = api_client.post("/path/from-openapi", json=payload)
assert response.status_code == 200

body = api_client.json(response)
assert body["success"] is True
assert body["result"]["id"]
```

字段名称必须来自实际OpenAPI响应模型，示例不得直接复制为业务事实。

### 7.2 一致性断言

涉及需求、任务、容器、储位和车辆状态时，应根据知识库决定是否增加：

- 查询接口二次校验。
- 数据库状态校验。
- 状态历史校验。
- 外部系统调用日志校验。
- 资源占用和释放校验。

数据库关联以 `knowledge/05_reference/database/` 为准。DDL未声明的软关联必须经代码或实际数据确认。

### 7.3 异常断言

- 禁止只写 `assert response.status_code != 200`。
- 必须验证明确的HTTP状态、业务码或错误字段。
- 业务错误码未在知识库声明时，应标注缺口，不得编造预期码。

## 八、等待、重试与数据清理

1. 禁止使用 `time.sleep()`。
2. 轮询必须设置总超时、间隔、终止条件和超时错误信息。
3. 只有明确可重试的网络或最终一致性场景才允许重试。
4. 创建型用例必须考虑数据清理；清理失败应记录到执行结果。
5. 禁止通过直接修改数据库绕过业务接口，除非测试方案明确授权。

## 九、日志标准

`ApiClient`自动记录：

- HTTP方法和完整请求URL。
- 脱敏后的请求Header。
- Query参数和请求体。
- HTTP状态码和响应体。
- 请求耗时。
- 网络异常和堆栈。

敏感字段必须脱敏，至少包括：

- `Authorization`
- `X-Access-Token`
- `Cookie`
- `token`
- `password`
- `secret`

测试代码不得使用 `print()` 输出请求、响应或凭证，应使用项目统一logger。

## 十、结构化结果与知识回流

pytest执行结果默认写入：

```text
auto_test/artifacts/<run-id>/
└── results/
    ├── results-<run-id>.jsonl
    └── summary-<run-id>.json
```

单用例结果字段：

| 字段 | 含义 |
|---|---|
| `nodeid` | pytest用例唯一标识 |
| `name` | 测试函数名 |
| `status` | `passed`、`failed`、`skipped`或`error` |
| `duration_seconds` | 执行耗时 |
| `started_at`、`finished_at` | UTC时间 |
| `business_scenario` | `scenario`标记提供的场景 |
| `knowledge_paths` | `knowledge`标记提供的依据 |
| `error`、`traceback` | 失败信息和堆栈 |
| `artifacts` | 截图等产物路径 |

用例必须使用知识标记建立可追溯关系：

```python
@pytest.mark.knowledge(
    "knowledge/02_state_machine/demand_flow.md",
    "knowledge/04_constraint_rule/data_consistency_rule.md",
)
@pytest.mark.scenario("需求重复下发幂等校验")
```

报告中的 `feedback_target` 固定指向 `knowledge/test_feedback/`。报告只是回流数据源，不允许测试代码直接修改知识库；回流前必须分类和人工审核：

- 业务场景缺失 → `uncovered_scenario.md`
- 历史缺陷 → `bug_history.md`
- 自动化不稳定或基座问题 → `automation_optimize.md`

## 十一、pytest标记

| 标记 | 用途 |
|---|---|
| `@pytest.mark.api_tms` | TMS接口用例 |
| `@pytest.mark.smoke` | 核心冒烟 |
| `@pytest.mark.e2e` | 端到端或跨系统联调 |
| `@pytest.mark.knowledge(*paths)` | 关联知识文档 |
| `@pytest.mark.scenario(name)` | 业务场景名称 |

标记必须反映真实测试范围，禁止所有用例无差别添加 `smoke` 或 `e2e`。

## 十二、Codex生成API代码强制约束

Codex生成或修改API测试前必须：

1. 读取 `knowledge/KNOWLEDGE_INDEX.md`。
2. 读取本规范。
3. 按索引读取对应业务、状态机、约束、OpenAPI和测试反馈文档。
4. 检查目标接口的URL、方法、参数位置、请求模型和响应模型。
5. 明确知识库是否足以支持预期结果。

Codex允许：

- 在 `auto_test/test_api/` 中生成或修改TMS测试用例。
- 在 `auto_test/test_api/data/` 中增加非敏感测试数据。
- 使用现有fixture、ApiClient、marker和报告能力。

Codex禁止：

- 裸用requests或创建Session。
- 硬编码地址、账号、Token、密码和长期固定业务单号。
- 修改业务状态机或伪造业务规则使测试通过。
- 根据接口名猜测业务码、状态值和错误提示。
- 为单个用例复制通用重试、日志或报告逻辑。
- 自动写入 `knowledge/test_feedback/`，未经执行证据和人工审核不得回流。
- 在用户仅要求生成测试时，擅自修改 `core`、`conftest.py` 或配置结构。

如果缺少接口、fixture或业务依据，Codex必须停止生成相关逻辑并明确输出：

```text
阻塞原因：知识库或基座缺少……
需要补充：……
禁止采取：自行推断或绕开公共封装。
```

## 十三、代码评审清单

- [ ] 已关联知识库文档和明确业务场景。
- [ ] 只使用fixture注入的ApiClient。
- [ ] 没有明文地址、账号和凭证。
- [ ] 包含协议层与业务层断言。
- [ ] 异常预期来自知识库或OpenAPI。
- [ ] 没有 `time.sleep()` 和无边界重试。
- [ ] 测试数据可识别、可清理、互不污染。
- [ ] 日志不会泄露敏感信息。
- [ ] 失败信息足以进入结构化报告并支持问题分类。
