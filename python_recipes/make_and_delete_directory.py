"""
Section:
    os

Author:
    Simon Ward-Jones

Description:
    How to make and delete direcotries

Tags:
    os, direcotry, shutil
"""
import os
import shutil

# # Make a directory
directory = os.path.join(os.curdir, "temporary_zebra")
if not os.path.exists(directory):
    os.makedirs(directory)

# Delete the directory
if os.path.exists(directory):
    shutil.rmtree(directory)


# Both of the above could be acheived with raw system commands:
if not os.path.exists(directory):
    os.system(f'mkdir {directory}')

# # Delete the directory
if os.path.exists(directory):
    os.system(f'rm -rf {directory}')
