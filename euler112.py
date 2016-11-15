# wrong!!
bouncy = 0

def check_bouncy(n):
    inc = 0
    dec = 0
    a = n%10
    n = n//10
    b = n%10
    n = n//10
    while n!=0:
        if a>b:
            dec = 1
        if a<b:
            inc = 1
        if dec and inc:
            return True
        a = b
        b = n%10
        n = n//10
    return False

# number of bouncy for n digits
n = 2
incr = 0
decr = 0
total = 10**n-1

for s in range(1,10):
    for e in range(1,10):
        incr+=(int(e-s+1)**n-2)
decr = incr
decr += 9*(n-1)

bouncy = total - incr-decr
print(bouncy, total)
