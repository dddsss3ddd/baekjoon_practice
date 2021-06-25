import math
import sys

size = 123456*2
primeList = [0,0]+[1]*(size)
numRange = int(size**0.5+1.5)
for i in range(2,numRange):
    if primeList[i] == 1:
        primeList[i*2::i] = [0]*((size-i)//i)

while True:
    usrin = int(sys.stdin.readline().rstrip())
    if(usrin == 0):
        break
    print(sum(primeList[usrin+1:usrin*2+1]))

