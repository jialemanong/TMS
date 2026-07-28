# 系统管理与权限接口明细

> 来源：`../raw/jeecg-system.swagger.json`。本文由生成器自动生成，请勿手工修改生成区内容。

## 服务信息

- 服务标识：`jeecg-system`
- 网关地址：`http://111.160.91.170:59999`
- Base Path：`/jeecg-system`
- 鉴权头：`X-Access-Token`
- 路径数：84
- 接口操作数：95
- 数据模型数：31

## 控制器索引

| 控制器/标签 | 接口数 |
|---|---:|
| 编码校验规则 | 8 |
| 表单评论文件 | 7 |
| 部门角色 | 7 |
| 部门权限表 | 7 |
| 定时任务接口 | 2 |
| 多数据源管理 | 7 |
| 角色首页配置 | 8 |
| 数据字典 | 1 |
| 填值规则 | 7 |
| 系统评论回复表 | 12 |
| 用户登录 | 6 |
| 知识库-文档管理 | 7 |
| 职务表 | 8 |
| 重复校验 | 1 |
| tms_pda_permission | 7 |

## 接口清单

### 编码校验规则

#### POST /jeecg-system/sys/checkRule/add

- 名称：编码校验规则-添加
- Operation ID：`addUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysCheckRule | body | 是 | sys_check_rule对象 | sysCheckRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/checkRule/checkByCode

- 名称：编码校验规则-通过Code校验传入的值
- Operation ID：`checkByCodeUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ruleCode | query | 是 | string | ruleCode |
| value | query | 是 | string | value |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/checkRule/delete

- 名称：编码校验规则-通过id删除
- Operation ID：`deleteUsingDELETE`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/checkRule/deleteBatch

- 名称：编码校验规则-批量删除
- Operation ID：`deleteBatchUsingDELETE`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/checkRule/edit

- 名称：编码校验规则-编辑
- Operation ID：`editUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysCheckRule | body | 是 | sys_check_rule对象 | sysCheckRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/checkRule/edit

- 名称：编码校验规则-编辑
- Operation ID：`editUsingPUT`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysCheckRule | body | 是 | sys_check_rule对象 | sysCheckRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/checkRule/list

- 名称：编码校验规则-分页列表查询
- Operation ID：`queryPageListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | 主键id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| ruleCode | query | 否 | string | 规则Code |
| ruleDescription | query | 否 | string | 规则描述 |
| ruleJson | query | 否 | string | 规则JSON |
| ruleName | query | 否 | string | 规则名称 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/checkRule/queryById

- 名称：编码校验规则-通过id查询
- Operation ID：`queryByIdUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 表单评论文件

#### POST /jeecg-system/sys/formFile/add

- 名称：表单评论文件-添加
- Operation ID：`addUsingPOST_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFormFile | body | 是 | sys_form_file对象 | sysFormFile |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/formFile/delete

- 名称：表单评论文件-通过id删除
- Operation ID：`deleteUsingDELETE_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/formFile/deleteBatch

- 名称：表单评论文件-批量删除
- Operation ID：`deleteBatchUsingDELETE_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/formFile/edit

- 名称：表单评论文件-编辑
- Operation ID：`editUsingPOST_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFormFile | body | 是 | sys_form_file对象 | sysFormFile |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/formFile/edit

- 名称：表单评论文件-编辑
- Operation ID：`editUsingPUT_7`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFormFile | body | 是 | sys_form_file对象 | sysFormFile |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/formFile/list

- 名称：表单评论文件-分页列表查询
- Operation ID：`queryPageListUsingGET_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人登录名称 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| fileId | query | 否 | string | 关联文件id |
| fileType | query | 否 | string | 文档类型（folder:文件夹 excel:excel doc:word pp:ppt image:图片  archive:其他文档 video:视频） |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| tableDataId | query | 否 | string | 数据id |
| tableName | query | 否 | string | 表名 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/formFile/queryById

- 名称：表单评论文件-通过id查询
- Operation ID：`queryByIdUsingGET_7`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 部门角色

