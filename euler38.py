def isPandigital(string):
	if len(string)!=9: return False
	d={1,2,3,4,5,6,7,8,9}
	s=set()
	for x in string:
		s.add(eval(x))
	return d==s

l = list()
for n in range(2,10):
	c=9/n
	length=0
	s=''
	flag = True
	for x in range(10**(c-1), 10**c):
		s=''
		for z in range(1,n+1):
			s+=str(x*z)
			if(len(s)>9):
				flag=False
				break
		if flag==False:
			break
		if len(s)==9:
			if isPandigital(s):
				print s
				l.append(int(s))
print "**" , max(l)
