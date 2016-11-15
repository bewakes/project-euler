print "NEW METHOD"
import matrix_multiply as mat

p1 = [[1,2,2],[2,1,2],[2,2,3]]
p2=[[1,2,2],[-2,-1,-2],[2,2,3]]
p3=[[-1,-2,-2],[2,1,2],[2,2,3]]

# generate primitive triplets
p=[3,4,5]
primitives=[p]
curr_len = 1
prev_len = 0
cnt=0 # to check if sum >1000 or not, if any 3 consecutive have
#       sum > 1000, we exit loop
while True:
    l=[]
    greater1000=True
    for y in primitives[prev_len:curr_len]:
        a=mat.multiply(y,p1)[0]
        b=mat.multiply(y,p2)[0]
        c=mat.multiply(y,p3)[0]
        if sum(a) < 1000 or sum(b)<1000 or sum(c)<1000:
            greater1000=False
        l += [a, b, c]
    for k in l:
        if sum(k)<1000:
            if not k in primitives:
                primitives.append(k)
    prev_len=curr_len
    curr_len=len(primitives)
    if greater1000:
        break

# now we have primitives
nonprimitives=[]
for x in primitives:
    nonprimitives.append(x)
    cnt=2
    while True:
        temp = [a*cnt for a in x]
        if sum(temp)>1000:
            break
        nonprimitives.append(temp)
        cnt+=1

hashed=[0]*1000
for x in nonprimitives:
    hashed[sum(x)-1]+=1
print hashed
print hashed.index(max(hashed))

print "OLD METHOD"
triplets = list()

def hcf(a, b):
	if(a%b==0):return b
	return hcf(b, a%b)

m = 1
while((m+1)**2 - m**2 <=1000):
	n=m+1
	while(n**2-m**2 <=1000):
		if(hcf(m,n)==1):
			temp=set()
			p=n**2-m**2
			b=2*m*n
			h=n**2+m**2
			if((n-m)%2==0):
				p=p/2
				b=b/2
				h=h/2
			if(p+b+h>1000): break
			temp.add(p)
			temp.add(b)
			temp.add(h)
		if not temp in triplets:triplets.append(temp)
		n+=1
	m+=1
		
no = list()
for x in range(2,1001, 2): no.append(x)

soln = list()
for x in no:
	count=0
	for y in triplets:
		s=0
		for z in y:
			s+=z
		if(x%s==0):count+=1
	soln.append(count)

c = max(soln)
d = soln.index(c)
print no[d]
