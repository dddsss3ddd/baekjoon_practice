import sys

def hanoi(diskCount, presentStack, targetStack):
    if diskCount == 1:
        return 1, f'\n{presentStack} {targetStack}'
    else:
        newTarget = 6-presentStack-targetStack

        a,b = hanoi(diskCount-1,presentStack,newTarget)
        a += 1
        b += f'\n{presentStack} {targetStack}'
        c,d = hanoi(diskCount-1,newTarget,targetStack)
        return a+c,b+d


usrIn = int(sys.stdin.readline().rstrip())
a,b = hanoi(usrIn,1,3)
print(a,end='')
print(b)

