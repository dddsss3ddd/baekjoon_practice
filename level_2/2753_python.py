usrin = int(input())

res = 0
if usrin%400 == 0:
    res = 1
elif usrin%4 == 0:
    if usrin%100 != 0:
        res = 1

print(res)