#### POST /jeecg-system/sys/sysDepartRole/add

- 名称：部门角色-添加
- Operation ID：`addUsingPOST_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartRole | body | 是 | sys_depart_role对象 | sysDepartRole |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/sysDepartRole/delete

- 名称：部门角色-通过id删除
- Operation ID：`deleteUsingDELETE_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/sysDepartRole/deleteBatch

- 名称：部门角色-批量删除
- Operation ID：`deleteBatchUsingDELETE_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/sysDepartRole/edit

- 名称：部门角色-编辑
- Operation ID：`editUsingPOST_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartRole | body | 是 | sys_depart_role对象 | sysDepartRole |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/sysDepartRole/edit

- 名称：部门角色-编辑
- Operation ID：`editUsingPUT_4`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartRole | body | 是 | sys_depart_role对象 | sysDepartRole |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysDepartRole/list

- 名称：部门角色-分页列表查询
- Operation ID：`queryPageListUsingGET_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| departId | query | 否 | string | 部门id |
| deptId | query | 否 | string | deptId |
| description | query | 否 | string | 描述 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| roleCode | query | 否 | string | 部门角色编码 |
| roleName | query | 否 | string | 部门角色名称 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysDepartRole/queryById

- 名称：部门角色-通过id查询
- Operation ID：`queryByIdUsingGET_4`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 部门权限表

#### POST /jeecg-system/sys/sysDepartPermission/add

- 名称：部门权限表-添加
- Operation ID：`addUsingPOST_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartPermission | body | 是 | sys_depart_permission对象 | sysDepartPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/sysDepartPermission/delete

- 名称：部门权限表-通过id删除
- Operation ID：`deleteUsingDELETE_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/sysDepartPermission/deleteBatch

- 名称：部门权限表-批量删除
- Operation ID：`deleteBatchUsingDELETE_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/sysDepartPermission/edit

- 名称：部门权限表-编辑
- Operation ID：`editUsingPOST_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartPermission | body | 是 | sys_depart_permission对象 | sysDepartPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/sysDepartPermission/edit

- 名称：部门权限表-编辑
- Operation ID：`editUsingPUT_3`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDepartPermission | body | 是 | sys_depart_permission对象 | sysDepartPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysDepartPermission/list

- 名称：部门权限表-分页列表查询
- Operation ID：`queryPageListUsingGET_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| dataRuleIds | query | 否 | string | 数据规则id |
| departId | query | 否 | string | 部门id |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| permissionId | query | 否 | string | 权限id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysDepartPermission/queryById

- 名称：部门权限表-通过id查询
- Operation ID：`queryByIdUsingGET_3`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 定时任务接口

#### GET /jeecg-system/sys/quartzJob/pause

- 名称：停止定时任务
- Operation ID：`pauseJobUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/quartzJob/resume

- 名称：启动定时任务
- Operation ID：`resumeJobUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 多数据源管理

#### POST /jeecg-system/sys/dataSource/add

- 名称：多数据源管理-添加
- Operation ID：`addUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDataSource | body | 是 | sys_data_source对象 | sysDataSource |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/dataSource/delete

- 名称：多数据源管理-通过id删除
- Operation ID：`deleteUsingDELETE_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/dataSource/deleteBatch

- 名称：多数据源管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/dataSource/edit

- 名称：多数据源管理-编辑
- Operation ID：`editUsingPOST_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDataSource | body | 是 | sys_data_source对象 | sysDataSource |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/dataSource/edit

- 名称：多数据源管理-编辑
- Operation ID：`editUsingPUT_2`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysDataSource | body | 是 | sys_data_source对象 | sysDataSource |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/dataSource/list

- 名称：多数据源管理-分页列表查询
- Operation ID：`queryPageListUsingGET_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 数据源编码 |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| dbDriver | query | 否 | string | 驱动类 |
| dbName | query | 否 | string | 数据库名称 |
| dbPassword | query | 否 | string | 密码 |
| dbType | query | 否 | string | 数据库类型 |
| dbUrl | query | 否 | string | 数据源地址 |
| dbUsername | query | 否 | string | 用户名 |
| id | query | 否 | string | id |
| name | query | 否 | string | 数据源名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| remark | query | 否 | string | 备注 |
| sysOrgCode | query | 否 | string | 所属部门 |
| tenantId | query | 否 | integer(int32) | 租户ID |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/dataSource/queryById

