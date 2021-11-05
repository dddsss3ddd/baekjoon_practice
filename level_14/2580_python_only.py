import sys
import itertools as it


dummySudoku = [[{} for i in range(1,10)] for j in range(1,10)]
sudoku = [list(map(int,sys.stdin.readline().rstrip().split(' ')))]
for i in range(8):
    sudoku.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

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
    axis_x=[i for i in range(3*(x//3),3*(x//3)+3)]
    axis_y=[i for i in range(3*(y//3),3*(y//3)+3)]
    ta = t_comb(axis_x,axis_y)
    ta.remove([x,y])
    return ta
    
def check_integrity(arr):
    return {i for i in range(1,10)}.difference(arr)

def check_square(index):
    a,b = index//3,index%3
    return check_integrity(sum([x[b*3:b*3+3] for x in sudoku[a*3:a*3+3]],[]))

def check_vertical(index):
    return check_integrity(row[index] for row in sudoku)

def check_horizontal(index):
    return check_integrity(sudoku[index])

def check_all_integrity():
    for i in range(0,9):
        if len(check_square(i)) != 0:
            return False
        if len(check_vertical(i)) != 0:
            return False
        if len(check_horizontal(i)) != 0:
            return False
    return True

def propagate_square(x,y,val):
    for a,b in get_square_axis_from_axis(x,y):
        if len(dummySudoku[b][a]) != 0:
            dummySudoku[b][a].discard(val)
            taskQueue.append([a,b])

def propagate_vertical(x,y,val):
    for i in range(0,9):
        if len(dummySudoku[i][x]) != 0:
            dummySudoku[i][x].discard(val)
            taskQueue.append([x,i])

def propagate_horizontal(x,y,val):
    for i in range(0,9):
        if len(dummySudoku[y][i]) != 0:
            dummySudoku[y][i].discard(val)
            taskQueue.append([i,y])

def propagate_using(x,y,val):
    propagate_square(x,y,val)
    propagate_vertical(x,y,val)
    propagate_horizontal(x,y,val)

def summarize_candidates():
    for i in range(0,9):
        for j in range(0,9):
            if len(dummySudoku[i][j]) != 0:
               dummySudoku[i][j] = set.intersection(dummySudoku[i][j][0],dummySudoku[i][j][1],dummySudoku[i][j][2])
               if len(dummySudoku[i][j]) == 1:
                   taskQueue.append([j,i])

def find_zeros_and_candies():
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:                
                dummySudoku[i][j] = [check_vertical(j),check_horizontal(i),check_square(get_square_index_from_axis(j,i))]
    for i in dummySudoku:
        print(i)

def task_working():
    while taskQueue:
        axis_x,axis_y = taskQueue.pop(0)
        if len(dummySudoku[axis_y][axis_x]) == 1:
            find = dummySudoku[axis_y][axis_x].pop()
            sudoku[axis_y][axis_x] = find
            dummySudoku[axis_y][axis_x] = {}
            propagate_using(axis_x,axis_y,find)

def recurcive_finding(pos_arr,idx):
    if idx == 0:
        for i in dummySudoku[pos_arr[idx][1]][pos_arr[idx][0]]:
            sudoku[pos_arr[idx][1]][pos_arr[idx][0]] = i
            if check_all_integrity():
                return True
        return False
    else:
        for i in dummySudoku[pos_arr[idx][1]][pos_arr[idx][0]]:
            sudoku[pos_arr[idx][1]][pos_arr[idx][0]] = i
            if recurcive_finding(pos_arr,idx-1):
                return True
        return False

find_zeros_and_candies()
summarize_candidates()
task_working()

find_all = sum(row.count(0) for row in sudoku)

if find_all != 0:
    loc = [(ix,iy) for ix, row in enumerate(sudoku) for iy, i in enumerate(row) if i == 0]
    if not recurcive_finding(loc,len(loc)-1):
        print('error')
        pass

for row in sudoku:
    print(' '.join(map(str,row)))

