def properDivisors(n):
    lst=[]
    for x in range(1,int(n**0.5)+1):
        if n%x==0:
            lst.append(x)
    start = len(lst)-1
    if int(n**0.5)**2 == n:
        start = len(lst)-2
    # find other divisors
    for x in range(start,-1,-1):
        lst.append(n/lst[x])
    return lst[:-1]

abundants_hash = [0]*28123
for x in range(2, 28123):
    if sum(properDivisors(x))>x:
        abundants_hash[x-1]=1

#abundants = [x+1 for x in range(len(abundants_hash)) if abundants_hash[x]==1]
not_abund_sum = []

for x in range(1,28123):
    non_ab_sum = True
    for y in range(1,int(x/2)+1):
        if abundants_hash[y-1] and abundants_hash[x-y-1]:
            non_ab_sum=False
            break
    if non_ab_sum: not_abund_sum.append(x)

print sum(not_abund_sum)
