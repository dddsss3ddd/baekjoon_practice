import sys

count = 0
usrin = int(sys.stdin.readline().rstrip())

dataMap = list(map(int,sys.stdin.readline().rstrip().split()))
dataMap.sort()


print(dataMap[0], dataMap[usrin-1])
