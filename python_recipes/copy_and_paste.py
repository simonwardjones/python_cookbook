"""
Section:
    helpers

Author:
    Simon Ward-Jones (Carlos Aguila)

Description:
    Copy and paste

Tags:
    copy , paste
"""
import clipboard
import pyperclip

# Method 1
clipboard.copy('A wild zebra')
clipboard.paste()

# Method 2
pyperclip.copy('A wild zebra')
pyperclip.paste()
