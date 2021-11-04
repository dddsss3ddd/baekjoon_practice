import numpy as np

arr = np.array([range(i*10+1,i*10+10) for i in range(1,10)])

def t_comb(a,b):
    c = []
    for i in a:
        for j in b:
            c.append([i,j])
    return c

def get_square_axis_from_axis(x,y):
    axis_x=np.arange(start=3*(x//3),stop=3*(x//3)+3)
    axis_y=np.arange(start=3*(y//3),stop=3*(y//3)+3)
    res = np.array(t_comb(axis_x,axis_y))
    res = np.delete(res,np.where((res[:,0]==x)&(res[:,1]==y)),axis=0)
    return res

q1 = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
q2 = np.empty((3,3),dtype=object)
q3 = [6,4,8,2]
print(q2)

q2[1][1] = [1,2,3]

print(q2)

print(len(q2[1][2]))
