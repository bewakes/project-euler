muls=list()

import math
primes = [2]
for x in range(3, 100):
	y=0
	prime = True
	while(primes[y]<=math.sqrt(x)):
		if x%primes[y]==0:
			prime=False
			break
		y+=1
	if prime==True: primes.append(x)

def distinct(n):
	a=n%10
	b=n/100
	c=(n/10)%10
	return a!=b and a!=c and b!=c

l=[]
for x in range(50, 500):
    temp = 2*x
    if distinct(temp):l.append(temp)
muls.append(l)


a = 1
while(primes[a]<=17):
	b=1
	lst=list()
	y=primes[a]*b
	while(y<1000):
		if(y>10 and distinct(y)):
			lst.append(y)
		b+=1
		y=primes[a]*b
	muls.append(lst)
	a+=1

print muls

def check(lst):
    if len(lst)!=7:
        return False
    a = set([0,1,2,3,4,5,6,7,8,9])
    b = set()
    for x in lst:
        for k in str(x):
            b.add(int(k))
    return (len(a)==len(b)+1, (a-b).pop())

solns = list()
for  x in muls[0]:
    temp=list()
    for y in muls[1]:
        if(x%100==y/10):
            for m in muls[2]:
                if y%100==m/10:
                    for n in muls[3]:
                        if m%100==n/10:
                            for p in muls[4]:
                                if n%100==p/10:
                                    for q in muls[5]:
                                        if p%100==q/10:
                                            for r in muls[6]:
                                                if q%100==r/10:
                                                    temp=[x,y,m,n,p,q,r]
                                                    #print temp
                                                    res = check(temp)
                                                    if res[0]:
                                                        solns.append((temp, res[1]))

print solns
summ= 0
for each in solns:
    s=''
    print each[0]
    s+=str(each[0][0])
    for x in range(1,len(each[0])):
        s+=str(each[0][x])[::-1][0]
    s=str(each[1])+s
    print s
    summ+=int(s)
print summ

