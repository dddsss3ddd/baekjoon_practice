import sys


# for xx in range(1,1000001):
    # usrIn =  str(xx)
    # national = xx
    # count = len(str(xx))

usrIn =  sys.stdin.readline().rstrip()
national = int(usrIn)
count = len(usrIn)

min = 0
for ii in range(national-9*(count-1)-int(usrIn[0]),national):
    if national == ii + sum(map(int,list(str(ii)))):
    # if national == ii + sum(map(int,[char for char in (str(ii))])):
        min = ii
        break

print(min)

    # newVal = 0
    # start_num = max(0, xx - 9*len(str(xx)))

    # for i in range(start_num, xx):
    #     if i + sum(map(int, str(i))) == xx:
    #         newVal = i
    #         break

    # if xx%1000 == 0:
    #     print('working {}'.format(xx))

    # if newVal != min:
    #     print(newVal,min,xx)
