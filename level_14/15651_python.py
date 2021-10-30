import sys
N,M = map(int,sys.stdin.readline().rstrip().split())

point= [1 for i in range(M)]

while point[0] <= N :
    print(' '.join(map(str,point)))

    for i in range(M-1,-1,-1):
        point[i] += 1
        if point[i] <= N:
            break;
        elif i != 0:
            point[i] = 1
