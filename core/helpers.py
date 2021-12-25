from datetime import datetime, timedelta, timezone


def is_recent(obj: datetime) -> True:
    """Return True if datetime is recent (not older than a second)"""
    return obj - datetime.now(timezone.utc) <= timedelta(seconds=1)
