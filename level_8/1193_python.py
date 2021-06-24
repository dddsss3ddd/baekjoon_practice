import math
import sys

usrIn = int(sys.stdin.readline().rstrip())

baseNum = (((usrIn*8-7)**0.5)+1)//2
countNo = (baseNum**2-baseNum+2)//2

num1=0
num2=0

num1 = int(baseNum - (usrIn-countNo))
num2 = int(1 + (usrIn-countNo))

if baseNum%2 == 1:
    print('{}/{}'.format(num1,num2))    
else:
    print('{}/{}'.format(num2,num1))