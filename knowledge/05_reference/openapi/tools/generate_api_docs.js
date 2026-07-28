#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const openapiDir = path.resolve(__dirname, "..");
const rawDir = path.join(openapiDir, "raw");
const generatedDir = path.join(openapiDir, "generated");
const services = [
  ["jeecg-tms", "TMS 核心后台"],
  ["jeecg-tms-api", "TMS 对外及终端"],
  ["jeecg-camera", "摄像头/明眸"],
  ["jeecg-radar", "雷达/RFID/报警灯"],
  ["jeecg-system", "系统管理与权限"],
];
const httpMethods = new Set(["get", "post", "put", "delete", "patch"]);

function escapeCell(value) {
  return String(value ?? "-").replace(/\|/g, "\\|").replace(/\r?\n/g, "<br>");
}

function schemaName(schema) {
  if (!schema) return "-";
  if (schema.$ref) return schema.$ref.split("/").pop();
  if (schema.type === "array") return `array<${schemaName(schema.items)}>`;
  if (schema.type) return schema.format ? `${schema.type}(${schema.format})` : schema.type;
  return "object";
}

function operationRows(spec) {
  const rows = [];
  for (const [route, pathItem] of Object.entries(spec.paths || {})) {
    for (const [method, operation] of Object.entries(pathItem)) {
      if (!httpMethods.has(method)) continue;
      rows.push({
        method: method.toUpperCase(),
        route,
        fullPath: `${spec.basePath || ""}${route}`,
        operation,
        parameters: [...(pathItem.parameters || []), ...(operation.parameters || [])],
      });
    }
  }
  return rows;
}

function renderParameters(parameters) {
  if (!parameters.length) return "_无显式请求参数。_\n";
  const lines = [
    "| 参数 | 位置 | 必填 | 类型/模型 | 说明 |",
    "|---|---|---:|---|---|",
  ];
  for (const parameter of parameters) {
    lines.push(
      `| ${escapeCell(parameter.name)} | ${escapeCell(parameter.in)} | ${
        parameter.required ? "是" : "否"
      } | ${escapeCell(schemaName(parameter.schema || parameter))} | ${escapeCell(
        parameter.description
      )} |`
    );
  }
  return `${lines.join("\n")}\n`;
}

function renderResponses(responses) {
  const entries = Object.entries(responses || {});
  if (!entries.length) return "_Swagger 未声明响应。_\n";
  const lines = ["| HTTP 状态 | 响应模型 | 说明 |", "|---|---|---|"];
  for (const [status, response] of entries) {
    lines.push(
      `| ${escapeCell(status)} | ${escapeCell(schemaName(response.schema))} | ${escapeCell(
        response.description
      )} |`
    );
  }
  return `${lines.join("\n")}\n`;
}

function renderDefinitions(definitions) {
  const lines = ["## 数据模型", ""];
  const entries = Object.entries(definitions || {}).sort(([a], [b]) => a.localeCompare(b, "zh-CN"));
  if (!entries.length) return `${lines.join("\n")}_无数据模型。_\n`;
  for (const [name, definition] of entries) {
    lines.push(`### ${name}`, "");
    if (definition.description) lines.push(definition.description, "");
    const properties = Object.entries(definition.properties || {});
    if (!properties.length) {
      lines.push("_无字段定义。_", "");
      continue;
    }
    const required = new Set(definition.required || []);
    lines.push("| 字段 | 必填 | 类型/模型 | 说明 |", "|---|---:|---|---|");
    for (const [field, property] of properties) {
      const enumText = property.enum ? `；枚举：${property.enum.join(", ")}` : "";
      lines.push(
        `| ${escapeCell(field)} | ${required.has(field) ? "是" : "否"} | ${escapeCell(
          schemaName(property)
        )} | ${escapeCell(`${property.description || ""}${enumText}`)} |`
      );
    }
    lines.push("");
  }
  return `${lines.join("\n")}\n`;
}

