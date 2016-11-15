def tri(n): return n*(n+1)//2
def quad(n): return n**2
def penta(n): return n*(3*n-1)//2
def hexa(n): return n*(2*n-1)
def hept(n): return n*(5*n-3)//2
def octa(n): return n*(3*n-2)

triangle = [(n,tri(n)) for n in range(1, 5000) if tri(n)>999 and tri(n)<10000]
quadri = [(n,quad(n)) for n in range(1, 5000) if quad(n)>999 and quad(n)<10000]
pentagon = [(n, penta(n)) for n in range(1, 5000) if penta(n)>999 and penta(n)<10000]
hexagon = [(n,hexa(n)) for n in range(1, 5000) if hexa(n)>999 and hexa(n)<10000]
heptagon = [(n, hept(n)) for n in range(1, 5000) if hept(n)>999 and hept(n)<10000]
octagon = [(n, octa(n)) for n in range(1, 5000) if octa(n)>999 and octa(n)<10000]


print(triangle)
print()
print(quadri)
print()
print(pentagon)
print()
print(hexagon)
print()
print(heptagon)
print()
print(octagon)
