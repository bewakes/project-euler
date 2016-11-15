import math

from primeGen import sieve

# initially let total distinct be 99*99, 2 <= a <= 100 and 2 <= b <= 100
primes_hash = sieve(100)
primes = [x+1 for x in range(len(primes_hash)) if primes_hash[x]==1]

length = 99
total = length*length 

for x in range(2, length+2):
    for y in range(2, length+2):
        if x**y>length+1: break
        for k in range(2,length+2):
            if (x**y)**k <= x**(length+1):
                total-=1
print total

# i don't know why it is givin 1 less value
