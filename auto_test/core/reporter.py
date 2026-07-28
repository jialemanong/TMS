"""Structured pytest result output for future knowledge feedback ingestion."""

from __future__ import annotations

import json
import threading
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class TestResult:
    nodeid: str
    name: str
    status: str
    duration_seconds: float
    started_at: str
    finished_at: str
    business_scenario: str = ""
    knowledge_paths: list[str] = field(default_factory=list)
    error: str = ""
    traceback: str = ""
    artifacts: dict[str, str] = field(default_factory=dict)


class JsonResultReporter:
    """Thread-safe run reporter with stable JSON and JSONL outputs."""

    schema_version = "1.0"

    def __init__(self, output_dir: Path, environment: str) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.environment = environment
        self.run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        self.started_at = utc_now()
        self.results: list[TestResult] = []
        self._lock = threading.Lock()

    @property
    def jsonl_path(self) -> Path:
        return self.output_dir / f"results-{self.run_id}.jsonl"

    @property
    def summary_path(self) -> Path:
        return self.output_dir / f"summary-{self.run_id}.json"

    def add(self, result: TestResult) -> None:
        payload = asdict(result)
        with self._lock:
            self.results.append(result)
            with self.jsonl_path.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def finalize(self, exit_status: int) -> Path:
        counts = {"passed": 0, "failed": 0, "skipped": 0, "error": 0}
        for result in self.results:
            counts[result.status] = counts.get(result.status, 0) + 1
        payload = {
            "schema_version": self.schema_version,
            "run_id": self.run_id,
            "environment": self.environment,
            "started_at": self.started_at,
            "finished_at": utc_now(),
            "exit_status": exit_status,
            "counts": counts,
            "results": [asdict(result) for result in self.results],
            "feedback_target": "knowledge/test_feedback/",
        }
        self.summary_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return self.summary_path
