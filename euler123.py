import math

# I don't know why the answer should be incremented by 1 in case of 10**10 but works for 10**9
# this could be made a little bit efficient(reducing loops) but I'm lazy


# the logic is, we need not calculate large powers, for even n, rem is always 2
#  but for odd ones, the remainder is 2 * n * Pn
# The above result can be derived by binomial expansion of 
#  (a+b)^n + (a-b)^n and the fact that remainder when Pn^2 divided Pn^k is zero when k>=2

def primeGen(n):
    l = [2]
    if(n<=1):
        return l
    x = 3
    cnt=2
    while cnt <= n:
        y=0
        prime = True
        while(l[y]<=math.sqrt(x)):
            if x%l[y]==0:
                prime=False
                break
            y+=1
        if prime==True: 
            cnt+=1
            l.append(x)
        x+=1
    return l

ps = primeGen(100000)

N = 10**10

for i, x in enumerate(ps):
    if 2*(i+1)*x % x **2 >= N:
        print(i+1)
        break
