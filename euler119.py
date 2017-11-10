import math

def wrong_method():
    lst = []

    n = 4
    c = 0
    while c < 80:
        pow = 2
        while pow* math.log(n,10)+1 <= n+1:
            p = n**pow
            sm = sum([int(x) for x in str(p)])
            if sm == n:
                c+=1
                lst.append(p)
                break
            pow+=1
        n+=1

    lst.sort()
    for i, x in enumerate(lst):
        print(i, x)

    print(lst[29])


def find():
    lst = []
