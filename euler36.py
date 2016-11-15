def dec_to_binary(n):
    binstr=''
    while n!=0:
        binstr=str(n&1)+binstr
        n=n>>1
    return binstr

solution = []
for x in range(1,1000000):
    if x%10!=0:#we don't need leading zeros
        if str(x) == str(x)[::-1]:
            if dec_to_binary(x)==dec_to_binary(x)[::-1]:
                solution.append(x)
print sum(solution)
