from collections import defaultdict
import sys

uIn = sys.stdin.readline
uOut = sys.stdout.write

usrInCount = int(uIn())

arr = {}
arr = defaultdict(lambda:0,arr)

for _ in range(usrInCount):
    uNum = int(uIn().rstrip())
    arr[uNum] = arr[uNum]+1

uList = list(arr.keys())
uList.sort()

for i in uList:
    for _ in range(0,arr[i]):
        uOut(str(i)+'\n')