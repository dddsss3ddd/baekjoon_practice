from collections import defaultdict
import sys
from typing import DefaultDict

usrCount = int(sys.stdin.readline().rstrip())

mean = 0
middle = 0
minVal = 0
maxVal = 0

valMap = {}
for i in range(usrCount):
    newVal = int(sys.stdin.readline().rstrip())
    if newVal in valMap:
        valMap[newVal] += 1
    else:
        valMap[newVal] = 1

mean = round(sum(a*b for a ,b in zip(list(valMap.keys()),valMap.values()))/usrCount)
keyList = list(valMap.keys())
keyList.sort()
usrCount = (usrCount-1)//2

for i in keyList :
    usrCount -= valMap[i]
    if usrCount < 0 :
        middle = i
        break

# middle = keyList[(len(keyList)-1)//2]
minVal = min(valMap)
maxVal = max(valMap)

d_inv = defaultdict(list)
for k,v in valMap.items():
    d_inv[v].append(k)

many = d_inv[max(d_inv)]
many.sort()



print(mean)
print(middle)
print(many[1] if len(many)>1 else many[0])
print(maxVal-minVal)