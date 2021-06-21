import sys
usrin = sys.stdin.readline().rstrip().split(' ')

res = ""

usrrange = int(usrin[0])
limit = int(usrin[1])
usrArr = sys.stdin.readline().rstrip().split(' ')
for x in usrArr:
    if int(x) < limit:
        res+=(x+' ')

print(res)