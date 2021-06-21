usrin = int(input())

resArr = []
for i in range(usrin):
    calDataStr = input().split(' ')
    resArr.append(int(calDataStr[0])+int(calDataStr[1]))

for i in range(usrin):
    print(resArr[i])