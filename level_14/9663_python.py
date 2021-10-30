import sys
import copy


N = int(sys.stdin.readline().rstrip())

pannel = [[1 for j in range(N)] for i in range(N)]

# def horizonRemove(tPannel,f):
#     for i in range(N):
#         tPannel[f][i] = 0

def verticalRemove(tPannel,f,p):
    for i in range(f+1,N):
        tPannel[i][p] = 0
        # print(i,' floor ',p,'point is ',tPannel[i][p])

def diagonalRemove(tPannel,f,p):
    #neg
        for i in range(1,N-f):
            if p-i >= 0 and f+i < N:
                tPannel[f+i][p-i] = 0
            else:
                break
    #pos
        for i in range(1,N-f):
            if p+i < N and f+i < N:
                tPannel[f+i][p+i] = 0
            else:
                break

def allRemove(tPannel,f,p):
    #neg
        for i in range(1,N-f):
            tPannel[i+f][p] = 0
            if p-i >= 0 and f+i < N:
                tPannel[f+i][p-i] = 0
            elif p+i < N and f+i < N:
                tPannel[f+i][p+i] = 0

def getNextCase(tPannel,f,p):
    if f+1 == N:
        # print('=================================')
        # for x in range(N):
        #     print('tPannel',tPannel[x])
        # print('=================================')
        return sum(tPannel[f])
    else:
        res = 0
        nPannel = copy.deepcopy(tPannel)
        nPannel[f][p] = 2
        # print('nPannel',nPannel)
        # horizonRemove(nPannel,f)
        allRemove(nPannel,f,p)
        # diagonalRemove(nPannel,f,p)
        for x in range(0,N):
            if nPannel[f+1][x] == 1 :
                res += getNextCase(nPannel,f+1,x)
                # print('tval',nPannel,x,res)
        return res

ans = 0
for i in range(N):
    ans += getNextCase(pannel,0,i)
print(ans)


