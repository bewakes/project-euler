nums = []
for x in range(2, 5*9**5):
    s = sum([int(k)**5 for k in str(x)])
    if s== x:
        print x
        nums.append(x)
print sum(nums)
