import math
primes = [2]
for x in range(3, 10000):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)


primes4digit =[]
for x in range(len(primes)-1, 1, -1):
	if primes[x]<1000: break
	primes4digit.append(primes[x])

primes4digit.sort()

def isPermut(a, b):
	sa = list()
	sb = list()
	while(a!=0):
		sa.append(a%10)
		a/=10
	while(b!=0):
		sb.append(b%10)
		b/=10
	sa.sort()
	sb.sort()
	for x in range(len(sa)):
		if(sa[x]!=sb[x]): return False
	return True

permuts=list()
x=0
check = [0]*len(primes4digit)

for x in range(len(primes4digit)):
	temp = list()
	for y in range(x, len(primes4digit)):
		if check[y]!=1:			
			if isPermut(primes4digit[x],primes4digit[y]):
				temp.append(primes4digit[y])
				check[y]=1
	if not len(temp)==0:permuts.append(temp)
print permuts

for x in permuts:
	if len(x)<3: 
		permuts.remove(x)
	else:
		for y in x:
			if not y in primes4digit:
				x.remove(y)

finalpermuts=list()

for x in permuts:
	if len(x)>=3:
		finalpermuts.append(x)


for x in finalpermuts:
	for y in range(len(x)):
		for z in range(y+2, len(x)):
			if (x[y]+x[z])/2 in x:
				print x[y], x[z], (x[y]+x[z])/2

