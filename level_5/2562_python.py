import sys

max = 0
point = 0
for i in range(9):
    usrVal = int(sys.stdin.readline().rstrip())
    if max < usrVal:
        max = usrVal
        point = i+1

print(max)
print(point)