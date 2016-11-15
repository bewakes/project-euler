size = 21
nPossible = [0]*(size**2)

for x in range(size):
    for y in range(size):
        if x==0 or y==0:
            nPossible[x*size+y] = 1
        else:
            nPossible[x*size+y] = nPossible[x*size+y-1] + nPossible[(x-1)*size+y]
print nPossible[size**2-1]
