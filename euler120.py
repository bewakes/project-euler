s = 0
for a in range(3, 1001):
    n = int(a/2.)
    if a%2 == 0: n-=1
    s += (2*n*a)%(a*a)
print(s)
