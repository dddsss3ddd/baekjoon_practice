import sys
import math

for _ in range(int(sys.stdin.readline().rstrip())):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().rstrip().split())

    dSq = (x1-x2)**2+(y1-y2)**2

    if dSq == 0 and r1==r2:
        print(-1)
    elif dSq > (r1+r2)**2 or (max(r1,r2)-min(r1,r2))**2 > dSq:
        print(0)
    elif dSq == (r1+r2)**2 or (max(r1,r2)-min(r1,r2))**2 == dSq:
        print(1)
    else:
        print(2)