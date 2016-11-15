
def isPandigital(string):
	if len(string)!=7: return False
	d={1,2,3,4,5,6,7}
	s=set()
	for x in string:
		s.add(eval(x))
	return d==s


# NEW METHOD
from primeGen import sieve

primes_hash=sieve(8000000)
for x in range(8000000-1,2,-1):
    if primes_hash[x-1] and isPandigital(str(x)):
        print x
        break

# OLD METHOD
# a slow program, but gave the answer
import math

primes = [2]
for x in range(3, 8000000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)

for x in range(len(primes)-1, 0,-1):
	if len(str(primes[x]))<7: break
	if isPandigital(str(primes[x])): print primes[x]
