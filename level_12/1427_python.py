import sys


ans = list(sys.stdin.readline().rstrip())
ans.sort(reverse=True)
print(''.join(ans))