from pell import continued_fraction_sqrt, expand_frac_till_cond

def is_triplet(c, a):
    c = int(c)
    a = int(a)
    b = int((c**2 - a**2)**0.5)
    return a**2 + b**2 == c**2


def soln_by_pell():
    """This one uses pell equation, but is kind of hackish"""
    cf = continued_fraction_sqrt(3)
    sm = 0

    a0 = next(cf)
    a1 = next(cf)
    pp = a0
    p = a1*a0+1
    qq = 1
    q = a1
    while True:
        tp = p
        tq = q
        a = next(cf)
        p = a*p + pp
        q = a*q + qq
        pp = tp
        qq = tq

        c1 = int((2*p-1)/3)
        a1 = int((c1-1)/2)
        c2 = int((2*p+1)/3)
        a2 = int((c2+1)/2)
        if 2*a1 == c1-1 and is_triplet(c1, a1):
            print('-', c1, c1, 2*a1)
            if 2*c1+2*a1 <= 10**9:
                sm += (2*c1+ 2*a1)
        if 2*a2 == c2+1 and is_triplet(c2, a2):
            if 2*c2+2*a2 <= 10**9:
                sm += (2*c2+ 2*a2)
            print('+', c2, c2, 2*a2)
        if c1 > 10**9:
            break
    print(sm)


def better_solution():
    """This one is clever, which I obtained from PE thread
    Uses the fact that among the three transformations, namely
    (-x+2y+2z,-2x+y+2z,-2x+2y+3z), (x-2y+2z,2x-y+2z,2x-2y+3z) and 
    (x+2y+2z,2x+y+2z,2x+2y+3z),
    The third one is useless to generate x,y,z such that x=(z+-1)/2 or y=(z+-1)/2
    Considiring we have basic solution where x=(z+1)/2, we can use transformation 1
    to get another solution of the form y=(z-1)/2.
    And from solution of form x=(z+1)/2, we use tx 2 to get solution of form z=(z+1)/2
    """
    def tx1(x,y,z):
        return (-x+2*y+2*z,-2*x+y+2*z,-2*x+2*y+3*z)
    def tx2(x,y,z):
        return (x-2*y+2*z,2*x-y+2*z,2*x-2*y+3*z)

    x,y,z = 3,4,5 # of the form x=(z+1)/2
    sm = 2*3 + 2*5
    while True:
        # if flag:
            # print('tx2')
            # y,x,z = tx2(x,y,z)
        # else:
            # print('tx1')
        if True:
            # seems that we can just use tx1 and change values of x and y alternately
            y,x,z = tx1(x,y,z)
        # print(x,y,z)
        # flag = not flag
        if 2*x + 2*z > 10**9:
            break
        sm+=2*x+2*z
    print("The sum is:", sm)

better_solution()
