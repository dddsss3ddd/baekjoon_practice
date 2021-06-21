import sys
usrin = int(sys.stdin.readline().rstrip())

for i in range(usrin):
    inDataStr = sys.stdin.readline().rstrip().split(' ')
    print(int(inDataStr[0])+int(inDataStr[1]))