- 名称：多数据源管理-通过id查询
- Operation ID：`queryByIdUsingGET_2`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 角色首页配置

#### POST /jeecg-system/sys/sysRoleIndex/add

- 名称：角色首页配置-添加
- Operation ID：`addUsingPOST_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysRoleIndex | body | 是 | sys_role_index对象 | sysRoleIndex |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/sysRoleIndex/delete

- 名称：角色首页配置-通过id删除
- Operation ID：`deleteUsingDELETE_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/sysRoleIndex/deleteBatch

- 名称：角色首页配置-批量删除
- Operation ID：`deleteBatchUsingDELETE_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/sysRoleIndex/edit

- 名称：角色首页配置-编辑
- Operation ID：`editUsingPOST_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysRoleIndex | body | 是 | sys_role_index对象 | sysRoleIndex |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/sysRoleIndex/edit

- 名称：角色首页配置-编辑
- Operation ID：`editUsingPUT_9`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysRoleIndex | body | 是 | sys_role_index对象 | sysRoleIndex |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysRoleIndex/list

- 名称：角色首页配置-分页列表查询
- Operation ID：`queryPageListUsingGET_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| component | query | 否 | string | 组件 |
| createBy | query | 否 | string | 创建人登录名称 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| priority | query | 否 | integer(int32) | 优先级 |
| roleCode | query | 否 | string | 角色编码 |
| route | query | 否 | boolean | 是否路由菜单 |
| status | query | 否 | string | 状态 |
| sysOrgCode | query | 否 | string | 所属部门 |
| updateBy | query | 否 | string | 更新人登录名称 |
| updateTime | query | 否 | string(date-time) | 更新日期 |
| url | query | 否 | string | 路由地址 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysRoleIndex/queryByCode

- 名称：角色首页配置-通过code查询
- Operation ID：`queryByCodeUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| roleCode | query | 是 | string | roleCode |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/sysRoleIndex/queryById

- 名称：角色首页配置-通过id查询
- Operation ID：`queryByIdUsingGET_9`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 数据字典

#### GET /jeecg-system/sys/dictItem/dictItemCheck

- 名称：字典重复校验接口
- Operation ID：`doDictItemCheckUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | - |
| createTime | query | 否 | string(date-time) | - |
| description | query | 否 | string | - |
| dictId | query | 否 | string | - |
| id | query | 否 | string | - |
| itemText | query | 否 | string | - |
| itemValue | query | 否 | string | - |
| sortOrder | query | 否 | integer(int32) | - |
| status | query | 否 | integer(int32) | - |
| updateBy | query | 否 | string | - |
| updateTime | query | 否 | string(date-time) | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 填值规则

#### POST /jeecg-system/sys/fillRule/add

- 名称：填值规则-添加
- Operation ID：`addUsingPOST_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFillRule | body | 是 | sys_fill_rule对象 | sysFillRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/fillRule/delete

- 名称：填值规则-通过id删除
- Operation ID：`deleteUsingDELETE_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/fillRule/deleteBatch

- 名称：填值规则-批量删除
- Operation ID：`deleteBatchUsingDELETE_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/fillRule/edit

- 名称：填值规则-编辑
- Operation ID：`editUsingPOST_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFillRule | body | 是 | sys_fill_rule对象 | sysFillRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/fillRule/edit

- 名称：填值规则-编辑
- Operation ID：`editUsingPUT_6`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFillRule | body | 是 | sys_fill_rule对象 | sysFillRule |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/fillRule/list

- 名称：填值规则-分页列表查询
- Operation ID：`queryPageListUsingGET_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | 主键ID |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| ruleClass | query | 否 | string | 规则实现类 |
| ruleCode | query | 否 | string | 规则Code |
| ruleName | query | 否 | string | 规则名称 |
| ruleParams | query | 否 | string | 规则参数 |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/fillRule/queryById

