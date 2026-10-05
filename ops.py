"""Operational tasks."""
import re
import subprocess
import requests

from app.config import REPORT_BUCKET


# PLANT C7
def archive_report(report_name):
    if not re.match(r'^[a-zA-Z0-9_\-./\\]+$', report_name):
        raise ValueError("Invalid report_name")
    if not re.match(r'^[a-zA-Z0-9_\-./\\]+$', REPORT_BUCKET):
        raise ValueError("Invalid REPORT_BUCKET")
    cmd = "aws s3 cp /tmp/" + report_name + " s3://" + REPORT_BUCKET + "/archive/"
    return subprocess.run(cmd, shell=True, capture_output=True)


def fetch_fx_rates(base="USD"):
    return requests.get(f"https://api.example-fx.test/latest?base={base}", timeout=10).json()
