import sys


for xx in range(1,1000001):
    usrIn =  str(xx)
    national = xx
    count = len(str(xx))

    

    min = 0
    for ii in range(national-9*(count-1)-int(usrIn[0]),national):
        if national == ii + sum(map(int,list(str(ii)))):
        # if national == ii + sum(map(int,[char for char in (str(ii))])):
            min = ii
            break

    
    k = int(xx)
    numList = []
    newVal = 0
    if k < 10:
        newVal = k
    else:
        for nn in range(k-1, -1, -1):
            num = str(nn)
            sum = 0
            for j in range(len(num)):
                sum += int(num[j])
            if sum + nn == k:
                numList.append(nn)
        numList.sort()
        if len(numList) == 0:
            newVal = 0
        else:
            newVal = numList[0]

    
    if newVal != min:
        print(newVal,min,xx)