from datetime import datetime
from zoneinfo import ZoneInfo


def now_jst() -> datetime:
    """現在のJST時刻を返す"""
    return datetime.now(ZoneInfo(key="Asia/Tokyo"))
