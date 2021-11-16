import sys

full_num = {i for i in range(1,10)}
check_list = []
sudoku = []
for i in range(9):
	sudoku.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
	for j in range(9):
		if sudoku[i][j] == 0:
			check_list.append([i,j])

def get_nums(arr):
	return full_num.difference(arr)

def get_x_nums(x,y):
	q = get_nums(row[y] for row in sudoku)
	return q

def get_y_nums(x,y):
	t= get_nums(sudoku[x])
	return t

def get_sq_nums(x,y):
	w= get_nums(sum([a[y//3*3:y//3*3+3] for a in sudoku[x//3*3:x//3*3+3]],[]))
	return w

def find(index):
	if index == 0:
		x,y = check_list[0]
		tSet = full_num - set(row[y] for row in sudoku) - set(sudoku[x]) - set(sum([a[y//3*3:y//3*3+3] for a in sudoku[x//3*3:x//3*3+3]],[]))
		if(len(tSet) != 0):
			val = tSet.pop()
			sudoku[x][y] = val
			return True
		else:
			return False
	else:
		x,y = check_list[index]
		cSet = get_sq_nums(x,y).intersection(get_x_nums(x,y)).intersection(get_y_nums(x,y))
		if len(cSet) >= sudoku[x][y//3*3:y//3*3+3].count(0):
			for i in cSet:
				sudoku[x][y] = i
				if(find(index-1)):
					return True
		sudoku[x][y] = 0
		return False

find(len(check_list)-1)

for row in sudoku:
	print(' '.join(map(str,row)))