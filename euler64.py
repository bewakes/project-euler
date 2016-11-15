def cntfrac(n):
	A = list()
	a0 = a = int(n**0.5) # a0
	A.append(a)
	cnt = 0
	term = -a
	den = 1
	''' THE ALGORITHM GOES LIKE THIS:
		first find the integer part of the square root, which is a0
		add and subtract a0 from the square root
		take reciprocal of the square root minus a0 and ratonalize it
		repeat the same process, for each ratonalized fraction, subtract and add a0 and divide a0+integer part of numerator by denominator
	'''
	while 1:
		cnt+=1
		den = (n-term**2)/den
		term = term * -1
		term+=a0
		a = term/den
		A.append(a)
		term = -1*(a0-term%den)
		if a==2*a0:
			break
	return A

cnt = 0
for x in range(2, 10001):
	a = int(x**0.5)
	if a*a==x:
		continue
	if len(cntfrac(x))%2==0:
		cnt+=1
print cnt
