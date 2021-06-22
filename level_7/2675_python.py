import sys
quizCount = int(sys.stdin.readline().rstrip())

for i in range(quizCount):
    quizStr = sys.stdin.readline().rstrip().split()
    resStr = ''
    for x in list(quizStr[1]):
        resStr+=x*int(quizStr[0])
    print(resStr)


