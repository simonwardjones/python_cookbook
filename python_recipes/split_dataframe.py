"""
Section:
    Pandas

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    Chunk a Pandas DataFrame

Tags:
    pandas , numpy, split, chunk
"""
import pandas as pd
import numpy as np

dataframe = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], columns=['TEST'])
df_split = np.array_split(dataframe, 3)
# Gives a list with the chunked DF
for df in df_split:
    print(df)

#    TEST
# 0     1
# 1     2
# 2     3
# 3     4
#    TEST
# 4     5
# 5     6
# 6     7
# 7     8
#     TEST
# 8      9
# 9     10
# 10    11
