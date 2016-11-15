import math

primes = [2]
for x in range(3, 100000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)
	if(x%100000==0) : print x



n=9
loop = True
while(loop):
	sq=1
	if not n in primes:
		loop = False
		while(sq*sq <= n/2):
			#print n, n-2*sq*sq
			if (n-2*sq*sq) in primes:
				print n, "=", n-2*sq*sq,"+", 2, "*", sq*sq
				loop=True
				break
			else:
				sq+=1
	n+=2
print n-2