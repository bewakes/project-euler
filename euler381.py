from primeGen import sieve
from euclidean import extended_euclidian

# the logic here is that, [WILSON'S THEOREM] (p-1)! mod p = -1.
# from (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)! , we take (p-5)! common to get,
#  (p-5)! X, where, expanding X mod p, we get, 9
#  now, (p-5)! = (p-1)! / [(p-1)(p-2)(p-3)(p-4)]
#  By Wilson's theorem, we can cancel out (p-1)! and (p-1) mod p. thus, we are left over with,
#    X / (p-2)(p-3)(p-4) mod p.
#  The denominator mod p is -24 mod p (obtained after expanding).
#   So, left with X/(-24) mod p. and X = 9 mod p,
# we have, 9/ (-24) = 3/ (-8) mod p
#  Thus, for each prime, we just need to find inverse of -8 mod p and multiply it by 3 and mod p [By using extended euclidean algorithm]
#  DONE!
# BUT TAKES ~63 seconds.. :(

n = 10**8

primes = sieve(n)

s = 0

for i, x in enumerate(primes):
    if i < 4 or not x: continue
    prime = i+1
    inv = int(extended_euclidian(-8, prime)[1])
    #if inv<0: inv = prime - inv
    val = (inv*3)%prime
    s+= val

