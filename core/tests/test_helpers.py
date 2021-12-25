import datetime

import core.helpers as helpers


def test_is_recent():
    now = datetime.datetime.now(datetime.timezone.utc)
    assert helpers.is_recent(now)

    future = now + datetime.timedelta(seconds=2)
    assert not helpers.is_recent(future)
