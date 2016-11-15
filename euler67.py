rows = 100

f = open("triangles.txt", 'r')
triangle = f.read()
triangle=triangle.split('\n')
for x in range(len(triangle)):
    triangle[x] = triangle[x].split()
    triangle[x] = [int(k) for k in triangle[x]]

triangle=triangle[:-1]
print triangle

for x in range(rows-2,-1,-1):
    for y in range(x+1):
        triangle[x][y] += max([triangle[x+1][y], triangle[x+1][y+1]])

for x in triangle:
    print x
