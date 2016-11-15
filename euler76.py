def penta(n):
    return n*(3*n-1)//2

def ways(n):
    num = 1
    pent = penta(num)
    s= 0
    while pent<=n:
        s+= (-1)**(num-1) * ways(pent) 
        num+=1
        pent = penta(num)
    return s

g_parts = []


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

def main():
    n = 6 
    for x in range(100):
        g_parts.append([0]*100)

    print(part(n,n))

main()
