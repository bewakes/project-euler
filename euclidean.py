import math

def extended_euclidian(a, p):
    """return gcd, x and y such that a*x+ p*y = gcd"""
    if p == 0:
        d = a
        x = 1
        y = 0
        return d, x, y
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while p > 0:
        q = math.floor(a/p)
        r = a - q*p
        x = x2 - q*x1
        y = y2 - q*y1
        a = p
        p = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x=x2
    y=y2
    return d, x, y

# print(extended_euclidian(-24, 7))
