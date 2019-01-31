"""
Section:
    datetime

Author:
    Simon Ward-Jones

Description:
    How to convert datetimes to timestamps and back again

Tags:
    datetime, pytz, timestamp
"""
import datetime
import pytz

# datetime to timestamp
now_utc = datetime.datetime.now(tz=pytz.utc)
now_est = datetime.datetime.now(tz=pytz.timezone('EST'))

now_utc_timestamp = now_utc.timestamp()
now_est_timestamp = now_est.timestamp()

print(now_utc_timestamp)
print(now_est_timestamp)

# timestamp to datetime
timestamp_example = datetime.datetime.fromtimestamp(1532174055.633)
print(timestamp_example)

# Note you need to add the timezone
# e.g.
not_now_est_copy = datetime.datetime.fromtimestamp(
  now_est.timestamp())
now_est_copy = datetime.datetime.fromtimestamp(
  now_est.timestamp(), tz=now_est.tzinfo)
