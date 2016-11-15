import sys

fin = open('matrix.txt', 'r')
sys.stdin = fin
mat = list()
for line in sys.stdin:
	temp = [eval(x) for x in line.split(',')]
	mat.append(temp)

matcp = list(list(y for y in x) for x in mat)
n = len(mat)

startcol = n-2

while startcol>=0:
    for x in range(n):
        lst = []
        # go upwards
        s = 0
        for y in range(x, -1,-1):
            s+= matcp[y][startcol]
            lst.append(s+matcp[y][startcol+1])
        #go downwards
        s = matcp[x][startcol]
        for y in range(x+1, n):
            s+= matcp[y][startcol]
            lst.append(s+matcp[y][startcol+1])
        #print(lst)
        mat[x][startcol] = min(lst)

    matcp = list(list(y for y in x) for x in mat)
    startcol-=1

print(min(matcp[y][0] for y in range(len(mat))))
