x = 7830457
y = x/6	#multiply by 64
p = y*6
x = x-p
n = 28433
k = 2**x
a = y
while a>0:
	k = (k*64)%(10**10)
	a-=1
k = (k*n)%(10**10)
k+=1
print k
