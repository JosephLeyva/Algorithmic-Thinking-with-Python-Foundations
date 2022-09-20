# Starting with door 1 to 100 on the index (ignore index 0)
doors = [False] * 101


for j in range(1, 101):
    for i in range(j, len(doors), j):
        doors[i] = not doors[i]
# print(doors)

count = 0
index = 0
for door in doors:
    if door:
        print(index, end=',')
        count += 1
    index += 1

print(f'\b \n{count=}')
