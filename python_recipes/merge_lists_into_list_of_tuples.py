"""
Section:
    list

Author:
    Carlos Aguila

Description:
    How to merge two lists into a list of tuples

Tags:
    list, flatten, merge, tuple
"""
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

list_of_tuples = list(zip(list_a, list_b))
# [(1, 5), (2, 6), (3, 7), (4, 8)]
