import sys
import copy

# import time

N = int(sys.stdin.readline().rstrip())

# start = time.time()

pannel = [[0 for j in range(N)] for i in range(N)]
def paintLeftDiagonal(y,x):
    a,b = x,y

    while a > 0 and b > 0:
        a=a-1
        b=b-1
        if(pannel[b][a] == 0):
            pannel[b][a] = y

def paintRightDiagonal(y,x):
    a,b = x,y

    while a < N-1 and b > 0:
        a=a+1
        b=b-1
        if(pannel[b][a] == 0):
            pannel[b][a] = y

def paintVirtical(y,x):
    b = y

    while b > 0:
        b=b-1
        if(pannel[b][x] == 0):
            pannel[b][x] = y
    
def clearPannel(l):
    for j in range(l,-1,-1):
        for i in range(N):
            if(pannel[j][i] <= l):
                pannel[j][i] = 0
    
def countCase():
    # for i in range(N):
    #     print(pannel[i])
#    print('')
    return pannel[0].count(0)

def findCase(y):
    if y == 0:
        return countCase()
    else:
        ans = 0
        for i in range(N):
            if(pannel[y][i] == 0):
                pannel[y][i] = y
                paintLeftDiagonal(y,i)
                paintRightDiagonal(y,i)
                paintVirtical(y,i)

#                print('level',y)
#                for s in range(N):
#                    print(pannel[s])

                ans += findCase(y-1)
                clearPannel(y)
        return ans



ans = 0

if N == 1:
    ans = 1
elif N < 4:
    pass
else:
    for i in range(N//2):
#        print('case',i)
        pannel[N-1][i] = N-1
        paintLeftDiagonal(N-1,i)
        paintRightDiagonal(N-1,i)
        paintVirtical(N-1,i)
        ans += findCase(N-2)
        clearPannel(N-1)
    ans = ans*2
    if N%2 == 1:
        pannel[N-1][N//2] = N-1
        paintLeftDiagonal(N-1,N//2)
        paintRightDiagonal(N-1,N//2)
        paintVirtical(N-1,N//2)
        ans += findCase(N-2)

print(ans)
# print('elapse : ',time.time()-start)

