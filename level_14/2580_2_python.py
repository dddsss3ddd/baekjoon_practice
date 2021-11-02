#hard(2021-11-02)

from operator import truediv
import sys
import numpy as np
import itertools as it

dummySudoku = np.zeros((9,9))
sudoku = np.array(np.fromstring(sys.stdin.readline().rstrip(),dtype=int,sep=' '))
for i in range(8):
    sudoku=np.vstack([sudoku,np.array(np.fromstring(sys.stdin.readline().rstrip(),dtype=int,sep=' '))])

taskQueue = []

def get_square_index_from_axis(x,y):
    return 3*(y//3)+x//3

def t_comb(a,b):
    c = []
    for i in a:
        for j in b:
            c.append([i,j])
    return c

def get_square_axis_from_axis(x,y):
    axis_x=np.arange(start=3*(x//3),stop=3*(x//3)+3)
    axis_y=np.arange(start=3*(y//3),stop=3*(y//3)+3)
    res = np.array(t_comb(axis_x,axis_y))
    res = np.delete(res,np.where((res[:,0]==x)&(res[:,1]==y)),axis=0)
    return res
    
def remove_used(x,y,dir,num):
    is_removed = False
    if dummySudoku[y][x] != 0:
        if dir == 'v':
            dummySudoku[y][x][0].remove(num)
            if len(dummySudoku[y][x][0]) == 1:
                sudoku[y][x] = dummySudoku[y][x][0][0]
                dummySudoku[y][x] = 0
                taskQueue.append([y,x,'v'])
                is_removed = True
        elif dir == 'h':
            dummySudoku[y][x][1].remove(num)
            if len(dummySudoku[y][x][1]) == 1:
                sudoku[y][x] = dummySudoku[y][x][1][0]
                dummySudoku[y][x] = 0
                taskQueue.append([y,x,'h'])
                is_removed = True
        else:
            dummySudoku[y][x][2].remove(num)
            if len(dummySudoku[y][x][2]) == 1:
                sudoku[y][x] = dummySudoku[y][x][2][0]
                dummySudoku[y][x] = 0
                taskQueue.append([y,x,'s'])
                is_removed = True
                
        if is_removed:
            for i in range(1,10):
                if dummySudoku[i][x] != 0:
                    dummySudoku[i][x] = dummySudoku[i][x][dummySudoku[i][x] != num]
                if dummySudoku[y][i] != 0:
                    dummySudoku[y][i] = dummySudoku[y][i][dummySudoku[y][i] != num]
            for tAxis in get_square_axis_from_axis(x,y):
                if dummySudoku[tAxis[1]][tAxis[0]] != 0:
                    dummySudoku[tAxis[1]][tAxis[0]] = dummySudoku[tAxis[1]][tAxis[0]][dummySudoku[tAxis[1]][tAxis[0]] != num]



np.savetxt(sys.stdout,sudoku,newline='\n',fmt='%i')
