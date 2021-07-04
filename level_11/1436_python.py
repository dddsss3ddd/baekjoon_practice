import sys

def getNextNum( present: str):
    numSplit = present.split('666',maxsplit=1)
    
    if len(numSplit[1]) > 0:
        if str(10**len(numSplit[1])-1) != numSplit[1]:
            numSplit[1] = ("{:0"+str(len(numSplit[1]))+"d}").format(int(numSplit[1])+1)
        else:
            numSplit[0] = str(int(numSplit[0]+'6'*min(3,len(numSplit[1])))+1)+'0'*max(0,len(numSplit[1])-3)
            numSplit[1] = ''
    else:
        numSplit[0] = str(int(numSplit[0])+1)
        if '666' in numSplit[0]:
            numSplit2 = numSplit[0].split('666',maxsplit=1)
            numSplit[0] = numSplit2[0]
            numSplit[1] = numSplit2[1]+'000'
        else:
            count6 = 0
            for i in numSplit[0][::-1]:
                if i == '6':
                    count6 +=1
                else:
                    break
                           
            numSplit[1] = numSplit[1]+('0'*count6)
            numSplit[0] = numSplit[0][:(len(numSplit[0])-count6)]
        
    return numSplit[0]+'666'+numSplit[1]

usrIn = int(sys.stdin.readline().rstrip())

# resultArray = ['','666','1666']+['']*9998
# for i in range(3,10001):
#     resultArray[i] = getNextNum(resultArray[i-1])


# print(resultArray[usrIn])


if usrIn == 1:
    print('666')
elif usrIn == 2:
    print('1666')
else:
    nextVersion = '1666'
    for _ in range(usrIn-2):
        nextVersion = getNextNum(nextVersion)
    print(nextVersion)


