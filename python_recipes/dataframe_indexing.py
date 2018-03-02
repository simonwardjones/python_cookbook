"""
Section:
    Pandas

Author:
    Simon Ward-Jones

Description:
    Dataframe indexing

Tags:
    pandas , index, lookup
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

# First we create example dataframe
r = random.Random(12)


def generate_random_date_in_last_year():
    return (datetime.now() - relativedelta(days=365 * random.random()))


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

# How to get the value in row zero in the 'name' column

idx = 0

# All the below give the same result

# Using .loc to select row and column
dataframe.loc[idx, 'name']
# 'Walter'

# Select the row then name
# Use .iloc to select a row series and then select name entry
dataframe.iloc[idx]['name']
# 'Walter'

# Select the column series and then select the idx entry
dataframe['name'][idx]
# 'Walter'

# Same but with dot notation
dataframe.name[idx]
# 'Walter'
