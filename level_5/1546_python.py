import sys

objects = int(sys.stdin.readline().rstrip())
points = list(map(int,sys.stdin.readline().rstrip().split()))

points.sort()
sum = 0
for i in range(len(points)):
    sum += points[i]/points[len(points)-1]*100

print(sum/len(points))