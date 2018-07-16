"""
Section:
    numpy

Author:
    Simon Ward-Jones

Description:
    How to find maximum values and their indexes

Tags:
    numpy, max, argmax,argsort, maximum, array
"""

import numpy as np


# For an array
vector = np.array([1, 4, 9, 2, 7])

max_index = vector.argmax()

print(f'Max index of {vector} is {max_index}')
# 2 as expected


# For a 2d array
matrix = np.array([
    [1, 4, 9, 2, 7],
    [1, 2, 34, 12, 4],
    [2, 3, 2, 2, 2]]
)

# specify axis = None for overall maximum
max_flat_index = matrix.argmax(axis=None)
# 7  # This is the index in the flattened array

print(f'Max index of matrix\n {matrix}\nis {max_flat_index},'
      f' note it is assuming flattened')


# for the n-dim index we convert the flattened index

max_indexes = np.unravel_index(max_flat_index, matrix.shape)

print(f'The maximum value of "matrix" ({matrix[max_indexes]}) is '
      f'given by matrix[max_indexes]\nwhere max_indexes is '
      f'np.unravel_index(max_flat_index, matrix.shape)',
      f'= {max_indexes}')


# top n per row using argsort

# axis 0 is rows and axis 1 is columns
# we want to sort along coluns i.e. 1
sorted_indices = np.argsort(matrix, axis=1)

print(f'Indicies to sort rows np.argsort(matrix, axis=1):\n {sorted_indices}')

top_3_per_row_indexes = sorted_indices[:, -3:]

print(f'Top three indicies per row sorted_indices[:, -3:]: \n '
      f'{top_3_per_row_indexes}')


# This next bit is complex and can be explained by braodcasting
# the row and colum index arrays are broadcast to be the same shape!
# (3,3). We want the rows to be broadcast across ie.e have
# shape (3,1)
top_3_per_row = matrix[np.arange(matrix.shape[0])[:, None],
                       top_3_per_row_indexes][:,::-1]

print(f'Top 3 per row:\n {top_3_per_row}')
