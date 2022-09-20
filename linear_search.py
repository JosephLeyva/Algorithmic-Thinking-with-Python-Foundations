'''
LINEAR SEARCH
'''

from random import randint


# def linear_search(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return i
#     return -1


def linear_search(data, target):
    for idx, value in enumerate(data):
        if value == target:
            return idx
    return -1


# data = [randint(1, 100) for i in range(10)]
data = [4, 5, 2, 7, 1, 8]
print(data)
target = 5

result = linear_search(data, target)
if result == -1:
    print('item not found.')
else:
    print(f'item found at position {result}.')
