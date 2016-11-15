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


def count(ta, tb, d):
    global s
    mid= between(ta, tb)
    if mid[1]<=d:
        s+=1
    else: return
    count(ta,mid,d)
    count(mid,tb,d)

ta=(1,3)
tb=(1,2)
d = 12000
s = 0
current= [ta,tb]
while len(current)!=0:
    tb = current.pop()
    ta = current.pop()
    mid = between(ta,tb)
    if mid[1] <=d:
        s+=1
        current.append(ta)
        current.append(mid)
        current.append(mid)
        current.append(tb)
print(s)
