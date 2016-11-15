f = open('prime_powers', 'r')
cnt = 0
s = [0]*50000000
for line in f:
    num = line.split('>>')[1].strip()
    num = int(num)
    cnt+=1
    if num < 50000000:
        s[num-1] = 1
print(cnt)
print(sum(s))

