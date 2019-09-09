"""
Section:
    list

Author:
    Simon Ward-Jones

Description:
    How to find the absolute min value in list

Tags:
    list, min, abs
"""
numbers = [-23, 534, -134, 36, -294]

# method one using comprehension (note this works as by default min
# uses first element of each tuple then returns that tuple, we then
# select the posibly negative second value of the tuple)
abs_min = min((abs(value), value) for value in numbers)[1]
print(abs_min)  # -23

# method two using the reduce function
abs_min = reduce(lambda a, b: a if abs(a) < abs(b) else b, numbers)
print(abs_min)  # -23

# method three using the key option of min
abs_min = min(numbers, key=abs)
print(abs_min)  # -23
