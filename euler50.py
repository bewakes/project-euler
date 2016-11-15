from primeGen import sieve

primes_hash = sieve(1000000)
primes = [x+1 for x in range(len(primes_hash)) if primes_hash[x]==1]

max_len = 1
prime = 2

for x in range(len(primes)):
    smm = primes[x]
    cnt = x+1
    if primes[x]+primes[x+1] > 1000000:
        break
    while smm<1000000:
        smm+=primes[cnt]
        if smm>1000000:
            break
        if primes_hash[smm-1]:
            length = cnt-x+1
            if length>max_len:
                max_len=length
                prime = smm
        cnt+=1
print max_len, prime