- 名称：填值规则-通过id查询
- Operation ID：`queryByIdUsingGET_6`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 系统评论回复表

#### POST /jeecg-system/sys/comment/add

- 名称：系统评论回复表-添加
- Operation ID：`addUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysComment | body | 是 | sys_comment对象 | sysComment |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-system/sys/comment/addFile

- 名称：系统评论表-添加文件
- Operation ID：`addFileUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

_无显式请求参数。_

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-system/sys/comment/addText

- 名称：系统评论表-添加文本
- Operation ID：`addTextUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysComment | body | 是 | sys_comment对象 | sysComment |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/comment/delete

- 名称：系统评论回复表-通过id删除
- Operation ID：`deleteUsingDELETE_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/comment/deleteBatch

- 名称：系统评论回复表-批量删除
- Operation ID：`deleteBatchUsingDELETE_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/comment/deleteOne

- 名称：系统评论回复表-通过id删除
- Operation ID：`deleteOneUsingDELETE`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/comment/edit

- 名称：系统评论回复表-编辑
- Operation ID：`editUsingPOST_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysComment | body | 是 | sys_comment对象 | sysComment |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/comment/edit

- 名称：系统评论回复表-编辑
- Operation ID：`editUsingPUT_1`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysComment | body | 是 | sys_comment对象 | sysComment |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/comment/fileList

- 名称：系统评论回复表-列表查询
- Operation ID：`queryFileListUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| commentContent | query | 否 | string | 回复内容 |
| commentId | query | 否 | string | 评论id(允许为空，不为空时，则为回复) |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| fromUserId | query | 否 | string | 来源用户id |
| id | query | 否 | string | id |
| tableDataId | query | 否 | string | 数据id |
| tableName | query | 否 | string | 表名 |
| toUserId | query | 否 | string | 发送给用户id(允许为空) |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«SysCommentFileVo»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/comment/list

- 名称：系统评论回复表-分页列表查询
- Operation ID：`queryPageListUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| commentContent | query | 否 | string | 回复内容 |
| commentId | query | 否 | string | 评论id(允许为空，不为空时，则为回复) |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| fromUserId | query | 否 | string | 来源用户id |
| id | query | 否 | string | id |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| tableDataId | query | 否 | string | 数据id |
| tableName | query | 否 | string | 表名 |
| toUserId | query | 否 | string | 发送给用户id(允许为空) |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«sys_comment对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/comment/listByForm

- 名称：系统评论回复表-列表查询
- Operation ID：`queryListByFormUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| commentContent | query | 否 | string | 回复内容 |
| commentId | query | 否 | string | 评论id(允许为空，不为空时，则为回复) |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| fromUserId | query | 否 | string | 来源用户id |
| id | query | 否 | string | id |
| tableDataId | query | 否 | string | 数据id |
| tableName | query | 否 | string | 表名 |
| toUserId | query | 否 | string | 发送给用户id(允许为空) |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新日期 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«SysCommentVO»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/comment/queryById

- 名称：系统评论回复表-通过id查询
- Operation ID：`queryByIdUsingGET_1`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_comment对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 用户登录

#### GET /jeecg-system/sys/getLoginQrcode

- 名称：登录二维码
- Operation ID：`getLoginQrcodeUsingGET`
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

#### GET /jeecg-system/sys/getQrcodeToken

- 名称：获取用户扫码后保存的token
- Operation ID：`getQrcodeTokenUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| qrcodeId | query | 是 | string | qrcodeId |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象 | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-system/sys/login

- 名称：登录接口
- Operation ID：`loginUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysLoginModel | body | 是 | 登录对象 | sysLoginModel |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«JSONObject» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-system/sys/phoneLogin

- 名称：手机号登录接口
- Operation ID：`phoneLoginUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| jsonObject | body | 是 | object | jsonObject |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«JSONObject» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/randomImage/{key}

