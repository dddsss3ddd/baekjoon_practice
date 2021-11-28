import sys

with open("E:/temp/20211116/tt", "w") as f:
    
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
        # print('getx=',[row[y] for row in sudoku])
        q = get_nums(row[y] for row in sudoku)
        # print('xres=',q)
        return q

    def get_y_nums(x,y):
        # print('gety=',sudoku[x])
        t= get_nums(sudoku[x])
        # print('yres=',t)
        return t

    def get_sq_nums(x,y):
        # print('getq=',sum([a[y//3*3:y//3*3+3] for a in sudoku[x//3*3:x//3*3+3]],[]))
        w= get_nums(sum([a[y//3*3:y//3*3+3] for a in sudoku[x//3*3:x//3*3+3]],[]))
        # print('qres=',w)
        return w

    def find(index):
        if index == 0:
            x,y = check_list[0]
            tSet = full_num - set(row[y] for row in sudoku) - set(sudoku[x]) - set(sum([a[y//3*3:y//3*3+3] for a in sudoku[x//3*3:x//3*3+3]],[]))
            print('index=',index,', pos = ',x,y,', set=',tSet,file=f)
            if(len(tSet) != 0):
                val = tSet.pop()
                print('x,y=',x,y,', update=',val,file=f)
                sudoku[x][y] = val
                for row in sudoku:
                        print(' '.join(map(str,row)),file=f)
                return True
            else:
                return False
        else:
            x,y = check_list[index]
            cSet = get_sq_nums(x,y).intersection(get_x_nums(x,y)).intersection(get_y_nums(x,y))
            print('index=',index,', pos = ',x,y,', zero=',sudoku[x][y//3*3:y//3*3+3].count(0),', set=',cSet,file=f)
            if len(cSet) !=0 :
                for i in cSet:
                    sudoku[x][y] = i
                    print('x,y=',x,y,', update=',i,file=f)
                    for row in sudoku:
                        print(' '.join(map(str,row)),file=f)
                    if(find(index-1)):
                        return True
            sudoku[x][y] = 0
            return False

    find(len(check_list)-1)

    print('===========================================')

    for row in sudoku:
        print(' '.join(map(str,row)))

    f.close()