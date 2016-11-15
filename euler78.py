def ways(n):return part(n,n)

def part(n, m):
    if n==0: return 1
    if m>n:
        return part(n,n)
    s = 0
    for i in range(1, m+1):
        ans = g_parts[n-i-1][i-1]
        if ans==0:
            ans = part(n-i,i)
            g_parts[n-i-1][i-1] = ans
        s+= ans
    return s
g_parts = []

'''
for x in range(1000):
    g_parts.append([0]*1000)

for x in range(1,1000):
    #print(x,end="")
    c = ways(x)
    if c%1000000==0:
        print(c)
        break
'''
cs = [1]
bs = [1]

def c(n):
    s = 0
    for x in range(1,n+1):
        if(n%x==0):
            s+=x
    return s

def b(n):
    s = c(n)
    cs.append(s)
    for x in range(1, n):
        s+= cs[x-1]*bs[n-x-1]
    return s//n

def gen_penta(n):
    return n*(3*n-1)//2

def gen_qenta(n):
    return n*(3*n+1)//2

g_parts = [0]*1000000
def newpart(n):
    s = 0#g_parts[n-1-1] 
    k = 1
    p = gen_penta(k)
    q = gen_qenta(k)
    while p<=n or q<=n:
        pp = n-p
        qq = n-q
        if pp>=0: np = g_parts[pp]
        else: np = 0
        if qq>=0: nq = g_parts[qq]
        else: nq = 0
        if pp<0 and qq<0:break
        #print((-1)**(k+1),np," <<>>",(-1)**(-k+1),nq,end=" ")
        s=s+int((-1)**(k+1)*np)
        s=s+int((-1)**(k+1)*nq)
        k+=1
        p = gen_penta(k)
        q = gen_qenta(k)
        if(type(p)==float):print('float')
    return int(s)

'''
n = 2
while True:
    bval = b(n)
    bs.append(bval)
    print(n, bval)
    if bval%100==0:
        print(n,bval)
        break
    n+=1
'''
g_parts[0] = 1
g_parts[1] = 1
for x in range(1,100000):
    g_parts[x] = newpart(x)
    if(g_parts[x]%1000000==0):
        print(x, g_parts[x])
        break
    #print(x, g_parts[x])
