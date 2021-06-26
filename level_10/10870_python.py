import sys
import math

def pibo(a):
    if a == 0:
        return 0
    elif a <= 2:
        return 1
    else :
        return pibo(a-1)+pibo(a-2)

print(pibo(int(sys.stdin.readline().rstrip())))
