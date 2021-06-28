import sys

h,w = map(int,sys.stdin.readline().rstrip().split())

WpaintCountArray = [[0 for x in range(w-7)]for y in range(h)]#[h,w]
BpaintCountArray = [[0 for x in range(w-7)]for y in range(h)]#[h,w]
wbRef = 'WBWBWBWB'
bbRef = 'BWBWBWBW'

for i in range(h):
    board = sys.stdin.readline().rstrip()
    for j in range(len(board)-7):
        for k in range(8):
            if board[j+k] != wbRef[k]:
                WpaintCountArray[i][j] += 1
            if board[j+k] != bbRef[k]:
                BpaintCountArray[i][j] += 1

def getPaintCount(wStart,hStart,sColor):
    if sColor == 'W':
        return sum(WpaintCountArray[x][wStart]+BpaintCountArray[x+1][wStart] for x in range(hStart,hStart+8,2))
    else:
        return sum(WpaintCountArray[x+1][wStart]+BpaintCountArray[x][wStart] for x in range(hStart,hStart+8,2))

resSet = set()
for i in range(w-7):
    for j in range(h-7):
        resSet.add(getPaintCount(i,j,'W'))
        resSet.add(getPaintCount(i,j,'B'))

print(min(resSet))