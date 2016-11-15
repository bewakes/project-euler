from primeGen import sieve

prime_hash = sieve(1000000)

def truncate_right(n):
    l=[n]
    while n!=0:
        l.append(n/10)
        n/=10
    l.pop()
    return l

def truncate_left(n):
    l=[]
    n= str(n)
    for x in range(len(n)):
        l.append(int(n[x:len(n)]))
    return l

soln=[]
for x in range(10,1000000):
    if prime_hash[x-1]:
        flag= True
        temp = x
        for k in truncate_right(x):
            if not prime_hash[k-1]:
                flag=False
                break
        if flag:
            for k in truncate_left(x):
                if not prime_hash[k-1]:
                    flag=False
                    break
        if flag:
            soln.append(x)

print sum(soln)
print "slow method.."

import math
# generating primes upto 1000
primes = [2]
for x in range(3, 1000000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)

def isPrime(n): ## checking whether the number is prime or not
	#print "debugging"
	if n==1: return False
	prime=True
	y=0
	while(primes[y]<=math.sqrt(n)):
		if n%primes[y]==0:
			return False
		y+=1
	return True	

def truncable(n):
	if n<=10:
		return False
	k = n
	#removing from right
	while(n>=10):
		if not isPrime(n/10): return False
		n=n/10
	# removing from left
	d=10000
	while(k>10):
		if not isPrime(k%d): return False
		k=k%d
		d/=10
	return True

primes2dgt = primes[4:]

cnt =0
for x in primes2dgt:
	if truncable(x): 
		cnt+=x
		
print cnt
