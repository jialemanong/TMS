#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const databaseDir = path.resolve(__dirname, "..");
const sourceFile = path.join(databaseDir, "raw", "tms_v2.sql");
const generatedDir = path.join(databaseDir, "generated");
const sql = fs.readFileSync(sourceFile, "utf8");

function escapeCell(value) {
  return String(value ?? "-").replace(/\|/g, "\\|").replace(/\r?\n/g, "<br>");
}

function parseTables(source) {
  const tables = [];
  const tablePattern =
    /CREATE TABLE `([^`]+)` \(([\s\S]*?)\)\s+ENGINE=([^;]+);/g;
  let match;
  while ((match = tablePattern.exec(source))) {
    const [, name, body, engineTail] = match;
    const columns = [];
    const indexes = [];
    const foreignKeys = [];
    for (const rawLine of body.split(/\r?\n/)) {
      const line = rawLine.trim().replace(/,$/, "");
      const columnMatch = line.match(
        /^`([^`]+)`\s+(.+?)(?:\s+COMMENT\s+'((?:[^']|'')*)')?$/
      );
      if (columnMatch) {
        const definition = columnMatch[2];
        const typeMatch = definition.match(/^([a-zA-Z]+(?:\([^)]*\))?)/);
        const defaultMatch = definition.match(/\sDEFAULT\s+((?:'[^']*')|NULL|[^\s]+)/i);
        columns.push({
          name: columnMatch[1],
          type: typeMatch ? typeMatch[1] : definition.split(/\s+/)[0],
          nullable: !/\sNOT NULL(?:\s|$)/i.test(definition),
          defaultValue: defaultMatch ? defaultMatch[1] : "-",
          autoIncrement: /\sAUTO_INCREMENT(?:\s|$)/i.test(definition),
          comment: (columnMatch[3] || "").replace(/''/g, "'"),
        });
        continue;
      }
      const primaryMatch = line.match(/^PRIMARY KEY \(([^)]+)\)/i);
      const indexMatch = line.match(/^(?:UNIQUE )?KEY `([^`]+)` \((.+)\)/i);
      const foreignMatch = line.match(
        /CONSTRAINT `([^`]+)` FOREIGN KEY \(([^)]+)\) REFERENCES `([^`]+)` \(([^)]+)\)/i
      );
      if (primaryMatch) indexes.push({ name: "PRIMARY", columns: primaryMatch[1], unique: true });
      if (indexMatch)
        indexes.push({
          name: indexMatch[1],
          columns: indexMatch[2],
          unique: /^UNIQUE KEY/i.test(line),
        });
      if (foreignMatch)
        foreignKeys.push({
          name: foreignMatch[1],
          columns: foreignMatch[2],
          targetTable: foreignMatch[3],
          targetColumns: foreignMatch[4],
        });
    }
    const commentMatch = engineTail.match(/COMMENT='([^']*)'/);
    tables.push({
      name,
      comment: commentMatch ? commentMatch[1] : "",
      engine: engineTail.split(/\s+/)[0],
      columns,
      indexes,
      foreignKeys,
    });
  }
  return tables;
}

function category(tableName) {
  if (tableName.startsWith("tms_")) return "TMS业务";
  if (tableName.startsWith("sys_")) return "Jeecg系统";
  if (tableName.startsWith("qrtz_")) return "Quartz调度";
  if (tableName.startsWith("jimu_") || tableName.startsWith("rep_")) return "报表";
  if (tableName.startsWith("onl_")) return "在线表单";
  if (
    tableName.startsWith("demo") ||
    tableName.startsWith("jeecg_") ||
    tableName === "ceshi_note" ||
    tableName === "joa_demo"
  )
    return "示例";
  return "其他";
}

function renderTable(table) {
  const lines = [
    `## ${table.name}`,
    "",
    `- 表说明：${table.comment || "SQL未提供"}`,
    `- 存储引擎：${table.engine}`,
    `- 字段数：${table.columns.length}`,
    "",
    "| 字段 | 类型 | 可空 | 默认值 | 自增 | 说明 |",
    "|---|---|---:|---|---:|---|",
  ];
  for (const column of table.columns) {
    lines.push(
      `| ${escapeCell(column.name)} | ${escapeCell(column.type)} | ${
        column.nullable ? "是" : "否"
      } | ${escapeCell(column.defaultValue)} | ${column.autoIncrement ? "是" : "否"} | ${escapeCell(
        column.comment
      )} |`
    );
  }
  lines.push("", "索引：", "");
  if (table.indexes.length) {
    lines.push("| 索引 | 唯一 | 字段 |", "|---|---:|---|");
    for (const index of table.indexes)
      lines.push(
        `| ${escapeCell(index.name)} | ${index.unique ? "是" : "否"} | ${escapeCell(
          index.columns
        )} |`
      );
  } else {
    lines.push("_SQL未声明索引。_");
  }
  lines.push("");
  if (table.foreignKeys.length) {
    lines.push("物理外键：", "", "| 约束 | 本表字段 | 目标表 | 目标字段 |", "|---|---|---|---|");
    for (const foreignKey of table.foreignKeys)
      lines.push(
        `| ${escapeCell(foreignKey.name)} | ${escapeCell(
          foreignKey.columns
        )} | ${escapeCell(foreignKey.targetTable)} | ${escapeCell(
          foreignKey.targetColumns
        )} |`
      );
    lines.push("");
  }
  return lines.join("\n");
}

