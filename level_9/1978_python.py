import math
import sys

usrIn = int(sys.stdin.readline().rstrip())

result = usrIn
numbers = map(int,sys.stdin.readline().rstrip().split())
for i in numbers:
    if i == 1:
        result-=1
        continue
    for j in range(2,i):
        if i%j == 0:
            result-=1
            break

print(result)

