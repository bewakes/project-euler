def find_gcd(a, b):
    """ not used """
    if b == 0:
        return a
    return find_gcd(b, a%b)

def continued_fraction_sqrt(n):#, depth=10):
    """generator for continued fraction of sqrt of n"""
    # frac = [] # list of elements
    sqrt = int(n**0.5)
    # if sqrt == (n**0.5):
    yield sqrt
    # frac = [sqrt]
    a = - sqrt
    num = 1
    q = sqrt
    while  True:
        den = n - a**2
        den = den/num
        a = a*-1
        q = int((sqrt + a)/den)
        r =  a - (q * den)
        yield q
        # frac.append(q)
        a = r
        num = den
        # depth-=1
    # return frac

def expand_frac_rev(frac_list):
    """not used"""
    rev = reversed(frac_list)
    a = next(rev)
    n = 1
    d = a
    for x in rev:
        s = x*d+n
        n = d
        d = s
    return (d, n)

def expand_frac_till_den(frac_gen, den_limit):
    a0 = next(frac_gen)
    a1 = next(frac_gen)
    pp = a0
    p = a1*a0+1
    qq = 1
    q = a1
    while q <= den_limit:
        tp = p
        tq = q
        a = next(frac_gen)
        p = a*p + pp
        q = a*q + qq
        pp = tp
        qq = tq
    return p, q

def expand_frac_till_cond(frac_gen, cond):
    """cond is function that takes p, q"""
    a0 = next(frac_gen)
    a1 = next(frac_gen)
    pp = a0
    p = a1*a0+1
    qq = 1
    q = a1
    while cond(p,q):
        print('...', p, q)
        tp = p
        tq = q
        a = next(frac_gen)
        p = a*p + pp
        q = a*q + qq
        pp = tp
        qq = tq

    return p, q

if __name__== '__main__':

    n = 3
    cf = continued_fraction_sqrt(n)
    for i, x in enumerate(cf):
        print(x)
        if i>10:break

