"""
Section:
    objects

Author:
    Simon Ward-Jones

Description:
    Attribute access

Tags:
    descriptor protocol, __get__, __set__, __delete__
"""

# A descriptor has the __get__ magic function defined
# A data descriptor has the __get__ and at
# least one of __set__ or __delete__

class mood():
    """ descriptor"""
    def __get__(self, instance, owner):
        print(f'__get__ called with self, instance, owner ='
              f'{self, instance, owner}')
        return 'Happy'
    def __repr__(self):
        return f'<mood>'


class Age():
    """ data descriptor"""
    def __init__(self):
        print(f'initialise age property (note no value yet)')

    def __get__(self, instance, owner):
        print(f'__get__ called with self, instance, owner = '
              f'{self, instance, owner}')
        return instance._age

    def __set__(self, instance, value):
        instance._age = value

    def __repr__(self):
        return f'<Age>'


class Human():
    lung_count = 2
    age = Age()
    mood = mood()
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'<Human name={self.name}>'
    def __getattr__(self, attr):
        print('Fails looking for {attr} on {self}')
        return 'FAIL'


# Descriptors are useful because they allow logic on get/set/delete
# Soooo how does attribute look up work?

###################
# For an object
###################

# Say we are looking up attribute called attribute on a class
# instance called instance  with class called Class

# The look up goes through the below:

# 1- Class.__dict__ has data descriptor called attribute
# return Class.__dict__['attribute'].__get__(instance,Class)

# 2- attribute in instance.__dict__
# return instance.__dict__['attribute']

# 3- attribute in Class.__dict__ (but has __get__ not __set__ or __delete__)
# return Class.__dict__['attribute'].__get__(instance,Class)

# 4- attribute in Class.__dict__ (but has NO __get__ )
# return Class.__dict__['attribute']

# 5- finnaly call Class.__getattr__


# To see this look at the examples
# note type(fred) == Human

fred = Human(name='Fred', age=32)
assert type(fred) == Human
# initialise age property (note no value yet)


print('Scenraio 1')
print(fred.age)
# __get__ called with self, instance, owner =
# (<Age>, <Human name=Fred>, <class '__main__.Human'>)
# 32

# Explained
# Note fred is an object and age is a data descriptor so we end up in
# scenraio 1
assert fred.age == type(fred).__dict__['age'].__get__(fred, Human)


# print(fred.name)
print('Scenraio 2')
print(fred.name)
# Fred

# Explained
# Note fred is an object and name is not a descriptor so we end up in
# scenraio 2
assert fred.name == fred.__dict__['name']


print('Scenraio 3')
print(fred.mood)
# __get__ called with self, instance, owner =
# (<mood>, <Human name=Fred>, <class '__main__.Human'>)
# Happy

# Explained
# Note fred is an object and mood is a descriptor so we end up in
# scenraio 3
assert fred.mood == type(fred).__dict__['mood'].__get__(fred, Human)


print('Scenraio 4')
print(fred.lung_count)
# 2

# Explained
# Note fred is an object and lung_count is not a descriptor so we end up in
# scenraio 4
assert fred.lung_count == type(fred).__dict__['lung_count']

print('Scenraio 5')
print(fred.height)
# Fails looking for {attr} on {self}
# FAIL

# Explained
# Note fred is an object and height is not in fred.__dict__ or Human.__dict__
# which leaves us in scenraio 5

