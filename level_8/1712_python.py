import sys
objects = list(map(int,sys.stdin.readline().rstrip().split()))

if objects[1]>=objects[2]:
    print(-1)
else:
    print(objects[0]//(objects[2]-objects[1])+1)