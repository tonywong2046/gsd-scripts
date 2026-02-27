"""
Cloud Run Functions 入口 — HTTP handlers
entryPoint 对应关系：
  fetch-jobs      → fetch_jobs_handler
  fetch-journals  → fetch_journals_handler
  fetch-reports   → fetch_reports_handler
"""
import functions_framework

from fetch_jobs    import main as _run_jobs
from fetch_journals import main as _run_journals
from fetch_reports  import main as _run_reports


@functions_framework.http
def fetch_jobs_handler(request):
    _run_jobs()
    return "OK", 200


@functions_framework.http
def fetch_journals_handler(request):
    _run_journals()
    return "OK", 200


@functions_framework.http
def fetch_reports_handler(request):
    _run_reports()
    return "OK", 200
