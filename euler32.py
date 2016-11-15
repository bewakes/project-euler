def isPandigital(string):
	if len(string)!=9: return False
	d={1,2,3,4,5,6,7,8,9}
	s=set()
	for x in string:
		s.add(eval(x))
	return d==s

l=list()
count= 0
for x in range(1,9999):
	s=''
	c=(9-len(str(x)))/2 
	for y in range(10**(c-1),10**(c)):
		s=str(x)+str(y)+str(x*y)
		if(len(s)>9):break
		if(len(s)==9):
			if isPandigital(s):
				l.append(x*y)
				print x, y, x*y
sum=0
l.sort()
for x in range(len(l)):
	c= l[x]
	if(not c in l[:x]):
		sum+=c
print sum


