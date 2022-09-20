'''
EXERCISE: Implement the SELECTION SORT - Course solution

* Find the smallest element in the array and exchange it with the element in the first position
* Find the second smallest element in the array and exchange it with the element in the second position
* Continue this process until the array is sorted
'''


def selection_sort(data):
    # The last value will automatically be in the correct position
    for i in range(len(data) - 1):
        # Find minimum value in the unsorted region
        min_index = i
        for j in range(i + 1, len(data)):
            # Update min_index if the value at j is lower than current minimum value
            if data[j] < data[min_index]:
                min_index = j
        # After finding the minimum value in the unsorted region, swap with the first unsorted value
        data[i], data[min_index] = data[min_index], data[i]


data = [3, 2, 1, 5, 4]
print(data)
selection_sort(data)
print(data)

# A nice Pythonic way to check a list is sorted
# without relying on using  Python's own sorting methods to compare.
print(all(data[i] <= data[i+1] for i in range(len(data) - 1)))
