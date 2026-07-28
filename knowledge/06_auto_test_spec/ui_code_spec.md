# TMS UI自动化与POM开发规范

> 规范级别：强制
>
> 适用系统：TMS
>
> 技术栈：Python + pytest + Playwright
>
> 基座目录：`auto_test/`
>
> 业务知识入口：`knowledge/KNOWLEDGE_INDEX.md`

## 一、核心原则

TMS UI自动化采用人工维护POM、Codex编排业务流程的协作模式：

```text
人工维护页面定位和原子操作
            ↓
稳定的POM公开方法
            ↓
Codex仅调用POM编排test_ui业务流程
```

最高优先级边界：

1. POM页面层及元素定位由人工创建、评审和维护。
2. Codex只允许生成或修改 `auto_test/test_ui/` 中的业务流程用例。
3. Codex禁止新增、修改或绕开POM中的任何元素定位代码。
4. UI用例禁止直接调用 `locator()`、`get_by_*()`、XPath或CSS选择器。
5. POM能力不足时必须提出“待人工扩充POM”，禁止在用例中临时定位元素。

## 二、工程分层

当前基座：

```text
auto_test/
├── conftest.py
├── config/
│   └── env.yaml
├── core/
│   ├── browser_base.py
│   └── reporter.py
└── test_ui/
```

进入POM阶段后的目标结构：

```text
auto_test/
├── pom/
│   └── tms/
│       ├── base_page.py
│       └── <business>_page.py
├── test_ui/
│   ├── data/
│   └── test_tms_<module>_<flow>.py
└── conftest.py
```

| 层级 | 责任人 | 允许内容 | 禁止内容 |
|---|---|---|---|
| `core/browser_base.py` | 基座维护者 | 导航、加载等待、截图等通用能力 | 业务元素和业务流程 |
| `pom/tms` | 人工 | 定位器、页面状态、原子操作 | 跨页面完整业务流程 |
| `test_ui` | Codex/人工 | 调用POM编排流程、业务断言 | 任何元素定位代码 |
| `conftest.py` | 基座维护者 | Browser、Context、Page和POM fixture | 具体业务流程 |

## 三、POM人工维护规范

### 3.1 Page类

- 类名采用大驼峰：`<Business>Page`。
- 文件名采用小写下划线：`<business>_page.py`。
- 每个Page类对应一个明确页面或稳定功能区域。
- Page类应复用统一基础类或 `BrowserBase` 能力，不自行启动浏览器。

示例名称：

```text
TransportOrderPage
DemandPoolPage
ContainerTaskPage
```

名称只表示编码形式，不代表知识库已确认具体页面。

### 3.2 POM公开方法

公开方法以动词开头，表达业务可读的原子动作：

```text
open()
search_by_order_no()
fill_required_fields()
submit()
confirm_dialog()
get_status_text()
wait_until_loaded()
```

规则：

1. 方法只完成一个原子动作或一个稳定的小型页面操作。
2. 方法参数传入测试数据，不硬编码业务单号。
3. 查询方法返回可断言的文本、值或领域数据，避免把Locator直接暴露给用例。
4. 方法内部负责必要的页面加载和控件可操作等待。
5. 禁止在POM中完成跨页面端到端流程。

### 3.3 定位优先级

仅人工维护POM时允许写定位器，优先级如下：

1. `get_by_role()` 配合稳定可访问名称。
2. `get_by_label()`。
3. `get_by_test_id()`。
4. `get_by_placeholder()`。
5. `get_by_text()`，仅用于稳定且唯一文本。
6. 稳定CSS属性。
7. XPath，仅在无稳定语义或属性方案时使用。

禁止使用：

- 基于DOM层级的长CSS链。
- 带动态序号的XPath。
- 依赖构建产物随机class。
- 未验证唯一性的模糊文本定位。

### 3.4 定位变更评审

POM定位变更必须由人工确认：

- 元素是否唯一。
- 是否有更稳定的语义定位。
- 是否影响其他流程。
- 是否需要同步修改页面方法契约。
- 是否来自真实页面变化，而非用例等待不足。

## 四、Fixture与浏览器生命周期

浏览器实例必须由 `auto_test/conftest.py` 和 `pytest-playwright` 管理。

现有fixture：

| Fixture | Scope | 用途 |
|---|---|---|
| `settings` | session | UI地址、浏览器配置 |
| `artifact_dir` | session | 本次执行产物目录 |
| `browser_type` | session | 浏览器类型 |
| `browser_type_launch_args` | session | headless、slow_mo |
| `browser_context_args` | session | viewport、HTTPS和录屏 |
| `page` | function | pytest-playwright提供的Page |
| `browser_base` | function | 基于Page的通用封装 |

规则：

