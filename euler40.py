import math
f=1
count=0
l = list()
for x in range(1,1000005):
	c=int(math.log(x,10)+0.000000001)+1
	count+=c
	#print count, x
	if count>=f and count-c<f:
		k=count
		t=x
		if count==f:
			l.append(x%10)
		else:
			while(k!=f):
				t/=10
				#print t
				k-=1
			l.append((t%10))
		f*=10
		if(f>1000000):break


print l
