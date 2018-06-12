"""
Section:
    objects

Author:
    Simon Ward-Jones

Description:
    Creating a property on a class

Tags:
    property, __get__, __set__, __delete__
"""

# A property allows logic to be built
# into accessing/setting/deleting values

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print(f"Getting value {self._temperature}")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print(f"Setting value {value}")
        self._temperature = value

    def delete_temperature(self):
        print(f'deleted {self._temperature}')
        self._temperature = 0

    temperature = property(get_temperature,
                           set_temperature,
                           delete_temperature,
                           doc="Temperature property")

# Create an instance of the celcius class
# this also creates an instance of property class
room_temp = Celsius()

# Set the temperature calls 'set_temperature'
room_temp.temperature = 5

# Delete temperature calls 'delete_temperature'
del room_temp.temperature
room_temp.temperature = 23

# This calls get_temperature
print(room_temp.temperature)


# For more understanding on how properties work
# please read up on descriptor protocol
# and attribute lookup

# output:
# Setting value 0
# Setting value 5
# deleted 5
# Setting value 23
# Getting value 23
# 23
