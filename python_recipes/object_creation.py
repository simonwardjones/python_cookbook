"""
Section:
    objects

Author:
    Simon Ward-Jones

Description:
    instance and Class creation

Tags:
    instance, creation, class, __new__, __init__, __prepare__
"""
class A:
    pass

a = A()

print(f'a.__class__ = {a.__class__}')
print(f'A.__class__ = {A.__class__}')
# a.__class__ = <class '__main__.A'>
# A.__class__ = <class 'type'>

# What just happened? No really what happened?
# We created a class then an instanc but how did that happen

#####################
# Instance creation
#####################
print('Instance creation')

# 1 - The MetaClass.__call__ function is called which does two things**
#     1.1 - Calls Class.__new__ returning an object
#     1.2 - Calls Class.__init__ returning initialised object
# The instance is the returned

## We can override these magic functions to see this.
# Note the default MetaClass is type

# First we create a metaclass and override __call__
class MetaExample(type):
  def __call__(cls, *args, **kwargs):
         print(f'MetaExample __call__\n'
               f'\tcls = {cls}\n\targs = {args}\n\tkwargs = {kwargs}')
         return super().__call__(*args, **kwargs)

# Now we create the Class and override __new__ and __init__
class Example(metaclass=MetaExample):
    def __init__(self,*args, **kwargs):
        print('Example.__init__\n',
              f'\tself = {self}\n\targs = {args}\n\tkwargs = {kwargs}')
        super().__init__()
    def __new__(self, *args, **kwargs):
        print('Example.__new__\n'
              f'\tself = {self}\n\targs = {args}\n\tkwargs = {kwargs}')
        return super().__new__(self)


example_instance = Example(1, a='string')

# MetaExample __call__
#   cls = <class '__main__.Example'>
#   args = (1,)
#   kwargs = {'a': 'string'}
# Example.__new__
#   self = <class '__main__.Example'>
#   args = (1,)
#   kwargs = {'a': 'string'}
# Example.__init__
#   self = <__main__.Example object at 0x1104ce710>
#   args = (1,)
#   kwargs = {'a': 'string'}



#####################
# Class creation
#####################
print('\nClass creation')

# 1 - the MetaClass __prepare__ fumnction is called providing a namespace dict
# 2 - The MetaMetaClass.__call__ function is called which does two things
#     2.1 - Calls MetaClass.__new__ returning a Class object
#     2.2 - Calls MetaClass.__init__ returning initialised Class

class MetaMetaClass(type):
    def __call__(mcls, *args, **kwargs):
        print(f'MetaMetaClass __call__\n'
              f'\tmcls = {mcls}\n\targs = {args}\n\tkwargs = {kwargs}')
        cls = mcls.__new__(mcls, *args, **kwargs)
        mcls.__init__(cls, *args, **kwargs)
        return cls
        # this mimics the standard
        # return super().__call__(*args, **kwargs)


class MetaClass(type, metaclass=MetaMetaClass):
    def __new__(cls, name, bases, namespace, *args, **kwargs):
        print('MetaClass.__new__\n'
              f'\tcls = {cls}\n'
              f'\tname = {name}\n\tbases = {bases}\n\tnamespace = {namespace}')
        return super().__new__(cls, name, bases, namespace)

    def __init__(self, *args, **kwargs):
        print(f'MetaClass.__init__\n\tself = {self}')


class Example(metaclass=MetaClass):
    pass

# Class creation
# MetaMetaClass __call__
#   mcls = <class '__main__.MetaClass'>
#   args = ('Example', (), {'__module__': '__main__', '__qualname__': 'Example'})
#   kwargs = {}
# MetaClass.__new__
#   cls = <class '__main__.MetaClass'>
#   name = Example
#   bases = ()
#   namespace = {'__module__': '__main__', '__qualname__': 'Example'}
# MetaClass.__init__
#   self = <class '__main__.Example'>

# Note the class object now exists
# Also see __new__ and __init__ are static

print(Example)

# Just to blow you mind the statement:
# class Example(metaclass=MetaClass):
#     pass
# could be replaced with
# Example = MetaMetaclass.__call__(MetaClass,'Example', (), {})

# Note
# type('Example',(),{})
# is type.__call__(type,'Example',(),{})
