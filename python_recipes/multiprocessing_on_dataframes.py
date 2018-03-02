"""
Section:
    Processing

Author:
    Carlos Aguilar (Simon Ward-Jones)

Description:
    Demonstration of the multiprocessing library on Dataframes.

Tags:
    pandas, , boto3
"""

import pandas as pd
import numpy as np
import multiprocessing as mp
from functools import partial

# Mutiprocessing with DATAFRAMES


def parallelSum(df, b, c, d):
    a = df.TEST.sum()
    dfA = pd.DataFrame(data=[{'results': a}])
    print('A -> {},B -> {},C -> {},D -> {}'.format(a, b, c, d))
    return dfA


df = pd.DataFrame(np.random.random_sample((50000, 1)), columns=['TEST'])
df_split = np.array_split(df, 100)

cores = mp.cpu_count()
maxCores = cores - 1
pool = mp.Pool(maxCores)

# use partial to fix the arguments that don't change
worker_a = partial(parallelSum, b='b', c='c', d='d')
results = pool.map(worker_a, df_split)
pool.close()
pool.join()
# The results are a list of dataframes
extResults = pd.DataFrame()
for thisDF in results:
    extResults = extResults.append(thisDF, ignore_index=True)
