"""
Section:
    Pandas

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    Chunk a Pandas DataFrame

Tags:
    pandas , split, chunk
"""
import pandas as pd

dataframe = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], columns=['TEST'])
df_split = np.array_split(dataframe, 3)
# Gives a list with the chunked DF
print(df_split)
