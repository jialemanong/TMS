# TMS 自动化测试基座

技术栈：Python、pytest、requests、Playwright。

当前目录仅包含自动化基础设施和技术冒烟验证，不包含TMS业务用例、页面POM或页面定位。

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

## 4. 运行最小验证

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

## 5. 执行产物

默认输出到 `auto_test/artifacts/<run-id>/`：

- `screenshots/`：UI失败截图及主动截图
- `videos/`：每个Playwright上下文录屏
- `results/results-*.jsonl`：逐用例结构化结果
- `results/summary-*.json`：本次运行汇总

结果结构预留 `business_scenario`、`knowledge_paths`、`artifacts` 和
`feedback_target` 字段，后续可转换并回流到 `knowledge/test_feedback/`。

## 6. 扩展边界

- API用例只能使用fixture注入的 `api_client`。
- 浏览器、Context和Page只能由pytest fixture管理。
- UI流程脚本不得直接写定位器，后续必须调用人工维护的POM。
- 当前阶段禁止增加TMS业务流程脚本和POM。
