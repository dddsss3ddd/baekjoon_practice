import math
import sys

usrIn = int(sys.stdin.readline().rstrip())


baseNum = (((8*usrIn-7)**.5)+1)/2//1

print(baseNum)
postBase = baseNum -1
print(postBase)

num1=0
num2=0
print((postBase*(postBase-1)/2+1))
if baseNum%2==0:
    num1 = (usrIn-(postBase*(postBase-1)/2+1))
    num2 = baseNum-(usrIn-(postBase*(postBase-1)/2+1))
else:
    num1 = baseNum-(usrIn-(postBase*(postBase-1)/2+1))
    num2 = (usrIn-(postBase*(postBase-1)/2+1))

print('{}/{}'.format(num1,num2))

#TODO:not done