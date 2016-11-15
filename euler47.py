def isPrimes(n): ## checking whether the number is prime or not
	#print "debugging"
	global primes
	if n==1: return False
	return n in primes

def primeFactors(n):
	global primes
	l=set()
	y=0
	loop=True
	while(primes[y]<=math.sqrt(n)):
		if(n%primes[y]==0): l.add(primes[y])
		while(n%primes[y]==0): 
			n=n/primes[y]
		if(n==1): break
		if isPrime(n):
			l.add(n)
			break
		y+=1
	return l

from primeGen import sieve
prime_hash = sieve(2000000)

def isPrime(n):
    return prime_hash[n-1]


import math
# generating primes upto 1000
primes = [2]
for x in range(3, 2000000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)


n=645

count = 0
while (True):
    if isPrime(n+3):
        n+=4
        continue
    if isPrime(n+2):
        n+=3
        continue
    if isPrime(n+1):
        n+=2
        continue
    if isPrime(n):
        n+=1
        continue
        
    a = primeFactors(n)
    b = primeFactors(n+1)
    c = primeFactors(n+2)
    d = primeFactors(n+3)

    flag=True
    if len(a)!=4 or len(b)!=4 or len(c)!=4 or len(d)!=4:
        flag=False
    if a==b or b==c or c==d or a==c or a==d or b==d:
        flag=False
    '''
    if len(a)!=3 or len(b)!=3 or len(c)!=3:
        flag = False
    if a==b or b==c or a==c:
        flag=False
    '''
    if flag:
        print n,n+1,n+2,n+3
        print a, b, c, d
        break
    n+=1

