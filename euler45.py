# just solve the quadratic equation

def solveQuadratic(a,b,c):
    if b**2 < 4*a*c:return 0
    return (float(-b) + (b**2-4*a*c)**0.5)/float(2*a)

def genTriangle(n):
    return n*(n+1)/2

def genPentagonal(n):
    return n*(3*n-1)/2

def genHexagonal(n):
    return n*(2*n-1)

n = 1
cnt = 0

while cnt<3:
    triangle = n*(n+1)/2
    penta = solveQuadratic(3, -1, -2*triangle)
    hexa = solveQuadratic(2, -1, -triangle)
    if genPentagonal(int(penta))==triangle and genHexagonal(int(hexa))==triangle:
        cnt+=1
        print triangle
    n+=1