function renderService(service, displayName, spec) {
  const rows = operationRows(spec);
  const byTag = new Map();
  for (const row of rows) {
    for (const tag of row.operation.tags || ["未分类"]) {
      if (!byTag.has(tag)) byTag.set(tag, []);
      byTag.get(tag).push(row);
    }
  }

  const lines = [
    `# ${displayName}接口明细`,
    "",
    `> 来源：\`../raw/${service}.swagger.json\`。本文由生成器自动生成，请勿手工修改生成区内容。`,
    "",
    "## 服务信息",
    "",
    `- 服务标识：\`${service}\``,
    `- 网关地址：\`http://${spec.host || "111.160.91.170:59999"}\``,
    `- Base Path：\`${spec.basePath || "/"}\``,
    `- 鉴权头：\`${Object.values(spec.securityDefinitions || {})[0]?.name || "文档未声明"}\``,
    `- 路径数：${Object.keys(spec.paths || {}).length}`,
    `- 接口操作数：${rows.length}`,
    `- 数据模型数：${Object.keys(spec.definitions || {}).length}`,
    "",
    "## 控制器索引",
    "",
    "| 控制器/标签 | 接口数 |",
    "|---|---:|",
  ];
  for (const [tag, taggedRows] of [...byTag.entries()].sort(([a], [b]) =>
    a.localeCompare(b, "zh-CN")
  )) {
    lines.push(`| ${escapeCell(tag)} | ${taggedRows.length} |`);
  }

  lines.push("", "## 接口清单", "");
  for (const [tag, taggedRows] of [...byTag.entries()].sort(([a], [b]) =>
    a.localeCompare(b, "zh-CN")
  )) {
    lines.push(`### ${tag}`, "");
    for (const row of taggedRows.sort((a, b) => a.fullPath.localeCompare(b.fullPath))) {
      const operation = row.operation;
      lines.push(
        `#### ${row.method} ${row.fullPath}`,
        "",
        `- 名称：${operation.summary || "Swagger 未提供"}`,
        `- Operation ID：\`${operation.operationId || "-"}\``,
        `- Content-Type：\`${(operation.consumes || spec.consumes || ["未声明"]).join(", ")}\``,
        `- 返回类型：\`${(operation.produces || spec.produces || ["未声明"]).join(", ")}\``,
        `- Deprecated：${operation.deprecated ? "是" : "否"}`,
        "",
        "请求参数：",
        "",
        renderParameters(row.parameters),
        "响应：",
        "",
        renderResponses(operation.responses)
      );
    }
  }
  lines.push(renderDefinitions(spec.definitions));
  return lines.join("\n");
}

fs.mkdirSync(generatedDir, { recursive: true });
const loaded = services.map(([service, displayName]) => {
  const spec = JSON.parse(fs.readFileSync(path.join(rawDir, `${service}.swagger.json`), "utf8"));
  fs.writeFileSync(
    path.join(generatedDir, `${service}.md`),
    renderService(service, displayName, spec),
    "utf8"
  );
  return { service, displayName, spec, operations: operationRows(spec) };
});

const overview = [
  "# TMS 接口知识库总览",
  "",
  "> 接口事实以 `raw/*.swagger.json` 为准；`generated/*.md` 为可检索明细。采集日期：2026-07-28。",
  "",
  "## 接口规模",
  "",
  "| 服务 | 业务定位 | Base Path | 路径数 | 操作数 | 模型数 | 明细 |",
  "|---|---|---|---:|---:|---:|---|",
];
for (const item of loaded) {
  overview.push(
    `| ${item.service} | ${item.displayName} | \`${item.spec.basePath}\` | ${
      Object.keys(item.spec.paths || {}).length
    } | ${item.operations.length} | ${Object.keys(item.spec.definitions || {}).length} | [查看](generated/${
      item.service
    }.md) |`
  );
}
overview.push(
  "",
  `合计：${loaded.reduce((sum, item) => sum + Object.keys(item.spec.paths || {}).length, 0)} 条路径，${loaded.reduce(
    (sum, item) => sum + item.operations.length,
    0
  )} 个接口操作，${loaded.reduce(
    (sum, item) => sum + Object.keys(item.spec.definitions || {}).length,
    0
  )} 个数据模型。`,
  "",
  "## 查询路由",
  "",
  "| 查询目标 | 优先文档 |",
  "|---|---|",
  "| 后台基础数据、任务池、规则、配置、报表 | `generated/jeecg-tms.md` |",
  "| PAD/PDA、MES/WMS/WCS、AGV回调、提升机 | `generated/jeecg-tms-api.md` |",
  "| 明眸/摄像头通知 | `generated/jeecg-camera.md` |",
  "| 雷达、RFID、报警灯 | `generated/jeecg-radar.md` |",
  "| 登录、权限、数据字典、系统基础能力 | `generated/jeecg-system.md` |",
  "",
  "## 使用边界",
  "",
  "1. Swagger 描述反映接口声明，不等同于完整业务规则；业务断言仍应联合状态机、流程和约束规则。",
  "2. 所有服务均声明 `X-Access-Token` 请求头，但公开回调是否免鉴权需以环境配置和实测为准。",
  "3. 文档未统一声明服务协议，示例网关使用当前文档站点的 HTTP 地址。",
  "4. `Test-Controller`、测试 Modbus、模拟通知和系统开关接口具有环境风险，自动化默认不得在生产环境执行。",
  "5. Swagger 的通用 `200` 响应不代表业务成功，测试需继续断言响应体中的成功标识、业务码和数据状态。"
);
fs.writeFileSync(path.join(openapiDir, "API_OVERVIEW.md"), `${overview.join("\n")}\n`, "utf8");
