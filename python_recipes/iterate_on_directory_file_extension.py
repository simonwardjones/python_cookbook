""" 
Section:
    os

Author:
    Simon Ward-Jones

Description:
    How to iterate on a directory filtering by 
    file extension

Tags:
    file extension, directory, os
"""
import os
import glob

## Method 1
# use the endswith method on a string
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(file)


## Method 2
# Use the glob library
for file in glob.glob("*.py"):
    print(file)


