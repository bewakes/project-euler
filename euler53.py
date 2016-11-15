def fact(n):
	a=1
	for x in range(1, n+1):
		a*=x
	return a

def comb(n, r):
	return fact(n)/(fact(r)*fact(n-r))

total=0
for x in range(23, 101):
	for y in range(1, x):
		if(comb(x, y)>1000000):
			total= total + x-2*y+1
			break

print total