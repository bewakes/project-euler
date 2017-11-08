### Thinking of doing this using permutations an reverse polish notation
from itertools import permutations, combinations

def valid_perms(l):
    oprs = ['+', '-', '*','/']
    return l[0] in  oprs and l[-1] not in oprs


perms = permutations(['+', '-', '*', '/', 'a', 'b', 'c', 'd'])
perms = list(filter(valid_perms, perms))
print(len(perms) * 42*3)

combs = combinations([1,2,3,4,5,6,7,8,9], 4)
