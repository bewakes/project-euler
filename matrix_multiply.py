p1 = [[1,2,2],[2,1,2],[2,2,3]]
p2=[[1,2,2],[-2,-1,-2],[2,2,3]]
p3=[[-1,-2,-2],[2,1,2],[2,2,3]]

def dot(a, b):
    s=0
    for x in range(len(a)):
        s+=a[x]*b[x]
    return s

def matrixprint(a):
    for x in a:
        print x
    print ''

def multiply(a, b):
    if type(a[0])!=list:
        a = [a]
    if type(b[0])!=list:
        b = [b]
    r = len(a) 
    c = len(b[0]) # since we are getting matrices as list of lists, c is the length of 
                  # first element(list) of matrix
    soln = [[0]*c for x in range(r)]
    for x in range(r):
        for y in range(c):
            temp = [m[y] for m in b]## extracting cth element from each row
            s = dot(a[x], temp)
            soln[x][y]=s
    return soln

"""
p = [3,4,5]
primitives = [p]

for x in range(4):
    l = []
    for y in primitives:
        l += [multiply(y,p1)[0], multiply(y,p2)[0], multiply(y,p3)[0]]
    for k in l:
        if not k in primitives:
            primitives.append(k)

for x in primitives:
    s = x[0]+x[1]+x[2]
    if 1000%(x[0]+x[1]+x[2])==0:
        print 1000/s
    #print x , " : ", x[0]+x[1]+x[2]
"""
