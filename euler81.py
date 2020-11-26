import sys
fin = open('matrix.txt', 'r')
sys.stdin = fin
mat = list()

for line in sys.stdin:
    temp = [int(x) for x in line.split(',')]
    mat.append(temp)
    print(temp)

print(len(mat))

a = n = 79
while a >= 0:
    if a == n:        # if right bottom corner
        mat[a][a] += 0
        for x in range(a-1, -1, -1):
            mat[x][a] += mat[x+1][a]
            mat[a][x] += mat[a][x+1]
    else:
        mat[a][a] += min(mat[a][a+1], mat[a+1][a])

        for x in range(a-1, -1, -1):      # in x direction
            mat[x][a] += min(mat[x+1][a], mat[x][a+1])

        for y in range(a-1, -1, -1):    # in y direction
            mat[a][y] += min(mat[a+1][y], mat[a][y+1])
    a -= 1

print(mat[0][0])
