primes = [2]
n = 100

MAX = 10**9

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

primepowers = []
cnt = 1

def find(i, j, product):
    global cnt
    if product > MAX:return
    if i+1>=len(primepowers):return
    for x in range(i+1, len(primepowers)):
        for k in range(len(primepowers[x])):
            prod = product * primes[x]**primepowers[x][k]
            if prod>MAX:break
            #print(product, primes[x]**primepowers[x][k], prod)
            cnt+=1
            find(x,k,prod)

def main():
    global cnt
    genPrimes(n)

    for x in primes:
        y = 1
        while x**y<=MAX:
            y+=1
        t = list(range(1,y))
        primepowers.append(t)
    #print(primepowers)
    for i, x in enumerate(primepowers):
        print(i)
        for j, y in enumerate(x):
                if primes[i]**x[j]>MAX:continue
                #print(primes[i]**x[j])
                cnt+=1
                find(i,j,primes[i]**x[j])
    print(cnt)

if __name__=="__main__":
    main()
