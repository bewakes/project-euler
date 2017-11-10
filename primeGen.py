import math

def primeGen(n):
        l = [2]
        if(n<3):
                return l
        for x in range(3, n):
                y=0
                prime = True
                while(l[y]<=math.sqrt(x)):
                        if x%l[y]==0:
                                prime=False
                                break
                        y+=1
                if prime==True: 
                        l.append(x)
        return l


def sieve(n):
    primes = [1]*(n)
    primes[0] = 0
    for x in range(2,int(n**float(1)/2)+1):
        cnt=x+x
        if(primes[x-1]!=0):
            while 1:
                if cnt>n:
                    break
                primes[cnt-1]=0
                cnt+=x
    return primes
