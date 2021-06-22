import sys

usrStr = list(sys.stdin.readline().rstrip().upper())

time = 0

for i in usrStr:
    if ord(i) >= ord('A') and ord('C') >= ord(i):
        time +=3
    elif ord(i) >= ord('D') and ord('F') >= ord(i):
        time +=4
    elif ord(i) >= ord('G') and ord('I') >= ord(i):
        time +=5
    elif ord(i) >= ord('J') and ord('L') >= ord(i):
        time +=6
    elif ord(i) >= ord('M') and ord('O') >= ord(i):
        time +=7
    elif ord(i) >= ord('P') and ord('S') >= ord(i):
        time +=8
    elif ord(i) >= ord('T') and ord('V') >= ord(i):
        time +=9
    else:
        time +=10

print(time)