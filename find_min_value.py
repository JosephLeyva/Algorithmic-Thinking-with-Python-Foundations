'''
FIND MINIMUM VALUE: Implementation of Find the minimum value on an array
'''

from random import randint


def find_min_value(data):
    min_index = 0
    for idx, value in enumerate(data):
        if value < data[min_index]:
            min_index = idx
    return data[min_index]


data = [randint(1, 100) for i in range(10)]
print(data)

minimum = find_min_value(data)

print(minimum)
