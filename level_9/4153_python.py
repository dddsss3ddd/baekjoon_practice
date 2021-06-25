#import sys

while True:
    a = map(int,input().split())

    multiList = [i*i for i in a]

    if sum(multiList)==0:
        break
    elif sum(multiList) == max(multiList)*2 :
        print('right')
    else:
        print('wrong')
