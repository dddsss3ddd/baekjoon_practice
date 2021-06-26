import sys
import math

def pStar(line,dim):
    if dim < 2:
        if line%3 != 1:
            return '***'
        else:
            return '* *'
    else:
        if not (line%(3**dim) < 3**(dim-1)*2 and line%(3**dim) >= 3**(dim-1)):
            return pStar(line,dim-1)*3
        else:
            return pStar(line,dim-1)+(' '*(3**(dim-1)))+pStar(line,dim-1)

usrIn = int(sys.stdin.readline().rstrip())
for i in range(usrIn):
    print(pStar(i,int(math.log(usrIn,3)+0.1)).strip())

# no        id          Q.no    Q.name
# 14051628	asdhugh1	2447	별 찍기 - 10
# copy from someone else code below.
# def sierpinski_carpet(side_length):
#     if side_length == 1:
#         return '*'
#     side_shape = sierpinski_carpet(side_length // 3)
#     whitespace = ' ' * (side_length // 3)
    
#     top_or_bottom = '\n'.join(map(lambda line: line * 3, side_shape.split('\n')))
#     print('len = ',len(top_or_bottom.split('\n')),'tob = ',top_or_bottom)
#     middle = '\n'.join(map(lambda line: line + whitespace + line, side_shape.split('\n')))
#     print('len = ',len(middle.split('\n')),'mid = ',middle)
    
#     return f"{top_or_bottom}\n{middle}\n{top_or_bottom}"

# sierpinski_carpet(int(input()))