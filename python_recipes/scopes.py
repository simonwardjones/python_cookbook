"""
Section:
    Scopes

Author:
    Simon Ward-Jones

Description:
    Demonstrating Scopes

Tags:
    global, local, scopes
"""

a = 1


def f():
    """
    Uses global because there is no local 'a'
    """
    print('Inside f() : ', a)


def g():
    """
    Variable 'a' is redefined as a local
    """
    a = 2
    print('Inside g() : ', a)


def h():
    """
    Uses global keyword to modify global 'a'
    """
    global a
    a = 3
    print('Inside h() : ', a)

# If we did not incluse the 'global' keyword
# we would receive this error:
# "UnboundLocalError: local variable 'a' referenced before assignment"


print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

# global :  1
# Inside f() :  1
# global :  1
# Inside g() :  2
# global :  1
# Inside h() :  3
# global :  3
