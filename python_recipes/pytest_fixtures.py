"""
Section:
    test

Author:
    Simon Ward-Jones

Description:
    pytest fixture functionality

Tags:
    test , pytest, fixtures
"""
import pytest

##################
# General
##################

# As this file has the word 'test' in the name it will be picked up by
# the pytest command line command.


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


# tip:
# when running the test use -vvs to be more verbose and include stdout

# tip3:
# pytest --version   # shows where pytest was imported from
# pytest --fixtures  # show available builtin function arguments
# pytest -h | --help # show help on command line and config file options

##################
# Fixtures
##################

# Test functions can receive fixture objects by naming them
# as an input argument

# Fixtures are implemented in a modular manner
# as each fixture name triggers a fixture function
# which can itself use other fixtures.

class A:
    attribute = 121

    def inner(self):
        return 2

# we make a fixtue create an instance (normally a bit more)


@pytest.fixture
def A_instance():
    return A()

# simply including the name of the fixture is enough to run the fixture
# and include the result


def test_inner(A_instance):
    assert A_instance.inner() == 2


# collected 2 items

# pytest_fixtures.py::test_answer PASSED
# pytest_fixtures.py::test_inner PASSED
