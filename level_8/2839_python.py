import sys
import math

T = int(sys.stdin.readline().rstrip())
for i in range(T//5,-1,-1):
    if((T-(5*i))%3==0):
        print(i+((T-(5*i))//3))
        break
    else:
        if i != 0:
            continue
        else:
            print(-1)

