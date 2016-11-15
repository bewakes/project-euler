import math
# generating primes upto 1000
primes = [2]
for x in range(3, 1000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)
# end of generating primes upto 1000 ###

def isPrime(n): ## checking whether the number is prime or not
	#print "debugging"
	prime=True
	y=0
	while(primes[y]<=math.sqrt(n)):
		if n%primes[y]==0:
			return False
		y+=1
	return True


max_prod=1
max_num=1
for x in primes:
	for y in primes:
		n=0
		while(isPrime(n*n + n*y + x)):
			n+=1
		if(n>max_num):
			max_num=n
			max_prod=x*y
		n=0
		while((n*n-n*y+x)>=0 and isPrime(n*n - n*y + x)):
			n+=1
		if(n>max_num):
			max_num=n
			max_prod=x*y*(-1)
print max_prod

