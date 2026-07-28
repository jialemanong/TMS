# 数据库物理外键清单

> 本文只记录DDL明确声明的物理外键，不包含根据字段名称推测的软关联。

| 本表 | 约束 | 本表字段 | 目标表 | 目标字段 |
|---|---|---|---|---|
| qrtz_blob_triggers | qrtz_blob_triggers_ibfk_1 | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` | qrtz_triggers | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` |
| qrtz_cron_triggers | qrtz_cron_triggers_ibfk_1 | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` | qrtz_triggers | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` |
| qrtz_simple_triggers | qrtz_simple_triggers_ibfk_1 | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` | qrtz_triggers | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` |
| qrtz_simprop_triggers | qrtz_simprop_triggers_ibfk_1 | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` | qrtz_triggers | `SCHED_NAME`, `TRIGGER_NAME`, `TRIGGER_GROUP` |
| qrtz_triggers | qrtz_triggers_ibfk_1 | `SCHED_NAME`, `JOB_NAME`, `JOB_GROUP` | qrtz_job_details | `SCHED_NAME`, `JOB_NAME`, `JOB_GROUP` |
