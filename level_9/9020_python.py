import math
import sys

size = 10000
primeSet = set(i for i in range(3,9997,2))
primeSet.add(2)

numRange = int(size**0.5)+1
for i in range(3,numRange,2):
    if i in primeSet :
        primeSet -= set(j for j in range(i*2,9998,i))

primeList = list(primeSet)
primeList.sort()
totSize = len(primeList)

usrTrial = int(sys.stdin.readline().rstrip())

for _ in range(usrTrial):
    usrin = int(sys.stdin.readline().rstrip())
    reSultList = []
    for i in range(len(primeList)):
        if primeList[i]<= usrin//2:
            if usrin-primeList[i] in primeSet:
                reSultList.append([primeList[i],usrin-primeList[i]])
        else:
            break
    print(reSultList[-1][0],reSultList[-1][1])