1. 用例和POM禁止调用 `sync_playwright()`。
2. 禁止自行执行 `browser.launch()`、`new_context()` 或 `new_page()`。
3. 页面对象fixture应基于公共 `page` 或 `browser_base` 创建。
4. 登录状态需要复用时，应由人工设计session/context级fixture或storage state。
5. Fixture创建的数据和状态必须在结束时清理，避免用例互相污染。
6. 禁止把账号和密码写入fixture，必须从 `settings` 获取。

未来POM fixture形式：

```python
@pytest.fixture
def transport_order_page(browser_base):
    return TransportOrderPage(browser_base)
```

该示例仅说明fixture方式，Page类必须在POM人工封装阶段由人工实现。

## 五、浏览器基础能力

`auto_test.core.browser_base.BrowserBase` 当前提供：

- 基于配置地址的页面导航。
- 文档加载完成等待。
- 主动截图。
- 截图产物目录管理。

`conftest.py` 当前提供：

- 浏览器类型和headed/headless控制。
- viewport配置。
- HTTPS错误处理配置。
- 每个Context自动录屏。
- 测试失败时自动全页截图。
- 结构化结果记录。

通用能力应优先补充到基座或人工POM，禁止在各用例中复制。

## 六、等待规则

1. 严禁 `time.sleep()`。
2. 优先使用Playwright自动等待。
3. 页面状态断言使用Playwright `expect()`。
4. 页面加载使用 `wait_for_load_state()` 或POM统一的loading等待。
5. 等待必须针对可观察状态，例如元素可见、按钮可用、请求完成或状态文本变化。
6. 禁止用固定延时掩盖定位不稳定、接口慢或页面错误。
7. 所有显式等待必须有合理超时和可诊断错误。

## 七、UI用例命名与结构

### 7.1 文件和函数

- 文件：`test_tms_<模块>_<流程>.py`
- 函数：`test_<业务场景>_<预期>`
- 类可选：`Test<Module><Flow>`

示例：

```text
test_tms_transport_order_create.py
test_transport_order_create_success
test_transport_order_create_required_field_missing
```

### 7.2 用例标准结构

```python
import pytest


@pytest.mark.ui_tms
@pytest.mark.knowledge("knowledge/对应业务文档.md")
@pytest.mark.scenario("明确的TMS前端业务场景")
def test_example_flow(example_page):
    """场景：填写实际场景；前置：填写前置；预期：填写业务结果。"""
    # Given：只通过POM准备页面状态
    example_page.open()

    # When：只调用POM公开方法执行操作
    example_page.perform_action()

    # Then：通过POM查询方法返回结果后断言
    assert example_page.get_result_text() == "来自知识库或需求的明确预期"
```

示例中的类和方法为结构占位，不得当作已存在POM使用。

每个用例必须包含：

- docstring：业务场景、前置条件、预期结果。
- Given/When/Then或等价清晰结构。
- `knowledge`和`scenario`标记。
- 可独立识别和清理的测试数据。
- 明确的UI或后端业务断言。

## 八、UI断言标准

### 8.1 页面断言

POM内部可以使用Playwright `expect()` 验证页面级状态；测试用例通过POM公开查询或断言方法验证：

- 页面标题或区域是否出现。
- 表单值是否正确。
- 提交成功或失败提示。
- 列表中是否存在目标数据。
- 状态文本是否符合知识库定义。
- 按钮在当前状态下是否可用。

### 8.2 业务断言

不能只断言“页面无报错”或“按钮点击成功”。关键流程至少验证一个业务结果：

- UI列表或详情中的关键字段。
- 状态变化。
- 操作后的资源关系。
- 必要时通过 `api_client` 查询后端结果。

UI与API联合断言时，API调用仍必须使用fixture注入的 `api_client`。

### 8.3 异常断言

- 明确验证错误提示或禁止操作状态。
- 错误文案未在知识库明确时，不得猜测完整文案。
- 可验证错误类别、业务码或稳定关键词时，应在测试依据中说明。

## 九、环境与测试数据

1. UI地址、账号和密码来自 `auto_test/config/env.yaml` 对应的环境变量。
2. 禁止提交真实凭证和生产环境地址。
3. 禁止写死长期不变的业务单号、容器号和任务号。
4. 测试数据应带可识别前缀或运行ID，便于检索和清理。
5. 用例不得依赖执行顺序。
6. 用例不得默认依赖其他用例留下的数据。
7. 数据准备规则不明确时，先补知识库或测试数据方案。

## 十、截图、录屏与日志

默认产物结构：

```text
auto_test/artifacts/<run-id>/
├── screenshots/
├── videos/
└── results/
    ├── results-<run-id>.jsonl
    └── summary-<run-id>.json
```

规则：

