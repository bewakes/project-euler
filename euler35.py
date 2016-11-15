from primeGen import sieve

def genCircular(n):
    a = n
    l=[]
    while n!=0:
        r = n%10
        n = n/10
        a = a/10
        a = int(str(r)+str(a))
        l.append(a)
    return l


def circular(n):
	global primes
	if(n/10==0):return True
	l = list()
	ret = list()
	k=n
	while(k!=0):
		if k%2==0: return False
		l.append(k%10)
		k=k/10
	l=l[::-1]
	for x in range(len(l)):
		temp = l[0]
		for y in range(1,len(l)):
			l[y-1]=l[y]
		l[len(l)-1]=temp
		s=0
		for k in l:
			s=s*10+k
		if not s in primes:
			return False
	return True

count = 0
primes_hash = sieve(1000000)
for x in range(2, 1000000):
    if primes_hash[x-1]:
        flag = True
        for k in genCircular(x)[:-1]: # because last element is itself
            if not primes_hash[k-1]:
                flag=False
                break
        if flag==True:
            count+=1
            print x
print count
