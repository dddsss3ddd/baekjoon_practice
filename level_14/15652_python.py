import sys
from itertools import combinations_with_replacement

N,M = map(int,sys.stdin.readline().rstrip().split())

print('\n'.join(
    list(
        map(' '.join,
        combinations_with_replacement(
            map(str,
            range(1,N+1)),M)))))


