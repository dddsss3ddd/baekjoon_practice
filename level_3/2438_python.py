import sys
usrin = int(sys.stdin.readline().rstrip())

for x in range(1,usrin+1):
    star = ""
    for i in range(x):
        star+='*'
    print(star)
    
