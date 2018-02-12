"""
Section:
    os

Author:
    Simon Ward-Jones

Description:
    How to run a subprocess

Tags:
    os, subprocess
"""
import os
import subprocess
from subprocess import run, check_output

string_to_do = ["sleep 1; echo 'A wild Zebra!!'"]

# As of python 3.5 it is best to use the run command
# The are many options - see docs for full details
out = run(string_to_do,
          check=False,  # Do not error if subprocess returns non-zero
          stdout=subprocess.PIPE,  # Pipe value to stdout
          shell=True)  # Complete as shubshell command

print(str(out.stdout, 'utf-8'))
