from collections import Counter

c = Counter()

less_than = 10**12

base = 2
# while False and base<less_than:
    # pow = 0
    # sm = 0
    # while True:
        # sm += base**pow
        # pow+=1
        # if sm >less_than: break
        # # print(sm)
        # c[sm]+=1
        # #s.add(sm)
    # #l.append(s)
    # base+=1
#     #bases.append(base)

while True:
    pow = 1
    if base > less_than: break
    while True:
        v = (base**pow -1)/(base-1)
        # print(base, v)
        if v == round(v, 0) and v<less_than:
            c[int(v)] +=1
        if v >=less_than:break
        pow+=1
    base+=1


repunits = [k for k, v in c.items() if v>=2]
print(sum(repunits))
print(sorted(repunits))
