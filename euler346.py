def repunits(base, n):
    p= 2
    l = []
    while True:
        nm = base**p -1
        nm = nm/(base-1)
        if nm>n:break
        if nm< n and nm not in l:
            l.append(nm)
        p+=1
    return l 

n = 50
ls=[]
for x in range(2, 50):
    ls.append(repunits(x, 50))
for x in ls:print x

