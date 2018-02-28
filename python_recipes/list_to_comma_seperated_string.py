"""
Section:
    list

Author:
    Simon Ward-Jones

Description:
    Convert a list to a comma seperated string

Tags:
    list, comma, string
"""
example_list = ['The', 'Zebra', 'has', 5, 'stripes']
comma_sep_string = ','.join(map(str, example_list))
quote_comma_sep_string = ','.join(f"'{w}'" for w in example_list)

print(comma_sep_string)
# 'The,Zebra,has,5,stripes'

print(quote_comma_sep_string)
# 'The','Zebra','has','5','stripes'
# This can be useful for SQL
