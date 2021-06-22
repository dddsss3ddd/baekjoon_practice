import sys

def checkHan(a):
    varList = list(str(a))
    ansList = [0]*len(varList)
    for i in range(len(varList)-1):
        ansList[i] = int(varList[i+1])-int(varList[i])
        if i>0:
            if ansList[i-1] != ansList[i]:
                return False
    return True

usrin = int(sys.stdin.readline().rstrip())

res = 99

if usrin < 100:
    print(usrin)
else :
    for i in range(100,usrin+1):
        if(checkHan(i)):
            res+=1
    print(res)