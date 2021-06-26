import sys

def recMultiple(a):
    if a < 2:
        return 1
    elif a == 2:
        return 2
    else :
        return a*recMultiple(a-1)

print(recMultiple(int(sys.stdin.readline().rstrip())))