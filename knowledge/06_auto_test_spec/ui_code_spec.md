# TMS UI自动化 & POM开发规范
技术栈：Python + pytest + Playwright
适用范围：TMS前端页面自动化；人工POM封装标准、Codex生成Web业务脚本强制规范

## 1. 分层架构（POM严格分层，AI边界核心）
auto_test/
├── pom/
│   └── tms/                 # TMS页面对象层（人工维护，禁止AI修改/新增）
├── test_ui/                 # TMS业务流程用例层（Codex主要产出物）

### 分层职责硬性划分
1. Pom页面类：仅包含元素定位、原子操作（输入、点击、查询、弹窗确认等）
   - 只封装原子动作，不编排完整业务流程
2. Test用例：编排完整业务流程
   - ❗ 【最高优先级约束】UI测试脚本**禁止直接编写Locator、xpath、get_by_xxx定位代码**
   - 所有页面操作，只能调用已封装Pom实例方法

> 核心设计目的：人工维护稳定页面元素，AI只生成业务流程，避免AI频繁写出脆弱定位器

## 2. 命名规范
1. Page类：大驼峰，业务+Page
示例：`TransportOrderPage`（TMS运单页面）、`DispatchPage`（调度页面）
2. 页面方法：动词开头
示例：`input_order_no()`、`search()`、`submit()`、`wait_loading()`
3. 测试文件：`test_tms_业务模块_流程名称.py`
示例：`test_tms_transport_order_crud.py`
4. 测试函数：`test_业务场景_描述`
示例：`test_transport_order_create_and_search`

## 3. Playwright基础编码约束
1. Browser/Context由全局fixture统一管理，复用浏览器上下文；统一失败截图、录屏
2. 定位优先级：语义定位 `get_by_role / get_by_text > get_by_placeholder`，谨慎使用xpath/css
3. 严禁使用 `time.sleep()`；全部使用playwright显式等待 `expect()` / wait_for_xxx
4. 页面加载、loading等待统一封装至基础BasePage父类，不要每个页面重复实现

## 4. 断言规范
1. 界面元素断言：使用playwright原生expect断言
2. 业务结果断言：分为两类
   - UI层：页面文本、列表数据校验
   - 可选增强：UI操作完成后调用TMS接口校验后端数据一致性
3. 断言失败时，自动携带截图链路信息，用于回流知识库

## 5. 环境与数据规范
1. 登录账号、系统地址从 `config/env.yaml` 读取，禁止硬编码
2. 测试业务数据尽量解耦，可外部传入；禁止用例写死长期不变业务单号
3. 登录逻辑封装至公共fixture，用例只关注业务流程

## 6. AI（Codex）生成代码强制约束【重中之重】
1. Codex仅允许生成 `test_ui` 下业务流程用例，**不允许修改、新增pom目录代码**
2. 生成代码只能调用现有Pom中已定义方法；如果缺少所需方法，在注释中标记待人工扩充POM，禁止自行写定位
3. 流程步骤需要增加注释，关联知识库业务文档路径，作为业务依据
4. 严格使用项目已有的fixture获取page、页面实例，禁止自行创建Browser
5. 生成用例必须遵循本规范命名、标记规则，自动增加对应pytest mark

## 7. 标记规范
- @pytest.mark.ui_tms TMS前端自动化用例
- @pytest.mark.smoke 核心冒烟流程
- @pytest.mark.e2e 端到端业务流程

## 8. 禁止事项
❌ 在测试用例内直接编写元素定位代码
❌ 大量硬编码xpath、不稳定选择器
❌ 滥用time.sleep
❌ 代码内硬编码地址、账号、业务单号
❌ AI生成代码随意新增页面类与定位器
❌ 流程步骤缺少注释、无法追溯对应业务规则