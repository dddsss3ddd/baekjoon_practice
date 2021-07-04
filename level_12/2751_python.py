import sys

usrInCount = int(sys.stdin.readline().rstrip())

inArr = []
for _ in range(usrInCount):
    inArr.append(int(sys.stdin.readline().rstrip()))

inArr.sort()
print('\n'.join(map(str,inArr)))