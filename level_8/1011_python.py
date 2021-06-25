import math
import sys

usrIn = int(sys.stdin.readline().rstrip())

for _ in range(usrIn):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    distance = b-a - 1

    alpha = math.ceil((((distance+1)*4+1)**0.5-1)/2)
    beta = math.ceil((distance+1)**0.5-1)

    if(alpha<=beta):
        print(2*alpha)
    else:
        print(2*beta+1)


