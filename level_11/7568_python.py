import sys

usrIn =  sys.stdin.readline().rstrip()
national = int(usrIn)
count = len(usrIn)

min = 0
for ii in range(national-9*(count-1)-int(usrIn[0]),national):
     if national == ii + sum(map(int,[char for char in (str(ii))])):
        min = ii
        break

print(min)