const tables = parseTables(sql);
const tmsTables = tables.filter((table) => category(table.name) === "TMS业务");
fs.mkdirSync(generatedDir, { recursive: true });

const indexLines = [
  "# TMS V2 数据库全表索引",
  "",
  "> 来源：`../raw/tms_v2.sql`，采集日期：2026-07-28。表说明和字段说明均来自DDL注释。",
  "",
  "## 分类统计",
  "",
  "| 分类 | 表数 |",
  "|---|---:|",
];
const counts = new Map();
for (const table of tables) counts.set(category(table.name), (counts.get(category(table.name)) || 0) + 1);
for (const [name, count] of counts) indexLines.push(`| ${name} | ${count} |`);
indexLines.push("", `合计：${tables.length} 张表。`, "", "## 全表清单", "");
for (const group of [...counts.keys()]) {
  indexLines.push(`### ${group}`, "", "| 表名 | 表说明 | 字段数 | 索引数 |", "|---|---|---:|---:|");
  for (const table of tables.filter((item) => category(item.name) === group))
    indexLines.push(
      `| ${table.name} | ${escapeCell(table.comment)} | ${table.columns.length} | ${table.indexes.length} |`
    );
  indexLines.push("");
}
fs.writeFileSync(path.join(generatedDir, "ALL_TABLE_INDEX.md"), `${indexLines.join("\n")}\n`);

const dictionary = [
  "# TMS 业务表字段字典",
  "",
  "> 本文由 `tools/generate_database_docs.js` 根据 `raw/tms_v2.sql` 自动生成，请勿手工修改。",
  "",
  `共 ${tmsTables.length} 张 TMS 业务表。数据库仅对少量框架表声明物理外键；TMS业务表字段关联通常由应用层维护。`,
  "",
  ...tmsTables.map(renderTable),
];
fs.writeFileSync(
  path.join(generatedDir, "TMS_TABLE_DICTIONARY.md"),
  `${dictionary.join("\n\n")}\n`
);

const foreignKeyLines = [
  "# 数据库物理外键清单",
  "",
  "> 本文只记录DDL明确声明的物理外键，不包含根据字段名称推测的软关联。",
  "",
  "| 本表 | 约束 | 本表字段 | 目标表 | 目标字段 |",
  "|---|---|---|---|---|",
];
for (const table of tables) {
  for (const foreignKey of table.foreignKeys)
    foreignKeyLines.push(
      `| ${table.name} | ${foreignKey.name} | ${escapeCell(
        foreignKey.columns
      )} | ${foreignKey.targetTable} | ${escapeCell(foreignKey.targetColumns)} |`
    );
}
fs.writeFileSync(
  path.join(generatedDir, "PHYSICAL_FOREIGN_KEYS.md"),
  `${foreignKeyLines.join("\n")}\n`
);

console.log(
  JSON.stringify({
    tables: tables.length,
    tmsTables: tmsTables.length,
    columns: tables.reduce((sum, table) => sum + table.columns.length, 0),
    tmsColumns: tmsTables.reduce((sum, table) => sum + table.columns.length, 0),
    foreignKeys: tables.reduce((sum, table) => sum + table.foreignKeys.length, 0),
  })
);

