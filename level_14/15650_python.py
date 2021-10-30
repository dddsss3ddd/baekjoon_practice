import sys
from itertools import combinations 

N,M = map(int,sys.stdin.readline().rstrip().split())

print('\n'.join(
    list(
        map(' '.join,
        combinations(
            map(str,
            range(1,N+1)),M)))))


