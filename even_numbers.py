'''
EXERCISE: Find all the even numbers up to 100
'''

# BRUTE FORCE APPROACH
for i in range(1, 101):  # from 1 to a 100
    if i % 2 == 0:  # if number is divisible by 2
        print(i)

# STEP APPROACH
for i in range(2, 101, 2):
    print(i)
