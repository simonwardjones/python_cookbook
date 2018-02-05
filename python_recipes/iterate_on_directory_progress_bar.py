""" 
Section:
    progress bar

Author:
    Carlos Aguila (Simon Ward-Jones)

Description:
    How to iterate on a directory with a progress bar

Tags:
    tqdm, directory, progress bar
"""
import tqdm as tqdm
# tqdm is a progress bar library
import os
import time

for file in tqdm.tqdm(os.listdir('.')):
    # here you might actually want to do more than sleep
    time.sleep(0.5)        