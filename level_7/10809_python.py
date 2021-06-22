import sys
usrStrList = list(sys.stdin.readline().rstrip())
resultList = [-1]*(ord('z')-ord('a')+1)

count = len(usrStrList)-1
for a in reversed(usrStrList):
    resultList[ord(a)-ord('a')] = count
    count-=1

res = ''
for x in resultList:
    res+=str(x)
    res+=' '

print(res)
