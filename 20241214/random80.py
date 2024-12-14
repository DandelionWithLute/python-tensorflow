import random


def handleAnswer():
    arr = []
    for i in range(12):
        a = random.random()
        newNum = round(10 * a / 2)
        arr.append(newNum)
    print(arr)
    total = 0
    for inde in arr:
        total += inde
    print(total)
    if abs(total - 60) > 10:
        handleAnswer()
    else:
        file = open("random80.txt", "a+")
        file.write(str(arr) + "\n" + str(total) + "\n")


# 12 * 5 + 4 * 10 = 100

# broken
# if __name__ == "__main__":
#     times = 8
#     for i in range(times):
#         answer = handleAnswer()
#         if answer > 10 and times > 0:
#             # handleAnswer()
#             continue
#         else:
#             f = open("random80.txt", "a+")
#             f.write(str(answer) + " ")
if __name__ == "__main__":
    handleAnswer()
