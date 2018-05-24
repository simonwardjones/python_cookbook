"""
Section:
    Scopes

Author:
    Simon Ward-Jones

Description:
    nonlocal keyword usage

Tags:
    global, local, scopes, nonlocal
"""

# Example 1) local variables
a = 1


def f():
    def g():
        a = 3
        print(f'a in g: {a}')
    a = 2
    print(f'a in f before g called: {a}')
    g()
    print(f'a in f after g called: {a}')


print(f'a before f called: {a}')
f()
print(f'a after f called: {a}')
print()

# a before f called: 1
# a in f before g called: 2
# a in g: 3
# a in f after g called: 2
# a after f called: 1

# The vairables scopes are all separate and hence not changed


# Example 2) global variables
a = 1


def f():
    def g():
        global a
        a = 3
        print(f'a in g: {a}')
    global a
    a = 2
    print(f'a in f before g called: {a}')
    g()
    print(f'a in f after g called: {a}')


print(f'a before f called: {a}')
f()
print(f'a after f called: {a}')
print()

# a before f called: 1
# a in f before g called: 2
# a in g: 3
# a in f after g called: 3
# a after f called: 3

# The a variable always refers to the global!
# See that all variables were changed by assignment in g


# Example 3) nonlocal variables
a = 1


def f():
    def g():
        nonlocal a
        a = 3
        print(f'a in g: {a}')
    a = 2
    print(f'a in f before g called: {a}')
    g()
    print(f'a in f after g called: {a}')


print(f'a before f called: {a}')
f()
print(f'a after f called: {a}')
print()

# a before f called: 1
# a in f before g called: 2
# a in g: 3
# a in f after g called: 3
# a after f called: 1

# The nonlocal a variable refers to the variable defined in the
# local f function scope (more generally one level above)
# nonloal can not be used to refer to module level variable


# Example 4) A more complex example
a = 1


def f():
    def g():
        def h():
            global a
            a = 4
            print(f'a in h {a}')
        nonlocal a
        a = 3
        print(f'a in g before h: {a}')
        h()
        print(f'a in g after h: {a}')
    a = 2
    print(f'a in f before g called: {a}')
    g()
    print(f'a in f after g called: {a}')


print(f'a before f called: {a}')
f()
print(f'a after f called: {a}')
print()

# a before f called: 1
# a in f before g called: 2
# a in g before h: 3
# a in h 4
# a in g after h: 3
# a in f after g called: 3
# a after f called: 4

# The global variable is altered in h scope and the local variable
# defined in f is altered in the g scope using nonlocal keyword
