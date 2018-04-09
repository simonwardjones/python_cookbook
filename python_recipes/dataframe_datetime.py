"""
Section:
    Pandas

Author:
    Simon Ward-Jones

Description:
    Dataframe datetime

Tags:
    pandas , datetime, timestamp
"""
import pandas as pd
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

# First we create example dataframe
r = random.Random(12)


def generate_random_date_in_last_year():
    return (datetime.now() - relativedelta(days=365 * random.random()))


dataframe = pd.DataFrame({
    "date_time": [generate_random_date_in_last_year() for _ in range(10)]})
dataframe['month'] = dataframe.date_time.dt.month
dataframe['day'] = dataframe.date_time.dt.day
dataframe['hour'] = dataframe.date_time.dt.hour
dataframe['minute'] = dataframe.date_time.dt.minute
dataframe['day_of_week'] = dataframe.date_time.dt.dayofweek

dataframe
#   | date_time                  | month | day | hour | minute | day_of_week
# 0 | 2017-06-01 16:52:55.692476 | 6     | 1   | 16   | 52     | 3
# 1 | 2017-06-15 04:19:29.499383 | 6     | 15  | 4    | 19     | 3
# 2 | 2017-08-31 14:48:38.406128 | 8     | 31  | 14   | 48     | 3
# 3 | 2017-06-06 23:46:50.090056 | 6     | 6   | 23   | 46     | 1
# 4 | 2018-03-01 04:08:46.937911 | 3     | 1   | 4    | 8      | 3
# 5 | 2017-03-14 11:36:48.532703 | 3     | 14  | 11   | 36     | 1
# 6 | 2017-10-19 22:47:44.591292 | 10    | 19  | 22   | 47     | 3
# 7 | 2017-06-23 03:39:29.668738 | 6     | 23  | 3    | 39     | 4
# 8 | 2017-09-15 05:33:02.847853 | 9     | 15  | 5    | 33     | 4
# 9 | 2017-06-19 01:41:20.161772 | 6     | 19  | 1    | 41     | 0
