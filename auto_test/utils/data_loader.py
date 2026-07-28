"""Versioned YAML test-data loading for TMS automation.

Data-generation and usage rules follow
``knowledge/06_auto_test_spec/api_code_spec.md`` and
``knowledge/06_auto_test_spec/ui_code_spec.md``.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

SCENARIO_TYPES = frozenset({"normal", "abnormal", "boundary"})


class TestDataError(RuntimeError):
    """Base exception for invalid or unavailable test data."""


class TestDataNotFoundError(TestDataError):
    """Raised when a requested module, scenario, or case does not exist."""


class TestDataFormatError(TestDataError):
    """Raised when a YAML data set does not follow the required structure."""


class TestDataLoader:
    """Load isolated, module-based TMS YAML data sets."""

    def __init__(self, data_root: Path) -> None:
        self.data_root = Path(data_root).resolve()
        if not self.data_root.is_dir():
            raise TestDataNotFoundError(
                f"Test data directory does not exist: {self.data_root}"
            )
        self._cache: dict[str, dict[str, Any]] = {}

    def load_module(self, module_name: str) -> dict[str, Any]:
        """Return a deep copy of one validated module data set."""
        if module_name not in self._cache:
            module_path = self._resolve_module_path(module_name)
            if not module_path.is_file():
                raise TestDataNotFoundError(
                    f"Test data module does not exist: {module_name}"
                )
            raw_data = yaml.safe_load(module_path.read_text(encoding="utf-8"))
            self._cache[module_name] = self._validate_module(
                module_name,
                raw_data,
            )
        return deepcopy(self._cache[module_name])

    def load_scenario(
        self,
        module_name: str,
        scenario_type: str,
    ) -> dict[str, Any]:
        """Return all cases under normal, abnormal, or boundary."""
        if scenario_type not in SCENARIO_TYPES:
            raise TestDataFormatError(
                f"Unsupported scenario type '{scenario_type}'; "
                f"expected one of {sorted(SCENARIO_TYPES)}"
            )
        module_data = self.load_module(module_name)
        return deepcopy(module_data[scenario_type])

    def load_case(
        self,
        module_name: str,
        scenario_type: str,
        case_name: str,
    ) -> dict[str, Any]:
        """Return one named case as an isolated dictionary."""
        scenario_data = self.load_scenario(module_name, scenario_type)
        case_data = scenario_data.get(case_name)
        if case_data is None:
            raise TestDataNotFoundError(
                f"Test data case does not exist: "
                f"{module_name}.{scenario_type}.{case_name}"
            )
        if not isinstance(case_data, dict):
            raise TestDataFormatError(
                f"Test data case must be a mapping: "
                f"{module_name}.{scenario_type}.{case_name}"
            )
        return deepcopy(case_data)

    def _resolve_module_path(self, module_name: str) -> Path:
        if not module_name or Path(module_name).name != module_name:
            raise TestDataFormatError(
                f"Invalid test data module name: {module_name!r}"
            )
        module_path = (self.data_root / f"{module_name}.yaml").resolve()
        if module_path.parent != self.data_root:
            raise TestDataFormatError(
                f"Test data module escapes configured root: {module_name!r}"
            )
        return module_path

    @staticmethod
    def _validate_module(
        module_name: str,
        raw_data: Any,
    ) -> dict[str, Any]:
        if not isinstance(raw_data, dict):
            raise TestDataFormatError(
                f"Test data module must be a mapping: {module_name}"
            )
        missing_types = SCENARIO_TYPES.difference(raw_data)
        if missing_types:
            raise TestDataFormatError(
                f"Test data module '{module_name}' is missing scenario types: "
                f"{sorted(missing_types)}"
            )
        for scenario_type in SCENARIO_TYPES:
            if not isinstance(raw_data[scenario_type], dict):
                raise TestDataFormatError(
                    f"Scenario '{module_name}.{scenario_type}' "
                    "must be a mapping"
                )
        return raw_data
