import sys

print(len(list(sys.stdin.readline().rstrip().replace('c=', '0').replace('c-', '0').replace('dz=', '0').replace('d-', '0').replace('lj', '0').replace('nj', '0').replace('s=', '0').replace('z=', '0'))))


# c=input().count;print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))

# print(list(map(c,['-','=','nj','lj','dz='])))