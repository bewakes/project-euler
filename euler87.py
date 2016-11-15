N = 56
primes = [2]

def genPrimes(n):
    for i in range(3, n+1):
        f = True
        c = 0
        while True:
            if primes[c]*primes[c]>i:break
            if i%primes[c]==0:
                f = False
                break
            c+=1
        if f:
            primes.append(i)

genPrimes(int(N**0.5 +1))
print(len(primes))

alln= [0]*N

sq = [x**2 for x in primes]
cb = [x**3 for x in primes]
fp = [x**4 for x in primes]

ps = set()
for s in sq:
    if s**2 > N:break
    for c in cb:
        if c**3>N:break
        for f in fp:
            sf = s**2+c**3+f**4
            if sf<N:
                alln[sf-1]=1
                #ps.add(sf)
