"""
Section:
    list

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    Reduce a list of values using a function

Tags:
    reduce, functools
"""
from functools import reduce

list_values = [1, 2, 4, 4, 2, 3, 7]


def add(a, b):
    """
    Re-implementing the add function ...
    """
    return a + b


list_sum = reduce(add, list_values)
print(list_sum)
# 23

# Example with lambda
list_product = reduce(lambda a, b: a * b, list_values)
print(list_product)
# 1344
