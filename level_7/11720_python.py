import sys
numCount = sys.stdin.readline().rstrip()
numList = list(str(sys.stdin.readline().rstrip()))

res = 0
for i in numList:
    res+=int(i)

print(res)
