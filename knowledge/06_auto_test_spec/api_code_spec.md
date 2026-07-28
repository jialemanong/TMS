# TMS API自动化代码开发规范
技术栈：Python + pytest + requests
适用范围：TMS系统接口自动化、上下游外部对接接口用例；同时作为 Codex 生成API测试代码强制约束标准

## 1. 工程分层规范
auto_test/
├── config/                 # 环境配置、账号、基础参数
├── core/
│   ├── api_client.py       # 统一http请求封装，禁止业务代码直接import requests
│   └── reporter.py         # 执行结果结构化输出（支撑结果回流知识库）
├── test_api/
│   └── test_tms/           # TMS接口测试用例
└── utils/

### 文件命名规则
测试用例文件：`test_tms_模块名称.py`
示例：`test_tms_transport_order.py`
测试函数：`test_场景标识_正常/异常`
示例：`test_create_transport_order_normal`、`test_create_transport_order_param_error`

## 2. 基础封装约束
1. 所有HTTP请求必须调用 `core.api_client` 封装实例，禁止裸写 requests.get/post
2. 统一封装能力：自动Token续签、统一超时、统一日志、统一异常捕获、响应格式化解析
3. 环境地址、密钥、账号全部存放 `env.yaml`，代码内**严禁硬编码域名、账号、凭证**
4. 禁止在测试用例内部重复构造session，请求实例由conftest全局fixture注入

## 3. 用例编写标准
1. 业务场景优先拆分，使用 `@pytest.mark.parametrize` 区分正常场景、边界场景、异常场景
2. 断言两层校验：
   - 基础：HTTP状态码
   - 核心：业务返回码、业务关键字段（禁止仅校验status_code=200）
3. 每个用例必须增加docstring，写明：业务场景、前置条件、预期结果（AI识别、人工维护双友好）
4. 复杂报文统一抽离到data目录，不要大段JSON内嵌在测试函数内

## 4. 日志 & 输出规范（关键：支撑结果回流知识库）
1. 每次请求强制输出：接口路径、请求头、入参、响应体、耗时
2. 用例执行完成输出结构化JSON信息：
    - 用例名称、执行状态、报错信息、业务场景、关联知识库文档路径
3. 失败用例必须完整捕获堆栈、原始报文，用于自动回填知识库 `test_feedback`

## 5. AI（Codex）生成代码强制约束
> 下发给Codex指令时必须附带本规范
1. 不得重新导入requests自建请求逻辑，只能复用项目现有 `ApiClient`
2. 严格遵守命名规范、fixture注入方式，禁止自创初始化逻辑
3. 生成用例必须读取配置文件，禁止硬编码地址、账号
4. 生成代码需要引用知识库对应业务文档路径，在注释中标注业务依据来源
5. 异常场景优先参考知识库内 `04_constraint_rule`、业务约束文档构造

## 6. 标记规范
使用pytest mark做用例分类：
- @pytest.mark.api_tms TMS接口用例
- @pytest.mark.smoke 冒烟用例
- @pytest.mark.e2e 端到端联调用例

## 7. 禁止事项
❌ 使用time.sleep()处理接口轮询；统一封装轮询工具方法
❌ 业务逻辑与请求代码耦合
❌ 生产环境地址、密钥提交至代码仓库
❌ 断言只判断HTTP状态码，忽略业务返回码