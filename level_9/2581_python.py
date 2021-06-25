import math
import sys

lowNum = int(sys.stdin.readline().rstrip())

resultSum = 0
leastNum = -1

highNum = int(sys.stdin.readline().rstrip())
for i in range(highNum,lowNum-1,-1):
    isPrime = True
    if i == 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        leastNum = i
        resultSum += i

if leastNum == -1:
    print(leastNum)
else:
    print(resultSum)
    print(leastNum)

