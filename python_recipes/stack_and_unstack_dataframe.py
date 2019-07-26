"""
Section:
    Pandas

Author:
    Simon Ward-Jones

Description:
    Dataframe stacking and unstacking

Tags:
    pandas , stack, unstack
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
    "Zoo": ['London Zoo', 'New York Zoo',
            'London Zoo', 'New York Zoo',
            'London Zoo', 'New York Zoo'],
    "animal": ['zebra', 'zebra',
               'lion', 'lion',
               'rhino', 'rhino'],
    "category": ['stripy'] * 2 + ['dangerous'] * 2 + ['heavy'] * 2,
    "count": [5, 1, 9, 6, 7, 9]})

# create a multiindex of animal and name
dataframe = dataframe.set_index(['Zoo', 'animal'])


# We can use unstack to unstack rows into columns
# going from deep to wide

dataframe['count'].unstack(level=0)
# same as dataframe['count'].unstack(level='Zoo')

# animal | London Zoo | New York Zoo
# lion   | 9          | 6
# rhino  | 7          | 9
# zebra  | 5          | 1


dataframe['count'].unstack(level=1)
# same as dataframe['count'].unstack(level='animal')
# same as dataframe['count'].unstack(level=-1)
# here -1 indicates last level

# Zoo        | lion | rhino | zebra
# London Zoo   | 9    | 7     | 5
# New York Zoo | 6    | 9     | 1

# stack does the opposite converting columns to rows
# going from wide to deep