import math

def fact(n):
    p = 1
    for x in range(1,n+1):
        p*=x
    return p

l = []

for x in range(3,fact(9)*9):
    s = str(x)
    s = [fact(int(k)) for k in s]
    if sum(s)==x:
        print x
        l.append(x)
print l
