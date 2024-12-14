import random

# arr = []
# total = 0
# for i in range(12):
#     a = round(random.random() * 4) - 2 + 3
#     arr.append(a)
#     total += a
# arr.append(total)
# print(arr)

arr = []
total = 0
for i in range(12):
    a = round(random.random() * 2) + 3
    arr.append(a)
    total += a


for i in range(4):
    a = round(random.random() * 5) + 5
    arr.append(a)
    total += a
arr.append(total)
print(arr)
