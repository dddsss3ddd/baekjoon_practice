import sys


preStr = '0'
postStr = ''

#comment(sj:2021-06-29): check the post number and set a post number condition.

def getNextNum():
    middle = '666'
    preNum = int(preStr)
    if preNum%10 != 5 and preNum%10 != 6:
        preStr = str(int(preStr)+1)
    else:
        if preNum%10 == 5:
            preNum += 1
            middle = '66'
            postStr = '0'*len(postStr)
        elif preNum%10 == 6:
            if int(postStr) != (10**(len(str(postStr))-1)):
                postStr = str(int(postStr)+1)
            else:
                

            middle = '66'