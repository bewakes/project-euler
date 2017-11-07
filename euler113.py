def countInc(num_length, first_digit):
    if num_length==1:
        return 10-first_digit, list(range(first_digit, 10))
    s = 0
    lst = []
    for x in range(first_digit, 10):
        cnt, l = countInc(num_length-1, x)
        print(num_length, first_digit, cnt, l)
        s+=cnt
        lst.extend([x*10+y for y in l])
        print(lst)
    return s, sorted(lst)

def countDec(num_length, first_digit):
    if num_length == 1:
        return first_digit, range(first_digit, -1, -1)
    s = 0
    lst = []
    for x in range(first_digit, 0, -1):
        cnt, l = countDec(num_length-1, x)
        s+=cnt
        lst.extend([x*10+y for y in l])
    return s, sorted(lst)

# cnt, l = countInc(3,1)
# print(l)
# assert False

def get_non_bouncy(digits):
    total = 0
    all = []
    for x in range(1, digits+1):
        t, l = countInc(x, 1)
        tt, ll = countDec(x, 9)
        total+= t + tt
        all.extend(l)
        all.extend(ll)
    total-=(9*digits)+1
    all = list(set(all))
    return len(all), all

print(get_non_bouncy(3))
