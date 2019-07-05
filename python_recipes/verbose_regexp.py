"""
Section:
    regexp

Author:
    Simon Ward-Jones

Description:
    How to remove comments from sql using vebose regexp

Tags:
    regexp, comments
"""

import re

sql_comment_pattern = re.compile(r"""
    ('[^'\\]*(?:\\+.[^'\\]*)*')  #  capture single quote strings
    |
    ("[^"\\]*(?:\\+.[^"\\]*)*")  #  capture double quote strings
    |
    (?:\s*(?:(?:(?:--)|(?:\/\/)).*))  #  -- comments (non capture group)
    |
    (?:\/\*[\s\S]*?\*\/)  #  multline /* */ comments (non capture group)
    """, re.X)

example_query = """
select
    T.column as "column_example",
    '-- sql comment' as "simon's column" -- sql comment to remove
from example_table T
/*
    Multiline comment to remove
*/
where 1=1
and T.date < '2001-01-01'::date
"""

print(example_query)
print('\nPrinting without comments:')
print(sql_comment_pattern.sub(r'\1\2', example_query))


# we can also use a function as the replace string. The function takes a
# single match object argument, and returns the replacement string

def remove_comments(matchobj):
    for group_id in [1, 2]:
        if matchobj.group(group_id):
            return matchobj.group(group_id)
    else:
        return ''


print(sql_comment_pattern.sub(remove_comments, example_query))