- 名称：获取验证码
- Operation ID：`randomImageUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| key | path | 是 | string | key |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### POST /jeecg-system/sys/scanLoginQrcode

- 名称：扫码登录二维码
- Operation ID：`scanLoginQrcodeUsingPOST`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| qrcodeId | query | 是 | string | qrcodeId |
| token | query | 是 | string | token |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 知识库-文档管理

#### POST /jeecg-system/sys/files/add

- 名称：知识库-文档管理-添加
- Operation ID：`addUsingPOST_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFiles | body | 是 | sys_files对象 | sysFiles |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/files/delete

- 名称：知识库-文档管理-通过id删除
- Operation ID：`deleteUsingDELETE_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/files/deleteBatch

- 名称：知识库-文档管理-批量删除
- Operation ID：`deleteBatchUsingDELETE_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/files/edit

- 名称：知识库-文档管理-编辑
- Operation ID：`editUsingPOST_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFiles | body | 是 | sys_files对象 | sysFiles |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/files/edit

- 名称：知识库-文档管理-编辑
- Operation ID：`editUsingPUT_5`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysFiles | body | 是 | sys_files对象 | sysFiles |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/files/list

- 名称：知识库-文档管理-分页列表查询
- Operation ID：`queryPageListUsingGET_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| createBy | query | 否 | string | 创建人登录名称 |
| createTime | query | 否 | string(date-time) | 创建日期 |
| delFlag | query | 否 | string | 删除状态(0-正常,1-删除至回收站) |
| downCount | query | 否 | integer(int32) | 下载次数 |
| enableDown | query | 否 | string | 是否允许下载(1：是  0：否) |
| enableUpdat | query | 否 | string | 是否允许修改(1：是  0：否) |
| fileName | query | 否 | string | 文件名称 |
| fileSize | query | 否 | number(double) | 文件大小（kb） |
| fileType | query | 否 | string | 文档类型（folder:文件夹 excel:excel doc:word pp:ppt image:图片  archive:其他文档 video:视频） |
| id | query | 否 | string | 主键id |
| izFolder | query | 否 | string | 是否文件夹(1：是  0：否) |
| izRootFolder | query | 否 | string | 是否为1级文件夹，允许为空 (1：是 ) |
| izStar | query | 否 | string | 是否标星(1：是  0：否) |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| parentId | query | 否 | string | 父级id |
| readCount | query | 否 | integer(int32) | 阅读次数 |
| realname | query | 否 | string | - |
| sharePerms | query | 否 | string | 分享权限(1.关闭分享 2.允许所有联系人查看 3.允许任何人查看) |
| shareUrl | query | 否 | string | 分享链接 |
| storeType | query | 否 | string | 文件上传类型(temp/本地上传(临时文件) manage/知识库) |
| tenantId | query | 否 | string | 租户id |
| updateBy | query | 否 | string | 更新人登录名称 |
| updateTime | query | 否 | string(date-time) | 更新日期 |
| url | query | 否 | string | 文件地址 |
| userData | query | 否 | string | - |
| zipName | query | 否 | string | - |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/files/queryById

- 名称：知识库-文档管理-通过id查询
- Operation ID：`queryByIdUsingGET_5`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 职务表

#### POST /jeecg-system/sys/position/add

- 名称：职务表-添加
- Operation ID：`addUsingPOST_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysPosition | body | 是 | sys_position对象 | sysPosition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/position/delete

- 名称：职务表-通过id删除
- Operation ID：`deleteUsingDELETE_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«object» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/position/deleteBatch

- 名称：职务表-批量删除
- Operation ID：`deleteBatchUsingDELETE_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/position/edit

- 名称：职务表-编辑
- Operation ID：`editUsingPOST_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysPosition | body | 是 | sys_position对象 | sysPosition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/position/edit

- 名称：职务表-编辑
- Operation ID：`editUsingPUT_8`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| sysPosition | body | 是 | sys_position对象 | sysPosition |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/position/list

