# function is_bouncy is better than check_bouncy
bouncy = 0

def check_bouncy(n):
    inc=False
    dec=False
    n = str(n)
    # prev = n%10
    for i in range(len(n)-1):
        if n[i] == n[i+1]:continue
        if n[i] > n[i+1]:
            dec=True
        else: inc=True
        if dec and inc:return True
    return False

def is_bouncy(n):
    inc=False
    dec=False
    prev = n%10
    n //= 10
    while n>0:
        curr = n%10
        if prev==curr:
            n //= 10
            continue
        elif prev>curr:inc=True
        else:dec=True
        if inc and dec:
            return True
        prev=curr
        n//=10
    return False

print(is_bouncy(66420))

percent = 99

n = 100
while True:
    if is_bouncy(n):
        bouncy+=1
    if 100*bouncy == 99*n:
        print(n)
        break
    n+=1
