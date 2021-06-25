import sys
import math

T = sys.stdin.readline().rstrip().split()

upNumber = ''
if len(T[0]) > len(T[1]):
    upNumber = T[0][:len(T[0])-len(T[1])]
    T[0] = T[0][len(T[0])-len(T[1]):]
elif len(T[0]) < len(T[1]):
    upNumber = T[1][:len(T[1])-len(T[0])]
    T[1] = T[1][len(T[1])-len(T[0]):]
res = ''
adder = 0
for i in range(len(T[1])-1,-1,-1):
    res = str((int(T[0][i])+int(T[1][i])+adder)%10) + res
    adder = (int(T[0][i])+int(T[1][i])+adder)//10

for i in range(len(upNumber)-1,-1,-1):
    if adder == 0:
        res = upNumber[0:i+1] + res
        break
    res = str((adder+int(upNumber[i]))%10) + res
    adder = (adder+int(upNumber[i]))//10

if adder > 0:
    res = '1'+res

print(res)




# if len(T[0]) != len(T[1]):
#     if len(T[0]) > len(T[1]):
#         T[1] = "0"*(len(T[0])-len(T[1])+9-len(T[0])%9)+T[1]
#     else:
#         T[0] = "0"*(len(T[1])-len(T[0])+9-len(T[1])%9)+T[0]

# adder = 0



# numA = [T[0][i:i+9] for i in range()

# res = [0]*(len(numA)+1)
# for i in range(len(numA)):
#     sum = numA[i]+numB[i]

    