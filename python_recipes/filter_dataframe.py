"""
Section:
    Pandas

Author:
    Simon Ward-Jones

Description:
    Dataframe filtering by values

Tags:
    pandas , filter, values
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

# We can filter the dataframe by specific values in a specific column
filter_list = ['lion','rhino']
dataframe[dataframe['animal'].isin(filter_list)]

# Alternatively we could use a map on the series
dataframe[dataframe['animal'].map(lambda x: x in filter_list)]

# or even this
dataframe.query('animal in '+ str(filter_list))
