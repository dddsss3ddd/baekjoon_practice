from collections import defaultdict
import sys

usrInCount = int(sys.stdin.readline().rstrip())

valMap = defaultdict(list)
for _ in range(usrInCount):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    valMap[y] += [x]

for i in sorted(valMap.keys()):
    for j in sorted(valMap[i]):
        print('{} {}'.format(j,i))
