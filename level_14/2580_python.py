import sys
import numpy as np

sudoku = np.array()
checkList = []

for i in range(9):
    sudoku = np.vstack(np.fromstring(sys.stdin.readline().rstrip(),dtype=int,sep=' '))

def fill_one_missing(dir,line):
    if dir == 'v':
        np.where(sudoku[line]==0,45-sum(sudoku[line]),sudoku[line])
    elif dir == 'h':
        np.where(sudoku[:,line]==0,45-sum(sudoku[:,line]),sudoku[:,line])
    else:
        a,b = line//3,line%3
        np.where(sudoku[b*3:b*3+3,a*3:a*3+3]==0,45-sum(sudoku[b*3:b*3+3,a*3:a*3+3]),sudoku[b*3:b*3+3,a*3:a*3+3])

def check_location(x,y):
    if np.count_nonzero(sudoku[y] == 0) == 1:
        fill_one_missing()
        checkList.append(['v',x])
        checkList.append(['s',3*(y//3)+x%3])
    elif np.count_nonzero(sudoku[:,x] == 0) == 1:
        checkList.append(['h',y])
        checkList.append(['s',3*(y//3)+x%3])
    elif np.count_nonzero(sudoku[3*(x//3):3*(x//3)+3,3*(y//3):3*(y//3)+3]) == 1:
        fill_one_missing('s',3*(y//3)+x//3)
        checkList.append(['v',x])
        checkList.append(['h',y])



def get_zero_pos():
    x,y = np.array,np.where(sudoku == 0)
    for a,b in x,y:
        check_location(a,b)
    
    while checkList:
        checkItem = checkList.pop()
        if checkItem[0] == 'v':
            if np.count_nonzero(sudoku[:,checkItem[1]]==0) == 1:
                
                fill_one_missing(checkItem[0],checkItem[1])

        elif checkItem[0] == 'h':

        else:





def getMissingNum(numArr):
    missingNum = np.arange(1,10)
    missingIndex = np.array()

    t1 = numArr[numArr != 0]
    if t1 != np.unique(t1):
        return np.array([[-1,-1],[-1,-1]])

    for i in range(1,10):
        if numArr[i] != 0:
            missingNum[numArr[i]-1] = 0
        else:
            np.append(missingIndex,i)

    return np.transpose(np.vstack(missingNum,missingIndex))

def checkArray(arrayType,line):
    zero = 0
    if arrayType == 'vertical':
        zero = np.count_nonzero(sudoku[:,line] == 0)
    elif arrayType == 'horizontal':
        zero = np.count_nonzero(sudoku[line] == 0)
    else:
        a,b = line//3,line%3
        tArr = np.ravel(sudoku[b*3:b*3+3,a*3:a*3+3])
        zero = np.count_nonzero(tArr == 0)

    if zero == 0:
        return 0,0,0
    elif zero == 1:
        x,y=0,0
        if arrayType == 'horizontal':
            missing = getMissingNum(sudoku[line])
            x=line
            y=missing[0][1]
            if(missing[0][0] == -1):
                return -1,x,y
            sudoku[line][missing[0][1]] = missing[0][0]
        elif arrayType == 'vertical':
            missing = getMissingNum(sudoku[:,line])
            x=missing[0][1]
            y=line
            if(missing[0][0] == -1):
                return -1,x,y
            sudoku[missing[0][1]][line] = missing[0][0]            
        else:
            a,b = line//3,line%3
            missing = getMissingNum(np.ravel(sudoku[b*3:b*3+3,a*3:a*3+3]))
            x=b+missing[0][1]%3
            y=a+missing[0][1]//3
            if(missing[0][0] == -1):
                return -1,x,y
            sudoku[b+missing[0][1]%3][a+missing[0][1]//3] = missing[0][0]
        return 1,x,y
    else:
        return zero,0,0







print()