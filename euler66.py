def continuedFrac(n):
	A = list()
	a0= a = int(n**0.5) #a0
	A.append(a)
	cnt = 0
	term =  -a # the term after the square root term
	den = 1 # initial
	''' algorithm detail in problem 64
	'''
	while 1:
		den = (n-term**2)/den
		term  = term * -1
		term+=a0
		a = term/den
		A.append(a)
		term = -1*(a0-term%den)
		if a==2*a0:
			break
	return A

maxx = 1
num = 2
for x in range(2, 1001):
	sqrt = int(x**0.5)
	if sqrt**2 == x:
		continue
	frac = continuedFrac(x)
	if len(frac)%2==0: #  Pr/Qr, P(2r+1) gives the required x
		c = len(frac)-1
		frac+=list(frac[k] for k in range(1, c))
		start = -1
	else:
		start = -2
	#print x, frac
	n = 1
	d = frac[start]
	for k in frac[start-1::-1]:
		n = n+ d*k
		t = d
		d = n
		n = t
	if d>maxx:
		#print maxx
		maxx = d
		num = x
print num, maxx, len(str(maxx))
		
		
