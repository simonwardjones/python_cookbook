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


#<table border="1" class="dataframe">\n  <thead>\n    <tr>\n      <th></th>\n      <th colspan="6" halign="left">sum</th>\n      <th colspan="6" halign="left">mean</th>\n    </tr>\n    <tr>\n      <th></th>\n      <th colspan="2" halign="left">bad_column</th>\n      <th colspan="2" halign="left">favourite_integer</th>\n      <th colspan="2" halign="left">weight</th>\n      <th colspan="2" halign="left">bad_column</th>\n      <th colspan="2" halign="left">favourite_integer</th>\n      <th colspan="2" halign="left">weight</th>\n    </tr>\n    <tr>\n      <th>employed</th>\n      <th>False</th>\n      <th>True</th>\n      <th>False</th>\n      <th>True</th>\n      <th>False</th>\n      <th>True</th>\n      <th>False</th>\n      <th>True</th>\n      <th>False</th>\n      <th>True</th>\n      <th>False</th>\n      <th>True</th>\n    </tr>\n    <tr>\n      <th>animal</th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n      <th></th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>lion</th>\n      <td>0.0</td>\n      <td>27.0</td>\n      <td>18.0</td>\n      <td>123.0</td>\n      <td>80.434418</td>\n      <td>298.366027</td>\n      <td>NaN</td>\n      <td>9.0</td>\n      <td>18.000000</td>\n      <td>41.0</td>\n      <td>80.434418</td>\n      <td>99.455342</td>\n    </tr>\n    <tr>\n      <th>rhino</th>\n      <td>NaN</td>\n      <td>6.0</td>\n      <td>NaN</td>\n      <td>69.0</td>\n      <td>NaN</td>\n      <td>211.681988</td>\n      <td>NaN</td>\n      <td>3.0</td>\n      <td>NaN</td>\n      <td>34.5</td>\n      <td>NaN</td>\n      <td>105.840994</td>\n    </tr>\n    <tr>\n      <th>zebra</th>\n      <td>4.0</td>\n      <td>0.0</td>\n      <td>163.0</td>\n      <td>71.0</td>\n      <td>298.659333</td>\n      <td>98.982827</td>\n      <td>2.0</td>\n      <td>NaN</td>\n      <td>54.333333</td>\n      <td>71.0</td>\n      <td>99.553111</td>\n      <td>98.982827</td>\n    </tr>\n  </tbody>\n</table>
