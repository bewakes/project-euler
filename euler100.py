from pell import expand_frac_till_den, continued_fraction_sqrt

# THE SOLUTION USES PELL EQUATION
#  upon expanding 1/2 = (n(n-1))/(k(k-1)) we get, (2*(2n-1)**2 - (2*k-1)**2 = 1
#   where N = number of blue, K = total
#  can be written as 2X^2 - 2Y^2 = 1, which is a pell equation
#   so, (X, Y) are the fractional representation of sqrt of 2 where denominator is just > 10**12
#  After finding X, get n as, (X+1)/2, which is th solution

# need to find expansion for sqrt of 2

cf = continued_fraction_sqrt(2)

p, q = expand_frac_till_den(cf, 10**12)

n = int((q+1)/2)
print(n)
