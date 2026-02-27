"""
main.py — GCP Cloud Run Functions 入口
三个抓取任务各对应一个 HTTP 触发器，由 Cloud Scheduler 按时调用。

触发路径（路由由 Cloud Run Functions 2nd gen 决定，通过 function-name 区分）：
  - fetch_jobs_handler     → Cloud Scheduler 每天 06:00 SGT
  - fetch_journals_handler → Cloud Scheduler 每天 07:00 SGT
  - fetch_reports_handler  → Cloud Scheduler 每天 08:00 SGT

运行时身份：claude-mcp@gpha-470410.iam.gserviceaccount.com
（不需要传 GOOGLE_SERVICE_ACCOUNT 环境变量，使用 Application Default Credentials）
"""

import functions_framework
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@functions_framework.http
def fetch_jobs_handler(request):
    """HTTP 触发器：抓取学术职位列表 → Google Sheets「工作」标签"""
    logger.info("Starting fetch_jobs...")
    try:
        from fetch_jobs import main
        main()
        return ("fetch_jobs completed successfully", 200)
    except Exception as e:
        logger.exception("fetch_jobs failed")
        return (f"fetch_jobs failed: {e}", 500)


@functions_framework.http
def fetch_journals_handler(request):
    """HTTP 触发器：抓取学术期刊论文 → Google Sheets「论文」标签"""
    logger.info("Starting fetch_journals...")
    try:
        from fetch_journals import main
        main()
        return ("fetch_journals completed successfully", 200)
    except Exception as e:
        logger.exception("fetch_journals failed")
        return (f"fetch_journals failed: {e}", 500)


@functions_framework.http
def fetch_reports_handler(request):
    """HTTP 触发器：抓取智库报告 → Google Sheets「报告」标签"""
    logger.info("Starting fetch_reports...")
    try:
        from fetch_reports import main
        main()
        return ("fetch_reports completed successfully", 200)
    except Exception as e:
        logger.exception("fetch_reports failed")
        return (f"fetch_reports failed: {e}", 500)
