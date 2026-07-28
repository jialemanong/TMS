# TMS 自动化测试基座

技术栈：Python、pytest、requests、Playwright。

当前目录包含自动化基础设施、人工维护的TMS任务池POM和技术冒烟验证，
不包含TMS业务流程用例。

## 1. 前置条件

- Python 3.9+
- 可访问Python包源
- 首次执行UI测试时可下载Playwright Chromium

业务测试开发前必须先读取：

- `../knowledge/KNOWLEDGE_INDEX.md`
- `../knowledge/06_auto_test_spec/api_code_spec.md`
- `../knowledge/06_auto_test_spec/ui_code_spec.md`

## 2. 安装

在仓库根目录执行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r auto_test/requirements.txt
python -m playwright install chromium
```

如果本机配置的Playwright镜像提示压缩包损坏，可临时使用官方源：

```bash
PLAYWRIGHT_DOWNLOAD_HOST=https://cdn.playwright.dev \
  python -m playwright install chromium
```

确认浏览器安装状态：

```bash
python -m playwright install --list
```

Playwright浏览器运行包只供自动化使用，不会替换系统默认浏览器。

## 3. 环境配置

配置模板位于 `config/env.yaml`。地址、账号和Token通过环境变量注入：

```bash
export TMS_API_BASE_URL="http://your-api-host"
export TMS_ACCESS_TOKEN="your-token"
export TMS_UI_BASE_URL="http://your-ui-host"
export TMS_UI_USERNAME="your-username"
export TMS_UI_PASSWORD="your-password"
```

禁止把真实账号、密码、Token或生产环境地址提交到仓库。

需要登录的UI用例统一使用 `tms_authenticated_page` fixture。该fixture会：

- 从环境变量读取账号和密码；
- 每次识别前点击验证码图片刷新，并等待图片内容变化；
- 使用 `ddddocr` 识别四位验证码并自动填写；
- 验证码错误、过期或识别失败时最多重试3次；
- 登录成功后返回由pytest统一管理的 `Page`。

OCR能力仅用于已授权的TMS测试环境。POM中只保留登录页原子操作，
登录重试由基础认证组件统一管理。

登录后页面统一通过 `tms_pages` fixture 获取，例如：

```python
def example(tms_pages):
    tms_pages.demand_pool.open()
    tms_pages.container_task_pool.open()
```

这里只展示fixture调用方式，不是业务测试用例。`tms_pages` 当前覆盖测试账号
登录后可见的27个叶子页面，包括基础配置、规则、任务池、日志、监控和参数配置。

## 4. 运行任务调度链路试点

试点用例只读查询已经完成车辆分配的容器任务和车辆任务。业务数据从
`config/test_data/task_dispatch.yaml` 加载，启动命令不再传递业务单号：

```bash
python -m pytest -c auto_test/pytest.ini \
  auto_test/test_ui/test_tms_task_dispatch_trace.py \
  --env=test --headed --slowmo=800
```

执行结果、知识库路径、场景名称、失败截图和录屏会由基座写入
`auto_test/artifacts/<run-id>/`。

## 5. 测试数据维护规范

业务测试数据与环境配置必须隔离：

```text
auto_test/config/
├── env.yaml
└── test_data/
    └── <business_module>.yaml
```

- `env.yaml` 只保存环境地址、账号、凭证引用、浏览器和超时等环境参数。
- 运单号、任务号、容器号等业务数据只能保存在 `config/test_data/`。
- 每个YAML文件对应一个业务模块，并必须包含 `normal`、`abnormal`、
  `boundary` 三类场景。
- 场景下以稳定的用例名称保存数据；数据失效时评审并更新对应YAML。
- 测试用例禁止直接读取YAML、环境变量或硬编码业务单据。
- 测试用例只能通过 `conftest.py` 提供的Fixture获取业务数据。
- Codex新增用例时应复用 `test_data_loader`，并为具体场景提供语义化Fixture。
- 数据用例应记录 `description` 和对应的 `knowledge_paths`，便于维护和回流。

标准数据结构：

```yaml
normal:
  case_name:
    description: 正向场景说明
    knowledge_paths:
      - knowledge/对应文档.md
    business_field: value

abnormal: {}

boundary: {}
```

统一加载入口为 `auto_test.utils.data_loader.TestDataLoader`。Fixture示例：

```python
@pytest.fixture
def module_case_data(test_data_loader):
    return test_data_loader.load_case("module_name", "normal", "case_name")
```

`load_module()`、`load_scenario()` 和 `load_case()` 返回隔离副本，用例修改
数据不会污染其他用例。模块、场景或用例不存在时会抛出明确的数据错误。

## 6. 运行最小验证

API基础封装冒烟不访问网络，使用受控的伪Session验证请求生命周期：

```bash
python -m pytest -c auto_test/pytest.ini auto_test/test_api/test_smoke_api_client.py
```

浏览器基础封装冒烟使用本地HTML，不访问TMS业务系统：

```bash
python -m pytest -c auto_test/pytest.ini auto_test/test_ui/test_smoke_browser_base.py
```

如尚未安装Playwright Chromium，可先运行API冒烟和用例收集；UI冒烟需在浏览器包安装完成后执行。

执行全部基础冒烟：

```bash
python -m pytest -c auto_test/pytest.ini auto_test
```

显示浏览器：

```bash
python -m pytest -c auto_test/pytest.ini auto_test/test_ui --headed
```

选择环境：

```bash
python -m pytest -c auto_test/pytest.ini auto_test --env=test
```

## 7. 执行产物

默认输出到 `auto_test/artifacts/<run-id>/`：

- `screenshots/`：UI失败截图及主动截图
- `videos/`：每个Playwright上下文录屏
- `results/results-*.jsonl`：逐用例结构化结果
- `results/summary-*.json`：本次运行汇总

结果结构预留 `business_scenario`、`knowledge_paths`、`artifacts` 和
`feedback_target` 字段，后续可转换并回流到 `knowledge/test_feedback/`。

## 8. 扩展边界

- API用例只能使用fixture注入的 `api_client`。
- 浏览器、Context和Page只能由pytest fixture管理。
- UI流程脚本不得直接写定位器，后续必须调用人工维护的POM。
- 业务测试数据只能通过数据Fixture注入，禁止在脚本中写死业务单据。
- POM定位与原子操作由人工维护，业务流程只能在后续阶段通过POM编排。
