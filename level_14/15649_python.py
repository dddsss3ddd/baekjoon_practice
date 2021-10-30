import sys

def permutation(list_A,list_B,leftcount):
    # print('listA',list_A)
    # print('listB',list_B)
    # print('LC',leftcount)
    if leftcount <= 1:
        for i in range(len(list_B)):
            tList = list(list_A)
            tList.append(list_B[i])
            print(' '.join(map(str,tList)))
    else:
        for i in range(len(list_B)):
            tList = list(list_A)
            tList.append(list_B[i])
            permutation(tList,[item for item in list_B if item != list_B[i]],leftcount-1)


N,M = map(int,sys.stdin.readline().rstrip().split())

permutation([],list(range(1,N+1)),M)