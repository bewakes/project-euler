from primeGen import sieve
from euclidean import extended_euclidian

n = 10**8

primes = sieve(n)

s = 0

for i, x in enumerate(primes):
    if i < 4 or not x: continue
    prime = i+1
    inv = int(extended_euclidian(-24, prime)[1])
    #if inv<0: inv = prime - inv
    val = (inv*9)%prime
    # print(prime, val)
    s+= val

print(s)
