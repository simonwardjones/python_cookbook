"""
Section:
    Pandas

Author:
    Simon Ward-Jones

Description:
    Dataframe aggregations

Tags:
    pandas , aggregate, sum, mean
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

# First we create example dataframe
r = random.Random(12)


def generate_random_date_in_last_year():
    return (datetime.now() - relativedelta(days=365 * random.random())).date()


dataframe = pd.DataFrame({
    "date_time": [generate_random_date_in_last_year() for _ in range(10)],
    "animal": ['zebra', 'zebra', 'zebra', 'zebra', 'lion', 'lion', 'lion',
               'lion', 'rhino', 'rhino', ],
    "category": ['stripy'] * 4 + ['dangerous'] * 6,
    "name": ['Walter', 'Edmund', 'Gyles', 'John', 'Bartholomew', 'Frederyk',
             'Raulf', 'Symond', 'Carlos', 'Arthur'],
    "weight": [80 + 40 * r.random() for _ in range(10)],
    "favourite_integer": [r.randint(0, 100) for _ in range(10)],
    "bad_column": ['', 3, '', 1, None, 2, 23, 2, 3, 3],
    'employed': [bool(r.randint(0, 1)) for i in range(10)]
})
dataframe.replace(to_replace='', value=np.nan, inplace=True)
dataframe

dataframe_stats = dataframe.groupby(['animal', 'employed']).agg({
    'favourite_integer': ['min', 'max', 'mean', 'std', 'sum'],
    'weight': ['sum']})

animal_weight_stats = dataframe_stats['weight'].sort_values('sum',
                                                            ascending=False)

animal_weight_stats

# animal | employed | sum
# zebra  | False    | 311.93814609882565
# lion   | False    | 298.3660273510712
# rhino  | False    | 211.68198767065672
# zebra  | True     | 85.70401411701471
# lion   | True     | 80.43441772360272

# Ineresting that the unemployed animals are heavier!
