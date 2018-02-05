"""
Section:
    dictionary

Author:
    Carlos Aguila

Description:
    How to merge two lists into a dictionary

Tags:
    list, dictionary
"""

words = ['zebra','bear','dog']
counts = [12, 43, 54]
count_look_up_dict = dict(zip(words,counts))

count_look_up_dict['zebra']
# {'bear': 43, 'dog': 54, 'zebra': 12}