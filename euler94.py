def main():
    sm = 0
    n = 1
    while True:
        m = (3*n**2+1)**0.5
        m1 = (3*n**2-1)**0.5
        if m==int(m):
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            print(a,b,c,2*(c+a))
            if 2*(c+a)<=10**9:
                sm+=2*(c+a)
        if m1==int(m1):
            m = m1
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            print(a,b,c, 2*(c+a))
            if 2*(c+a)<=10**9:
                sm+=2*(c+a)
                man = 2

        m2 = 2*n + (5*n**2+1)**0.5
        m3 = 2*n + (5*n**2-1)**0.5
        m4 = 2*n - (5*n**2+1)**0.5
        m5 = 2*n - (5*n**2-1)**0.5
        if m2==int(m2):
            m = m2
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            print(a,b,c, 2*(c+b))
            if 2*(c+b)<=10**9:
                sm+=2*(c+b)

        if m3==int(m3):
            m = m3
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            print(a,b,c, 2*(c+b))
            if 2*(c+b)<=10**9:
                sm+=2*(c+b)

        n+=1
        if n>10000:break
    print(sm)

def pell_soln():
    x=2;y=1
    lim = 10**9
    sm = 0
    while True:
        a3 = 2*x-1
        A3 = y*(x-2)
        if a3>lim:break
        if a3>0 and A3>0 and a3%3==0 and A3%3==0:
            a = a3//3
            A = A3//3
            b = (a+1)//2
            print(b, (a**2-b**2)**0.5, a, 3*a+1)
            sm += 3*a+1
        nx = 2*x+y*3
        ny = 2*y+x
        x=nx
        y = ny

        # for b = a-1
        a3 = 2*x+1
        A3 = y*(x+2)
        if a3>lim:break
        if a3>0 and A3>0 and a3%3==0 and A3%3==0:
            a = a3//3
            A = A3//3
            b = (a+1)//2
            print(b, (a**2-b**2)**0.5, a, 3*a-1)
            sm += 3*a-1
        nx = 2*x+y*3
        ny = 2*y+x
        x=nx
        y = ny

    return sm

main()
print(pell_soln())
