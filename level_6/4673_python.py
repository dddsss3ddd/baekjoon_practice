def splitAndCalculate(a):
    res = a
    varList = list(str(a))
    for i in varList:
        res += int(i)
    return res

for i in range(1,10001):
    isPrint = True
    if(i<10):
        for x in range(i-9,i):
            if(x<1):
                continue
            if(splitAndCalculate(x) == i):
                isPrint = False
                break
        if isPrint:
            print(i)
    elif(i//1000 >0): #10
        for x in range(i-36,i):
            if(splitAndCalculate(x) == i):
                isPrint = False
                break
        if isPrint:
            print(i)
    elif(i//100 > 0): #100
        for x in range(i-27,i):
            if(splitAndCalculate(x) == i):
                isPrint = False
                break
        if isPrint:
            print(i)
    elif(i//10 > 0): #1000
        for x in range(i-18,i):
            if(x<1):
                continue
            if(splitAndCalculate(x) == i):
                isPrint = False
                break
        if isPrint:
            print(i)
    isPrint = True


