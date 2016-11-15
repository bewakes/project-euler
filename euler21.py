def divisors(n):
    divisors=[]
    if int(n**0.5)**2 == n: divisors.append(int(n**0.5))
    for x in range(int(n**0.5)-1,0,-1):
        if n%x==0:
            divisors.append(x)
            divisors.append(n/x)
    divisors.sort()
    #last number is itself, so remove
    divisors = divisors[:-1]
    return divisors

amicables = []
for x in range(1,10000):
    sn = sum(divisors(x))
    sd = sum(divisors(sn))
    if sd== x and x!=sn:
        amicables.append(x)

print sum(amicables)
