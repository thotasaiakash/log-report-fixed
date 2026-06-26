import json
from pathlib import Path

REPORT = Path("/app/report.json")

EXPECTED_TOTAL = 5
EXPECTED_UNIQUE_IPS = 4
EXPECTED_TOP_PATH = "/index.html"


def test_report_exists():
    """Criterion 1: the agent must write a file at /app/report.json."""
    assert REPORT.exists(), "no file found at /app/report.json"


def test_report_is_valid_json():
    """Criterion 2: /app/report.json must contain valid JSON."""
    try:
        json.loads(REPORT.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError(f"/app/report.json is not valid JSON: {exc}")


def test_total_requests():
    """Criterion 3: report must contain the correct total request count."""
    data = json.loads(REPORT.read_text())
    assert "total_requests" in data, "key 'total_requests' missing from report"
    assert data["total_requests"] == EXPECTED_TOTAL, (
        f"expected total_requests={EXPECTED_TOTAL}, got {data['total_requests']}"
    )


def test_unique_ips():
    """Criterion 4: report must contain the correct count of unique client IPs."""
    data = json.loads(REPORT.read_text())
    assert "unique_ips" in data, "key 'unique_ips' missing from report"
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {data['unique_ips']}"
    )


def test_top_path():
    """Criterion 5: report must name the single most-requested URL path."""
    data = json.loads(REPORT.read_text())
    assert "top_path" in data, "key 'top_path' missing from report"
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {data['top_path']!r}"
    )