- 名称：职务表-分页列表查询
- Operation ID：`queryPageListUsingGET_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 否 | string | 职务编码 |
| companyId | query | 否 | string | 公司id |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | id |
| name | query | 否 | string | 职务名称 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| postRank | query | 否 | string | 职级 |
| sysOrgCode | query | 否 | string | 组织机构编码 |
| tenantId | query | 否 | integer(int32) | 租户ID |
| updateBy | query | 否 | string | 修改人 |
| updateTime | query | 否 | string(date-time) | 修改时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«sys_position对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/position/queryByCode

- 名称：职务表-通过code查询
- Operation ID：`queryByCodeUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| code | query | 是 | string | code |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/position/queryById

- 名称：职务表-通过id查询
- Operation ID：`queryByIdUsingGET_8`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«sys_position对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### 重复校验

#### GET /jeecg-system/sys/duplicate/check

- 名称：重复校验接口
- Operation ID：`doDuplicateCheckUsingGET`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| dataId | query | 否 | string | 数据ID |
| fieldName | query | 否 | string | 字段名 |
| fieldVal | query | 否 | string | 字段值 |
| tableName | query | 否 | string | 表名 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

### tms_pda_permission

#### POST /jeecg-system/sys/pdaPermission/add

- 名称：tms_pda_permission-添加
- Operation ID：`addUsingPOST_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaPermission | body | 是 | tms_pda_permission对象 | tmsPdaPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### DELETE /jeecg-system/sys/pdaPermission/delete

- 名称：tms_pda_permission-通过id删除
- Operation ID：`deleteUsingDELETE_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### DELETE /jeecg-system/sys/pdaPermission/deleteBatch

- 名称：tms_pda_permission-批量删除
- Operation ID：`deleteBatchUsingDELETE_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| ids | query | 是 | string | ids |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 204 | - | No Content |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |

#### POST /jeecg-system/sys/pdaPermission/edit

- 名称：tms_pda_permission-编辑
- Operation ID：`editUsingPOST_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaPermission | body | 是 | tms_pda_permission对象 | tmsPdaPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### PUT /jeecg-system/sys/pdaPermission/edit

- 名称：tms_pda_permission-编辑
- Operation ID：`editUsingPUT_10`
- Content-Type：`application/json`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| tmsPdaPermission | body | 是 | tms_pda_permission对象 | tmsPdaPermission |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«string» | OK |
| 201 | - | Created |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/pdaPermission/list

