# looking at the diagonals, we find the following equations
# 4x^2 - 4x + 1
# 4x^2 - 6x + 3
# 4x^2 - 8x + 5
# 4x^2 - 10x + 7

# here, 25 is the third sequence, 9 is second sequence and 1 is first
# so, 5=2*3-1, 3=2*2-1, 1=2*1-1
# 1001 = 2*n-1 ==> n = 501


diag_sum = 0
for x in range(2,502): # start from second iteration, add 1 at last
    diag_sum += 4*x**2 - 4*x + 1
    diag_sum += 4*x**2 - 6*x + 3
    diag_sum += 4*x**2 - 8*x + 5
    diag_sum += 4*x**2 - 10*x + 7

diag_sum+=1
print diag_sum
