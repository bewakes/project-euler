primes = [2]

def prime_gen(n):
	for x in range(3,n):
		prime=True
		index=0
		while(primes[index]<=x**0.5):
			if x%primes[index]==0:
				prime = False
				break
			index+=1
		if prime:
			primes.append(x)


def is_perm(a,b):
	lista = [x for x in str(a)]
	listb = [x for x in str(b)]
	for x in lista:
		if x not in listb:
			return False
		else:
			listb.remove(x)
	if len(listb) != 0:
		return False
	return True


def eulerphi(n):
	global primes
	index = 0
	phi = n
	flag = True
	while primes[index]<=n**0.5:
		if n%primes[index]==0:
			flag = False
			c = primes[index]
			phi/=c
			phi*=(c-1)
		index+=1
	if flag:
		phi-=1
	return phi


prime_gen(3200)

minphi = float(21)/12
soln =21
for x in range(2,1000000):
	phi = eulerphi(x)  
	if float(x)/phi < minphi:
		if is_perm(x, phi):
			minphi=float(x)/phi
			soln = x
print minphi
