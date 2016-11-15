def gcd(a, b):
    if a<b:m = a
    else: m = b
    for x in range(m,0,-1):
        if a%x==0 and b%x==0:
            return x

def cnt(a, b, mx):
    #print('cnt(',a,',',b,',',mx,')')
    lst = []
    k = 1
    g = gcd(a,b)
    bb = b//g
    aa = a//g
    x = k*bb+a
    y = b-k*aa
    while x<=mx and y>=0:
        lst.append((x,y))
        k+=1
        x = k*bb+a
        y = b-k*aa
    k = 1
    x = a-k*bb
    y = k*aa+b
    while x>=0 and y<=mx:
        lst.append((x,y))
        k+=1
        x = a-k*bb
        y = k*aa+b
    #print(lst)
    #print()
    return len(lst)

def main():
    n = 50
    tot = n**2*3
    for x in range(1, n+1):
        for y in range(1, n+1):
            tot+=cnt(x,y,n)
    print(tot)

main()
