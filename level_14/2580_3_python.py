#hard(2021-11-02)

import sys
import numpy as np
import itertools as it

from numpy.lib.arraypad import _pad_dispatcher

dummySudoku = np.zeros((9,9))
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
    
def check_integrity(arr):
    return np.setdiff1d(np.arange(1,10),arr)

def check_square(index):
    a,b = index//3,index%3
    return check_integrity(np.ravel(sudoku[a*3:a*3+3,b*3:b*3+3]))

def check_vertical(index):
    return check_integrity(sudoku[:,index])

def check_horizontal(index):
    return check_integrity(sudoku[index])

def propagate_square(x,y,val):
    for a,b in get_square_axis_from_axis(x,y):
        if dummySudoku[b][a] != 0:
            dummySudoku[b][a] = dummySudoku[b][a][dummySudoku[b][a] != val]
            taskQueue.append([a,b])

def propagate_vertical(x,y,val):
    for i in range(1,10):
        if dummySudoku[i][x] != 0:
            dummySudoku[i][x] = dummySudoku[i][x][dummySudoku[i][x] != val]
            taskQueue.append([x,i])

def propagate_horizontal(x,y,val):
    for i in range(1,10):
        if dummySudoku[y][i] != 0:
            dummySudoku[y][i] = dummySudoku[y][i][dummySudoku[y][i] != val]
            taskQueue.append([i,y])

def propagate_using(x,y,val):
    propagate_square(x,y,val)
    propagate_vertical(x,y,val)
    propagate_horizontal(x,y,val)

def summarize_candidates():
    for i in range(0,9):
        for j in range(0,9):
            if dummySudoku[i][j] != 0:
               dummySudoku[i][j] = np.intersect1d(np.intersect1d(dummySudoku[i][j][0],dummySudoku[i][j][1]),dummySudoku[i][j][2])
               if len(dummySudoku[i][j]) == 1:
                   taskQueue.append([j,i])

def find_zeros_and_candies():
    for i in range(1,10):
        for j in range(1,10):
            if sudoku[i][j] == 0:
                dummySudoku[i][j] = np.array([check_vertical(j),check_horizontal(i),check_square(get_square_index_from_axis(j,i))])

def task_working():
    while taskQueue:
        axis_x,axis_y = taskQueue.pop(0)
        if dummySudoku[axis_y][axis_x] != 0 and len(dummySudoku[axis_y][axis_x]) == 1:
            find = dummySudoku[axis_y][axis_x][0]
            sudoku[axis_y][axis_x] = find
            dummySudoku[axis_y][axis_x] = 0
            propagate_using(axis_x,axis_y,find)

def recurcive_finding(arr_x,arr_y,idx):
    if idx == 0:
        for i in dummySudoku[arr_y[idx]][arr_x[idx]]:
            sudoku[arr_y[idx]][arr_x[idx]] = i
            #TODO(sj:2021-11-04):add all integrity check here.




find_zeros_and_candies()
summarize_candidates()
task_working()

if np.count_nonzero(sudoku == 0) != 0:



np.savetxt(sys.stdout,sudoku,newline='\n',fmt='%i')
