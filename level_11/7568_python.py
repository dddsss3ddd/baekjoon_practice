import sys

<<<<<<< HEAD
usrIn =  sys.stdin.readline().rstrip()
national = int(usrIn)
count = len(usrIn)

min = 0
for ii in range(national-9*(count-1)-int(usrIn[0]),national):
     if national == ii + sum(map(int,[char for char in (str(ii))])):
        min = ii
        break

print(min)

# usrCount = int(sys.stdin.readline().rstrip())

#        #w,h,r
# # res = [0,0,1]*usrCount
# res = []
# for i in range(usrCount):    
#     # res.append(list(map(int,sys.stdin.readline().rstrip().split()+['1'])))
#     res.append(list(map(int,sys.stdin.readline().rstrip().split()))+[1])

#     for j in range(0,i):
#         if res[j][0] > res[i][0] and res[j][1] > res[i][1]:
#             res[i][2] +=1
#         elif res[j][0] < res[i][0] and res[j][1] < res[i][1]:
#             res[j][2] +=1
# for i in range(usrCount):
#     # print(res[i][0],res[i][1],res[i][2])
#     print(res[i][2],end=' ')
# print()
