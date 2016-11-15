#from primeGen import *

num = 0
def sigma(n):	# sigma returns the sum of proper divisors of n
	s = 0
	for x in range(2,int(n**0.5+1)):
		if n%x==0:
			s+=x
			s+=(n//x)
	c = int(n**0.5)
	if c*c==n:
		s-=c
	return s+1

chain_len = [-1]*1000000
sigmas = [0]*1000000
sigmalist = []

def chain(n):
    global num,sigmas,chain_len
    l = []
    cnt = 0
    if sigmas[n-1]==0:
        num+=1
        print('calculating sigma ', num, ',    ', n)
        sigmas[n-1] = sigma(n)
    sig = sigmas[n-1]
    sigmalist.append(n)
    while sig!=n or sig==0:
        if sig>1000000 or sig==0:return 0
        if sig in l: return 0
        l.append(sig)
        cnt+=1 
        if sigmas[sig-1]==0:
            sigmas[sig-1] = sigma(sig)
        sig = sigmas[sig-1]
    return cnt 

def main():
    max_len = 0
    n = 0
    for x in range(1,1000000):
        l = chain(x)
        chain_len[x-1] = l
        if l>max_len:
            print(n, max_len)
            max_len=l
            n = x
    print(n, max_len)
main()
