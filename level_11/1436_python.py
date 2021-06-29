import sys


preStr = '0'
postStr = ''

def stringAdder(a, b):
    lenA = len(a)
    lenB = len(b)
    adder = 0

    reverseStringA = a[::-1]
    reverseStringB = b[::-1]
    sumString = ''

    for i in range(min(lenA,lenB)):
        tmpSum = int(reverseStringA[0])+int(reverseStringB[0])+adder
        sumString = str(tmpSum%10)+sumString
        adder = tmpSum//10
        reverseStringA[0] = ''
        reverseStringB[0] = ''


    return adder, sumString



currentNum = '666'

def getNext(currentNo:str):

    pass



#comment(sj:2021-06-29): check the post number and set a post number condition.

def getNextNum( present: str):
    numSplit = present.split('666',maxsplit=1)
    
    if len(numSplit[1]) > 0:
        if str(10**len(numSplit[1])-1) != numSplit[1]:
            numSplit[1] = ("{0"+str(len(numSplit[1]))+"d}").format(int(numSplit[1])+1)
        else:
            numSplit[1] = ''
            numSplit[0] = str(int(numSplit[0]+'6'*min(3,len(numSplit[1])))+1)+'0'*max(0,len(numSplit[1])-3)
    else:
        numSplit[0] = str(int(numSplit[0])+1)
        if '666' in numSplit[0]:
            numSplit2 = numSplit[0].split('666',maxsplit=1)
            numSplit[0] = numSplit2[0]
            numSplit[1] = numSplit2[1]+'000'
        else:
            count6 = 0
            for i in numSplit[0][::-1]:
                if numSplit[0][i] == '6':
                    count6 +=1
                else:
                    break
            






testStr = '1666'

aa  = testStr.split('666')

print(len(aa))
print(aa[0])
print(aa[1])