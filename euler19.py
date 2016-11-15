def isleap(n):
    return ((n%4==0 and n%100!=0) or n%400==0)

monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
leapdays = [x for x in monthdays]
leapdays[1]+=1


initialcnt = 1 #monday

# count first day in 1901
for x in range(12):
    initialcnt+=monthdays[x]


initialcnt = (initialcnt)%7#first day of jan 1 1901

cnt = 0
for x in range(1901,2001):
    days = monthdays
    if(isleap(x)): days = leapdays
    for y in range(12):
        if((initialcnt)%7==0):cnt+=1
        initialcnt+=days[y]
    
print cnt

