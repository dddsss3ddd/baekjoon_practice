import sys

resultCount = int(sys.stdin.readline().rstrip())

for i in range(resultCount):
    points = list(map(int,sys.stdin.readline().rstrip().split()))
    studentCount = points.pop(0)
    average = sum(points)/studentCount
    overAverage = 0

    for i in points:
        if i > average:
            overAverage+=1
    
    print("{:.3f}%".format(overAverage/studentCount*100))
