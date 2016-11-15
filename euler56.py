mxm = 1
for x in range(2, 100):
    for y in range(2, 100):
        b = x**y
        sm = sum([int(i) for i in str(b)])
        if sm>mxm:
            mxm = sm
print mxm 
