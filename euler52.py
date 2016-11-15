def sameDigits(a, b):
    a = [int(x) for x in str(a)]
    a.sort()
    b = [int(x) for x in str(b)]
    b.sort()
    return a==b

a = 10

while True:
    true = False
    for x in range(2, 7):
        if not sameDigits(a, a*x):
            true = True
    if not true:
        print a, a*2, a*3, a*4, a*5, a*6
        break
    a+=1
