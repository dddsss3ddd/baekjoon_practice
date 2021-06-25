import math
import sys

lowNum,highNum = map(int,sys.stdin.readline().rstrip().split())

resultSum = 0
leastNum = -1

for i in range(lowNum,highNum+1):
    isPrime = True
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)

