import sys
usrin = int(sys.stdin.readline().rstrip())

for i in range(1,usrin+1):
    usrDataArr = sys.stdin.readline().rstrip().split(' ')
    print('Case #{0}: {1}'.format(i,(int(usrDataArr[0]))+int(usrDataArr[1])))
