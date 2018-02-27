"""
Section:
    Pandas

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    Pivot table from Dataframe

Tags:
    pivot , pandas, pivot table
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

# Pivot table
pivot_dataframe = pd.pivot_table(dataframe,
                                 values=['weight', 'bad_column'],
                                 index='animal',
                                 columns='employed',
                                 aggfunc=[np.mean])
pivot_dataframe

#          | mean       | mean       | mean               | mean
#          | bad_column | bad_column | weight             | weight
# employed | False      | True       | False              | True
# animal   |            |            |                    |
# lion     | 9.0        |            | 99.45534245035707  | 80.43441772360272
# rhino    | 3.0        |            | 105.84099383532836 |
# zebra    | 3.0        | 1.0        | 103.97938203294188 | 85.70401411701471
