'''
BINARY SEARCH
Python implementation of Binary Search algorithm'
REQUISITES
-----------
The dataset must be sorted before!
'''


from random import randint


def binary_search(data, target):
    low_pointer = 0
    high_pointer = len(data) - 1
    while low_pointer <= high_pointer:
        mid_point = (low_pointer + high_pointer) // 2
        if data[mid_point] == target:
            return mid_point
        elif data[mid_point] < target:
            low_pointer = mid_point + 1
        else:
            high_pointer - mid_point - 1

    return -1


n = 10
max_val = 100

data = [randint(1, max_val) for i in range(n)]
data.sort()  # Sorting the data before calling Binary Search algorithm
print("Data: ", data)
target = int(input("Enter target value: "))
# Remember that positioning starts at 0!
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list")
else:
    print(f"Your target {target} is found at position [{target_pos}]")
