import sys

full_num = {i for i in range(1,10)}
check_list = []
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
    for j in range(9):
        if sudoku[i][j] == 0:
            check_list.append([i,j])

def get_y_set(x,y):
    return full_num.difference(sudoku[x])

def get_x_set(x,y):
    return full_num.difference((row[y] for row in sudoku))

def get_sq_set(x,y):
    return full_num.difference(sum([arr[x*3:x*3+3] for arr in sudoku[y*3:y*3+3]],[]))

def get_possible_set(x,y):
    return get_y_set(x,y).union(get_x_set(x,y)).union(get_sq_set(x,y))

def recursive_sudoku(n):
    if n == 0:
        tset = get_possible_set(check_list[n][0],check_list[n][1])
        if len(tset) == 1:
            sudoku[check_list[n][0]][check_list[n][1]] = tset.pop()
            return True
        else:
            return False
    else:
        tset = get_possible_set(check_list[n][0],check_list[n][1])
        for i in tset:
            sudoku[check_list[n][0]][check_list[n][1]] = i
            if recursive_sudoku(n-1) is True:
                return True
        return False

for row in sudoku:
    print(' '.join(map(str,row)))


# 0 0 3 4 5 6 7 8 9
# 4 5 6 7 8 9 0 0 3
# 7 8 9 0 0 3 4 5 6
# 0 0 4 3 6 5 8 9 7
# 3 6 5 8 9 7 0 0 4
# 8 9 7 0 0 4 3 6 5
# 5 3 0 6 4 0 9 7 8
# 6 4 0 9 7 8 5 3 0
# 9 7 8 5 3 0 6 4 0