1. UI失败由pytest钩子自动截取全页截图。
2. Browser Context通过fixture自动录屏，禁止用例自行控制录屏生命周期。
3. 关键业务节点可调用 `browser_base.capture_screenshot()` 主动截图，但不能滥用。
4. 截图名称应包含场景或步骤，不含账号、Token等敏感信息。
5. 页面跳转和截图由统一logger记录。
6. 用例禁止使用 `print()` 代替日志。

## 十一、结构化结果与知识回流

UI执行使用与API一致的结果模型：

| 字段 | UI用途 |
|---|---|
| `nodeid`、`name` | 定位失败用例 |
| `status` | 区分通过、失败、跳过和基础设施错误 |
| `business_scenario` | 描述业务流程 |
| `knowledge_paths` | 追踪状态机、流程和约束依据 |
| `error`、`traceback` | 定位断言或运行异常 |
| `artifacts.screenshot` | 失败页面证据 |
| `duration_seconds` | 识别慢用例 |

录屏存放在同一运行目录的 `videos/`。后续回流必须先判断失败类别：

| 失败类别 | 回流目标 |
|---|---|
| 知识库缺少业务分支 | `knowledge/test_feedback/uncovered_scenario.md` |
| 确认的产品缺陷 | `knowledge/test_feedback/bug_history.md` |
| 定位、等待、数据或环境不稳定 | `knowledge/test_feedback/automation_optimize.md` |

禁止看到失败就自动认定为产品缺陷。回流需要执行证据、失败分类和人工审核。

## 十二、pytest标记

| 标记 | 用途 |
|---|---|
| `@pytest.mark.ui_tms` | TMS UI业务用例 |
| `@pytest.mark.smoke` | 核心前端冒烟 |
| `@pytest.mark.e2e` | 完整端到端流程 |
| `@pytest.mark.knowledge(*paths)` | 关联知识文档 |
| `@pytest.mark.scenario(name)` | 业务场景名称 |

## 十三、人工与Codex权责边界

### 13.1 人工负责

- 观察真实页面和确认稳定定位方式。
- 创建、修改和评审 `auto_test/pom/`。
- 定义POM公开方法及返回值。
- 处理页面结构变化和定位器失效。
- 确认登录策略、测试数据策略和环境权限。
- 审核Codex生成流程是否符合业务知识。

### 13.2 Codex允许

- 读取已有POM公开方法。
- 在 `auto_test/test_ui/` 生成或修改业务流程用例。
- 在 `auto_test/test_ui/data/` 创建非敏感测试数据。
- 调用现有fixture、POM、`api_client`和pytest marker。
- 在发现POM缺口时输出待人工补充的方法清单。

### 13.3 Codex禁止

- 新增、修改、删除 `auto_test/pom/` 中的代码。
- 在 `test_ui` 中写 `locator()`、`get_by_*()`、XPath、CSS或DOM查询。
- 通过 `page`、`browser_base.page` 绕过POM执行页面业务操作。
- 自行启动Browser、Context或Page。
- 因用例失败而擅自修改定位器。
- 猜测页面元素文本、按钮名称和页面路径。
- 硬编码地址、账号、密码、Token和业务数据。
- 为使测试通过而弱化或删除业务断言。
- 未经执行和人工审核直接修改 `knowledge/test_feedback/`。

## 十四、Codex生成UI代码工作流

生成前必须：

1. 读取 `knowledge/KNOWLEDGE_INDEX.md`。
2. 读取本规范。
3. 读取目标业务主流程、异常流程、状态机、约束和测试反馈。
4. 读取已有POM公开方法，不读取后自行猜测方法。
5. 对照流程步骤检查POM能力是否完整。

若POM能力完整：

1. 仅在 `test_ui` 编排流程。
2. 增加规范marker和docstring。
3. 添加UI层和必要的API层业务断言。
4. 本地执行并保留结构化报告、截图和录屏。

若POM能力不完整，必须停止生成缺失步骤并输出：

```text
待人工扩充POM
- 页面类：<已存在页面类或待人工确认>
- 建议方法：<方法名和输入输出>
- 业务用途：<对应流程步骤>
- 依据文档：<知识库路径>

禁止操作：Codex不得自行添加定位器或修改POM。
```

## 十五、代码评审清单

- [ ] 用例只调用人工维护的POM方法。
- [ ] `test_ui` 中不存在Locator、XPath、CSS或 `get_by_*()`。
- [ ] Browser、Context和Page全部来自fixture。
- [ ] 没有 `time.sleep()`。
- [ ] 用例关联业务文档和场景名称。
- [ ] 断言覆盖真实业务结果，不只是页面可见。
- [ ] 地址、账号和测试数据没有硬编码。
- [ ] 失败可产生截图、录屏和结构化结果。
- [ ] POM缺口已明确交还人工处理。
- [ ] 执行结果回流前经过失败分类和人工审核。
