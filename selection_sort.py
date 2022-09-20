'''
EXERCISE: Implement the SELECTION SORT

* Find the smallest element in the array and exchange it with the element in the first position
* Find the second smallest element in the array and exchange it with the element in the second position
* Continue this process until the array is sorted
'''

from random import randint


def swap(a, b):
    return b, a


def find_min_value(data):
    min_index = 0
    for i, value in enumerate(data):
        if value < data[min_index]:
            min_index = i
    return data[min_index], min_index


def selection_sort(data):
    # We iterate over all the array
    for i in range(len(data)-1):
        # We find the smallest element in the array. We need to repeat this
        # for the remaining items
        _, idx = find_min_value(data[i:])
        idx += i
        # We exchange the minimum with the correct position
        data[i], data[idx] = swap(data[i], data[idx])


data = [randint(1, 20) for i in range(20)]
# data = [3, 2, 1, 5, 4]
print(data)

selection_sort(data)
print(data)

print(all(data[i] <= data[i+1] for i in range(len(data) - 1)))
