def my_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


my_array = [5, 4, 3, 2, 1]
print(my_sum(my_array))

# Space Complexity => O(1)
