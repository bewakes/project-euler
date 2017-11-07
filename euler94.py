from pell import continued_fraction_sqrt, expand_frac_till_cond


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

    c1 = (2*p-1)/3
    a1 = (c1-1)/2
    c2 = (2*p+1)/3
    a2 = (c2+1)/2
    if 2*a1 == c1-1:
        print('-', c1, c1, 2*a1)
    if 2*a2 == c2+1:
        print('+', c2, c2, 2*a2)
    if c1 > 10**9:
        break
