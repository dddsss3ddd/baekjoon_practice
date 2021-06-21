import sys

while(True):
    usrin = sys.stdin.readline().rstrip().split(' ')
    a = int(usrin[0])
    b = int(usrin[1]) 
    if a+b ==0:
        break
    else:
        print(a+b)
