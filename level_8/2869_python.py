
import sys
import math

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    H,W,N = map(int,sys.stdin.readline().rstrip().split())
    print('{}{:02d}'.format(N%H if N%H !=0 else H,N//H +1 if N%H != 0 else N//H))
