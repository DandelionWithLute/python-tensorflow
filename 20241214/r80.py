import random

file = open("r80", "a+")

arr = []
for i in range(12):
    arr.append(5)


print(arr)
# for i in range(10):
#     ra = round(random.random() * 10) -5
#     print(ra)

for num in arr:
    ra = round(random.random() * 10) - 5
    arr[num] = num + ra
    print(ra)

print(arr)
