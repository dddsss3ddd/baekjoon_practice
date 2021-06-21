import sys

resultCount = int(sys.stdin.readline().rstrip())

for i in range(resultCount):
    points = list(sys.stdin.readline().rstrip())
    totalPoint = 0
    advantage = 0

    for i in points:
        if i == 'O':
            advantage +=1
            totalPoint += advantage
        else:
            advantage = 0

    print(totalPoint)