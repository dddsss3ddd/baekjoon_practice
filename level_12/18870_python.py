import sys

sys.stdin.readline()
numArr = list(map(int,sys.stdin.readline().rstrip().split(' ')))
sortMap = dict((v,k) for k,v in enumerate(sorted(set(numArr)),start = 0))

print(' '.join(map(str,(sortMap[i] for i in numArr))))