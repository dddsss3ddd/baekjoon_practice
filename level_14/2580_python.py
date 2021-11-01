import sys
import numpy as np

for i in range(9):
    sudoku = np.fromstring(sys.stdin.readline().rstrip(),dtype=int,sep=' ')

def getMissingNum(numArr):
    missingNum = np.arange(1,10)
    missingIndex = np.array()

    for i in range(1,10):
        if numArr[i] != 0:
            missingNum[numArr[i]-1] = 0
        else:
            np.append(missingIndex,i)
    
    return np.transpose(np.vstack(missingNum,missingIndex))

def checkArray(arrayType,line):
    zero = np.array()
    if arrayType == 'vertical':
        zero = np.count_nonzero(sudoku[:,line] == 0)
    elif arrayType == 'horizontal':
        zero = np.count_nonzero(sudoku[line] == 0)
    else:
        a,b = line//3,line%3
        zero = np.ravel(sudoku[b*3:b*3+3,a*3:a*3+3])

    if zero == 0:
        return 0
    elif zero == 1:
        missing = getMissingNum(sudoku[:,line])
        if arrayType != 'square':
            sudoku[missing[0][1]] = missing[0][0]
        else:

        return 0
    else:
        return zero







print()