
"""
Section:
    map

Author:
    Carlos Aguila (Simon Ward-Jones)

Description:
    How to apply functions to a list using map

Tags:
    map, list, lambda

"""

example_dir_list = ['dictionary_from_two_lists.py',
                    'flask_routing.py',
                    'flask_sqlalchemy_model.py',
                    'flatten_list_of_lists.py']

dashed_names = [*map(lambda x: x.replace('_', '-'),
                     example_dir_list)]
# ['dictionary-from-two-lists.py',
#  'flask-routing.py',
#  'flask-sqlalchemy-model.py',
#  'flatten-list-of-lists.py']

# Using a Lambda
squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))
# [0, 1, 4, 9, 16]