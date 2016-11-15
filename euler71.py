def gcd(a,b):
    r = a%b
    while r!=0:
        a =b
        b=r
        r=a%b
    return b

def between(ta, tb):
    a = ta[0]+tb[0]
    b = ta[1]+tb[1]
    g = gcd(a,b)
    a = int(a/g)
    b = int(b/g)
    return (a,b)

def dec(a):
 return a[0]/a[1]

d = 1000000
t = (3,7)

t1 = (1,d)
t2 = (d-1, d)
while True:
    print(t1,t2)
    mid = between(t1,t2)
    if mid==t:
        b = between(t1,mid)
        t = b
        if not t[1]<=d:
            print(t1)
            assert False
        while t[1]<=d:
            print(':',b, mid)
            t = between(b,mid)
            if t[1]>=d: 
                print(b)
                assert False
                b = t
            b = t
    if dec(mid)<dec(t):
        t1 = mid
    else:
        t2 = mid
