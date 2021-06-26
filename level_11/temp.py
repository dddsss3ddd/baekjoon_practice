import sys


national = int(sys.stdin.readline().rstrip())

count = len(str(national))

numList = []
newVal = 0
for ii in range(1,national):
    if national == ii + sum(map(int,list(str(ii)))):
    # if national == ii + sum(map(int,[char for char in (str(ii))])):
        numList.append(ii)

numList.sort()

if len(numList) != 0:
    newVal = numList[0]

print(newVal)