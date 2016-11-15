MAX = 51
nums = [0]*MAX

primes = [2] # number of primes upto MAX

def genPrimes(N):
    for x in range(3,N+1):
        flag = True
        for y in range(0,len(primes)):
            if primes[y]**2>x:break
            if x%primes[y]==0:
                flag=False
                break
        if flag:
            primes.append(x)

def getPrimeFactors(n): # returns a list giving powers of generated primes
    l = [0]*len(primes)
    for i,x in enumerate(primes):
        if n%x==0:
            cnt = 0
            while n%x==0 and n>1:
                n = n//x
                cnt+=1
            l[i] = cnt
    return l

def multiply(a,b):
    A = getPrimeFactors(a)
    B = getPrimeFactors(b)
    return [x+y for x,y in zip(A,B)]

def divide(a,b):
    A = getPrimeFactors(a)
    B = getPrimeFactors(b)
    return [x-y for x,y in zip(A,B)]

def multiplyList(l):
    f = [getPrimeFactors(x) for x in l]
    t = []
    if len(f)==0:
        return [0]*len(primes)
    for x in range(len(f[0])):
        s = 0
        for y in f:
            s+=y[x]
        t.append(s)
    return t

def numberFrmList(l):
    a = 1
    for x,y in zip(l,primes):
        a*=y**x
    return a

def dividefactors(a,b):
    return [x-y for x,y in zip(a,b)]
def multiplyfactors(a,b):
    return [x+y for x,y in zip(a,b)]

def combination(n, r):
    if r>n-r:
        a = r
    else:
        a = n-r
    numerator = list(range(a+1,n+1))
    denominator = list(range(1,n-a+1))
    n = multiplyList(numerator)
    d = multiplyList(denominator)
    return dividefactors(n,d)


def main():
    done = []
    genPrimes(MAX)

    for x in range(MAX):
        for y in range(x//2+1):
            l = combination(x,y)
            #print(x,y,l,numberFrmList(l))
            if not l in done:
                done.append(l)
    print()
    cnt=0
    sm = 0
    for x in done:
        flag = True
        for k in range(len(primes)):
            if x[k]>=2:
                flag = False
                break
        if flag:
            sm+=numberFrmList(x)
            print(x, numberFrmList(x))
            cnt+=1
    print(sm)

if __name__=="__main__":
    main()

