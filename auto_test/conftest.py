"""Global fixtures for the TMS automation foundation.

Business rules must be resolved through ``knowledge/KNOWLEDGE_INDEX.md`` before
future tests are added. This module only manages infrastructure lifecycle.
"""

from __future__ import annotations

import os
import re
from collections.abc import Iterator
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest
import yaml

from auto_test.core.api_client import ApiClient
from auto_test.core.browser_base import BrowserBase
from auto_test.core.captcha_recognizer import CaptchaRecognizer
from auto_test.core.reporter import JsonResultReporter, TestResult, utc_now
from auto_test.core.tms_auth import TmsAuthenticator
from auto_test.pom.tms import TmsLoginPage

AUTO_TEST_ROOT = Path(__file__).resolve().parent
ENV_FILE = AUTO_TEST_ROOT / "config" / "env.yaml"
ENV_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}")


def _expand_env(value: Any) -> Any:
    if isinstance(value, str):
        return ENV_PATTERN.sub(lambda match: os.getenv(match.group(1), match.group(2) or ""), value)
    if isinstance(value, dict):
        return {key: _expand_env(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_expand_env(item) for item in value]
    return value


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("tms-automation")
    group.addoption("--env", action="store", default=None, help="Environment key from config/env.yaml")
    group.addoption(
        "--artifacts-dir",
        action="store",
        default=None,
        help="Override screenshot, video, and result output directory",
    )


def pytest_configure(config: pytest.Config) -> None:
    raw_config = yaml.safe_load(ENV_FILE.read_text(encoding="utf-8")) or {}
    environment = config.getoption("--env") or raw_config.get("active", "local")
    environment_config = raw_config.get("environments", {}).get(environment)
    if environment_config is None:
        raise pytest.UsageError(f"Unknown environment '{environment}' in {ENV_FILE}")

    merged = _deep_merge(raw_config.get("defaults", {}), environment_config)
    merged = _expand_env(merged)
    if not config.getoption("--browser"):
        config.option.browser = [merged["browser"]["type"]]
    configured_artifacts = config.getoption("--artifacts-dir") or merged["artifacts"]["directory"]
    artifact_root = Path(configured_artifacts)
    if not artifact_root.is_absolute():
        artifact_root = AUTO_TEST_ROOT / artifact_root
    run_dir = artifact_root / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    run_dir.mkdir(parents=True, exist_ok=True)

    config._tms_environment = environment
    config._tms_settings = merged
    config._tms_artifact_dir = run_dir
    config._tms_reporter = JsonResultReporter(run_dir / "results", environment)
    config.addinivalue_line("markers", "knowledge(*paths): knowledge documents supporting a test")
    config.addinivalue_line("markers", "scenario(name): business scenario description")


@pytest.fixture(scope="session")
def environment_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig._tms_environment


@pytest.fixture(scope="session")
def settings(pytestconfig: pytest.Config) -> dict[str, Any]:
    return pytestconfig._tms_settings


@pytest.fixture(scope="session")
def artifact_dir(pytestconfig: pytest.Config) -> Path:
    return pytestconfig._tms_artifact_dir


@pytest.fixture(scope="session")
def api_client(settings: dict[str, Any]) -> Iterator[ApiClient]:
    api_config = settings["api"]
    static_token = api_config.get("token") or ""
    client = ApiClient(
        api_config["base_url"],
        timeout=(
            float(api_config["connect_timeout"]),
            float(api_config["read_timeout"]),
        ),
        verify_ssl=bool(api_config["verify_ssl"]),
        token_provider=lambda: static_token,
    )
    yield client
    client.close()


@pytest.fixture(scope="session")
def browser_type_launch_args(
    pytestconfig: pytest.Config,
    settings: dict[str, Any],
) -> dict[str, Any]:
    browser_config = settings["browser"]
    return {
        "headless": False if pytestconfig.getoption("--headed") else bool(browser_config["headless"]),
        "slow_mo": int(browser_config["slow_mo"]),
    }


@pytest.fixture(scope="session")
def browser_context_args(
    settings: dict[str, Any],
    artifact_dir: Path,
) -> dict[str, Any]:
    browser_config = settings["browser"]
    video_dir = artifact_dir / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)
    return {
        "viewport": browser_config["viewport"],
        "ignore_https_errors": bool(browser_config["ignore_https_errors"]),
        "record_video_dir": str(video_dir),
    }


@pytest.fixture
def browser_base(page, settings: dict[str, Any], artifact_dir: Path) -> BrowserBase:
    return BrowserBase(
        page=page,
        artifact_dir=artifact_dir,
        base_url=settings.get("ui", {}).get("base_url", ""),
    )


@pytest.fixture(scope="session")
def captcha_recognizer() -> CaptchaRecognizer:
    return CaptchaRecognizer()


@pytest.fixture
def tms_login_page(browser_base: BrowserBase) -> TmsLoginPage:
    return TmsLoginPage(browser_base)


@pytest.fixture
def tms_authenticated_page(
    page,
    settings: dict[str, Any],
    tms_login_page: TmsLoginPage,
    captcha_recognizer: CaptchaRecognizer,
):
    """Return the fixture-managed Page after OCR-assisted TMS login."""
    ui_config = settings.get("ui", {})
    auth_config = ui_config.get("auth", {})
    authenticator = TmsAuthenticator(
        tms_login_page,
        captcha_recognizer,
        max_attempts=int(auth_config.get("captcha_max_attempts", 3)),
        login_timeout_ms=int(auth_config.get("login_timeout_ms", 15_000)),
    )
    authenticator.login(
        username=str(ui_config.get("username", "")),
        password=str(ui_config.get("password", "")),
    )
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    if report.when not in {"setup", "call"}:
        return
    if report.when == "setup" and not report.failed:
        return

    reporter: JsonResultReporter = item.config._tms_reporter
    status = "error" if report.when == "setup" else "passed"
    if report.failed and report.when == "call":
        status = "failed"
    elif report.skipped:
        status = "skipped"

    artifacts: dict[str, str] = {}
    if report.failed:
        page = item.funcargs.get("page")
        if page is not None and not page.is_closed():
            screenshot_dir = item.config._tms_artifact_dir / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{item.nodeid.replace('/', '_').replace(':', '_')}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            artifacts["screenshot"] = str(screenshot_path)

    knowledge_marker = item.get_closest_marker("knowledge")
    scenario_marker = item.get_closest_marker("scenario")
    reporter.add(
        TestResult(
            nodeid=item.nodeid,
            name=item.name,
            status=status,
            duration_seconds=round(report.duration, 6),
            started_at=utc_now(),
            finished_at=utc_now(),
            business_scenario=str(scenario_marker.args[0]) if scenario_marker and scenario_marker.args else "",
            knowledge_paths=[str(path) for path in knowledge_marker.args] if knowledge_marker else [],
            error=str(report.longrepr) if report.failed else "",
            traceback=str(report.longrepr) if report.failed else "",
            artifacts=artifacts,
        )
    )


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    reporter = getattr(session.config, "_tms_reporter", None)
    if reporter is not None:
        reporter.finalize(exitstatus)
