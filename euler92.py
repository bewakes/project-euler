l89 = [0]*(7*81+1) 
l1 = [0]*(7*81+1)

def convergeto(n):
    global l1
    global l89
    b = (sum([int(k)**2 for k in str(n)]))
    while True:
        if b==1 or l1[b-1]:
            return 1
        elif b==89 or l89[b-1]:
            return 89
        b = sum([int(k)**2 for k in str(b)])


for x in range(1, 7*81+1):
    print x, convergeto(x)
    if convergeto(x)==1:
        l1[x-1]=1
    else:
        l89[x-1]=1

cnt = 0
for x in range(1, 10**7):
    s = sum([int(k)**2 for k in str(x)])
    if l89[s-1]:
        cnt+=1
print cnt
