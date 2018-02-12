"""
Section:
    list

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    How to flatten a list of lists

Tags:
    list, flatten
"""
import itertools

# Method 1
# For a list of lists simply use a list comprehension

example_string_list = ['an', 'example', 'list', 'of', 'strings']
example_int_list = [123, 34, 3, 12, 32, 14]
example_nested_list = [example_string_list, example_int_list]

flattened = [item for sublist in example_nested_list for item in sublist]
# ['an', 'example', 'list', 'of', 'strings', 123, 34, 3, 12, 32, 14]


# Method 2
# Again for same example but using built in method from itertools

flattened = list(itertools.chain.from_iterable(example_nested_list))
# ['an', 'example', 'list', 'of', 'strings', 123, 34, 3, 12, 32, 14]


# Method 3
# For a more complex example nested to an arbitrary depth we need a
# recursive function

def flatten(nested_lists):
    flattened_list = []
    for element in nested_lists:
        if isinstance(element, list):
            for sub_element in flatten(element):
                flattened_list.append(sub_element)
        else:
            flattened_list.append(element)
    return flattened_list


example_deeply_nested_list = [
    1, 2, 4, [1, 2, 3, 5, 67, [1, 2, 3, 4, [1, 2, 3, 4]]]]
flattened = flatten(example_deeply_nested_list)

# [1, 2, 4, 1, 2, 3, 5, 67, 1, 2, 3, 4, 1, 2, 3, 4]
