import sys
import math

def recursive(floor,order):
    if floor == 0:
        return range(1,order+1)
    else:
        localResult = recursive(floor-1,order)
        return [sum(localResult[:i]) for i in range(1,order+1)]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    k = int(sys.stdin.readline().rstrip()) #floor
    n = int(sys.stdin.readline().rstrip()) #order

    print(sum(recursive(k-1, n)))


