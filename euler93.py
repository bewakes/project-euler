### Thinking of doing this using permutations an reverse polish notation
from itertools import permutations, combinations, product

ops_map = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y
}

def calculate_reverse_polish(l):
    opds = [] # operands
    try:
        for x in l:
            if x in ['+', '-', '*', '/']:
                b = opds.pop()
                a = opds.pop()
                opds.append(ops_map[x](a, float(b)))
            else:
                opds.append(int(x))
        if int(opds[0]) != round(opds[0], 2):
            return None
        return int(opds[0])
    except:
        return None


def valid_perms(l):
    oprs = ['+', '-', '*','/']
    return l[0] not in  oprs and l[-1] in oprs


combs = combinations([1,2,3,4,5,6,7,8,9], 4)

syms = ['+', '-', '*', '/']
opcombs = list(product(syms, repeat=3))
mx = 0
mx_set = []

for i, comb in enumerate(combs):
    l = [0]*(9**4) # this is max, won't be fully used
    for opcomb in opcombs:
        perms = permutations(list(opcomb)+list(comb))
        validperms = filter(valid_perms, perms)
        for p in validperms:
            val = calculate_reverse_polish(p)
            if val and val>0:
                l[val-1] = 1
    cnt = 0
    for x in l:
        if not x:
            break
        cnt+=1
    if cnt > mx:
        mx = cnt
        mx_set = comb
print(mx_set)