- 名称：tms_pda_permission-分页列表查询
- Operation ID：`queryPageListUsingGET_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| componentName | query | 否 | string | - |
| createBy | query | 否 | string | 创建人 |
| createTime | query | 否 | string(date-time) | 创建时间 |
| id | query | 否 | string | 主键id |
| name | query | 否 | string | 菜单标题 |
| pageNo | query | 否 | integer(int32) | pageNo |
| pageSize | query | 否 | integer(int32) | pageSize |
| sort | query | 否 | integer(int32) | - |
| status | query | 否 | string | 状态 1启用/禁用0 |
| updateBy | query | 否 | string | 更新人 |
| updateTime | query | 否 | string(date-time) | 更新时间 |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«IPage«tms_pda_permission对象»» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

#### GET /jeecg-system/sys/pdaPermission/queryById

- 名称：tms_pda_permission-通过id查询
- Operation ID：`queryByIdUsingGET_10`
- Content-Type：`未声明`
- 返回类型：`*/*`
- Deprecated：否

请求参数：

| 参数 | 位置 | 必填 | 类型/模型 | 说明 |
|---|---|---:|---|---|
| id | query | 是 | string | id |

响应：

| HTTP 状态 | 响应模型 | 说明 |
|---|---|---|
| 200 | 接口返回对象«tms_pda_permission对象» | OK |
| 401 | - | Unauthorized |
| 403 | - | Forbidden |
| 404 | - | Not Found |

## 数据模型

### 登录对象

登录对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| captcha | 否 | string | 验证码 |
| checkKey | 否 | string | 验证码key |
| password | 否 | string | 密码 |
| username | 否 | string | 账号 |

### 接口返回对象

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | object | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«sys_comment对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«sys_comment对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«sys_position对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«sys_position对象» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«SysCommentFileVo»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«SysCommentFileVo» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«SysCommentVO»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«SysCommentVO» | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«IPage«tms_pda_permission对象»»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | IPage«tms_pda_permission对象» | 返回数据对象 |
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

### 接口返回对象«object»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | object | 返回数据对象 |
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

### 接口返回对象«sys_comment对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | sys_comment对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«sys_position对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | sys_position对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### 接口返回对象«tms_pda_permission对象»

接口返回对象

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | integer(int32) | 返回代码 |
| message | 否 | string | 返回处理消息 |
| result | 否 | tms_pda_permission对象 | 返回数据对象 |
| success | 否 | boolean | 成功标志 |
| timestamp | 否 | integer(int64) | 时间戳 |

### IPage«sys_comment对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<sys_comment对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«sys_position对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<sys_position对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«SysCommentFileVo»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<SysCommentFileVo> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«SysCommentVO»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<SysCommentVO> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### IPage«tms_pda_permission对象»

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| current | 否 | integer(int64) |  |
| pages | 否 | integer(int64) |  |
| records | 否 | array<tms_pda_permission对象> |  |
| size | 否 | integer(int64) |  |
| total | 否 | integer(int64) |  |

### sys_check_rule对象

编码校验规则

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | 主键id |
| ruleCode | 否 | string | 规则Code |
| ruleDescription | 否 | string | 规则描述 |
| ruleJson | 否 | string | 规则JSON |
| ruleName | 否 | string | 规则名称 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

### sys_comment对象

系统评论回复表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| commentContent | 否 | string | 回复内容 |
| commentId | 否 | string | 评论id(允许为空，不为空时，则为回复) |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| fromUserId | 否 | string | 来源用户id |
| id | 否 | string | id |
| tableDataId | 否 | string | 数据id |
| tableName | 否 | string | 表名 |
| toUserId | 否 | string | 发送给用户id(允许为空) |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### sys_data_source对象

多数据源管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 数据源编码 |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建日期 |
| dbDriver | 否 | string | 驱动类 |
| dbName | 否 | string | 数据库名称 |
| dbPassword | 否 | string | 密码 |
| dbType | 否 | string | 数据库类型 |
| dbUrl | 否 | string | 数据源地址 |
| dbUsername | 否 | string | 用户名 |
| id | 否 | string | id |
| name | 否 | string | 数据源名称 |
| remark | 否 | string | 备注 |
| sysOrgCode | 否 | string | 所属部门 |
| tenantId | 否 | integer(int32) | 租户ID |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新日期 |

### sys_depart_permission对象

部门权限表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| dataRuleIds | 否 | string | 数据规则id |
| departId | 否 | string | 部门id |
| id | 否 | string | id |
| permissionId | 否 | string | 权限id |

### sys_depart_role对象

部门角色

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| departId | 否 | string | 部门id |
| description | 否 | string | 描述 |
| id | 否 | string | id |
| roleCode | 否 | string | 部门角色编码 |
| roleName | 否 | string | 部门角色名称 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

### sys_files对象

知识库-文档管理

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人登录名称 |
| createTime | 否 | string(date-time) | 创建日期 |
| delFlag | 否 | string | 删除状态(0-正常,1-删除至回收站) |
| downCount | 否 | integer(int32) | 下载次数 |
| enableDown | 否 | string | 是否允许下载(1：是  0：否) |
| enableUpdat | 否 | string | 是否允许修改(1：是  0：否) |
| fileName | 否 | string | 文件名称 |
| fileSize | 否 | number(double) | 文件大小（kb） |
| fileType | 否 | string | 文档类型（folder:文件夹 excel:excel doc:word pp:ppt image:图片  archive:其他文档 video:视频） |
| id | 否 | string | 主键id |
| izFolder | 否 | string | 是否文件夹(1：是  0：否) |
| izRootFolder | 否 | string | 是否为1级文件夹，允许为空 (1：是 ) |
| izStar | 否 | string | 是否标星(1：是  0：否) |
| parentId | 否 | string | 父级id |
| readCount | 否 | integer(int32) | 阅读次数 |
| realname | 否 | string |  |
| sharePerms | 否 | string | 分享权限(1.关闭分享 2.允许所有联系人查看 3.允许任何人查看) |
| shareUrl | 否 | string | 分享链接 |
| storeType | 否 | string | 文件上传类型(temp/本地上传(临时文件) manage/知识库) |
| tenantId | 否 | string | 租户id |
| updateBy | 否 | string | 更新人登录名称 |
| updateTime | 否 | string(date-time) | 更新日期 |
| url | 否 | string | 文件地址 |
| userData | 否 | string |  |
| zipName | 否 | string |  |

### sys_fill_rule对象

填值规则

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | 主键ID |
| ruleClass | 否 | string | 规则实现类 |
| ruleCode | 否 | string | 规则Code |
| ruleName | 否 | string | 规则名称 |
| ruleParams | 否 | string | 规则参数 |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### sys_form_file对象

表单评论文件

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| createBy | 否 | string | 创建人登录名称 |
| createTime | 否 | string(date-time) | 创建日期 |
| fileId | 否 | string | 关联文件id |
| fileType | 否 | string | 文档类型（folder:文件夹 excel:excel doc:word pp:ppt image:图片  archive:其他文档 video:视频） |
| id | 否 | string | id |
| tableDataId | 否 | string | 数据id |
| tableName | 否 | string | 表名 |

### sys_position对象

职务表

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| code | 否 | string | 职务编码 |
| companyId | 否 | string | 公司id |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | id |
| name | 否 | string | 职务名称 |
| postRank | 否 | string | 职级 |
| sysOrgCode | 否 | string | 组织机构编码 |
| tenantId | 否 | integer(int32) | 租户ID |
| updateBy | 否 | string | 修改人 |
| updateTime | 否 | string(date-time) | 修改时间 |

### sys_role_index对象

角色首页配置

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| component | 否 | string | 组件 |
| createBy | 否 | string | 创建人登录名称 |
| createTime | 否 | string(date-time) | 创建日期 |
| id | 否 | string | id |
| priority | 否 | integer(int32) | 优先级 |
| roleCode | 否 | string | 角色编码 |
| route | 否 | boolean | 是否路由菜单 |
| status | 否 | string | 状态 |
| sysOrgCode | 否 | string | 所属部门 |
| updateBy | 否 | string | 更新人登录名称 |
| updateTime | 否 | string(date-time) | 更新日期 |
| url | 否 | string | 路由地址 |

### SysCommentFileVo

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| fileId | 否 | string |  |
| fileSize | 否 | number(double) |  |
| name | 否 | string |  |
| storeType | 否 | string |  |
| sysFormFileId | 否 | string |  |
| type | 否 | string |  |
| url | 否 | string |  |

### SysCommentVO

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| commentContent | 否 | string |  |
| commentId | 否 | string |  |
| createTime | 否 | string(date-time) | 创建日期 |
| fileList | 否 | array<SysCommentFileVo> |  |
| fromUserAvatar | 否 | string |  |
| fromUserId | 否 | string |  |
| fromUserId_dictText | 否 | string |  |
| id | 否 | string |  |
| tableDataId | 否 | string |  |
| tableName | 否 | string |  |
| toUserAvatar | 否 | string |  |
| toUserId | 否 | string |  |
| toUserId_dictText | 否 | string |  |

### tms_pda_permission对象

tms_pda_permission

| 字段 | 必填 | 类型/模型 | 说明 |
|---|---:|---|---|
| componentName | 否 | string |  |
| createBy | 否 | string | 创建人 |
| createTime | 否 | string(date-time) | 创建时间 |
| id | 否 | string | 主键id |
| name | 否 | string | 菜单标题 |
| sort | 否 | integer(int32) |  |
| status | 否 | string | 状态 1启用/禁用0 |
| updateBy | 否 | string | 更新人 |
| updateTime | 否 | string(date-time) | 更新时间 |

