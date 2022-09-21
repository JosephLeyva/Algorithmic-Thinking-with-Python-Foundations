def double(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i] * 2)
    return new_arr


my_arr = [5, 4, 3, 2, 1]
print(double(my_arr))

# Space Complexity => O(n)
