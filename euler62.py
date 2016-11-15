import math
def isPerm(a, b):
	aa=str(a)
	bb=str(b)
	if(len(aa)!=len(bb)):return False
	al=list()
	bl=list()
	for x in aa:
		al.append(x)
	for x in bb:
		bl.append(x)
	al.sort()
	bl.sort()
	return al==bl

x=345
while(True):
	cnt=0
	c=x**3
	d=x+1
	while(True):
		e=d**3
		if(isPerm(c,e)):
			#print "permutation"
			cnt+=1
		logc=int(math.log(c,10)+0.1)
		logd=int(math.log(e,10)+0.1)

		if(logc!=logd):

			break
		if(cnt==2):break
		d+=1
	if(cnt==2):
		print x
		break
	x+=1
				