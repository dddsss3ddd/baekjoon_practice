import sys

piboList = [[1,0],[0,1]]+[[0,0]]*39

for x in range(2,41):
    piboList[x] = [piboList[x-1][0]+piboList[x-2][0],piboList[x-1][1]+piboList[x-2][1]]

# def fibonacci(n):
#     if n == 0:
#         return 1,0
#     elif n == 1:
#         return 0,1
#     else:
#         a,b = fibonacci(n-1)
#         c,d = fibonacci(n-2)
#         return a+c,b+d

for _ in range(int(sys.stdin.readline().rstrip())):
    usrIn = int(sys.stdin.readline().rstrip())
    # a,b = fibonacci(int(sys.stdin.readline().rstrip()))

    print(piboList[usrIn][0],piboList[usrIn][1])