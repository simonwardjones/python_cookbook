"""
Section:
    set

Author:
    Carlos Aguila

Description:
    How to use basic set operations

Tags:
    set, list
"""

list_1 = [2, 3, 4, 5]
list_2 = [3, 4, 5, 6]
set_1 = set(list_1)
set_2 = set(list_2)

# Set operations:
set_1_without_set_2 = set_1 - set_2
set_1_union_set_2 = set_1 | set_2
set_1_intersect_set_2 = set_1 & set_2
symmetric_difference = set_1 ^ set_2  # In set 1 or set 2 but not both

print(set_1_without_set_2)
# {2}
print(set_1_union_set_2)
# {2, 3, 4, 5, 6}
print(set_1_intersect_set_2)
# {3, 4, 5}
print(symmetric_difference)
# {2, 6}
