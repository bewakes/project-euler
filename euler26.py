def findcycle(n):
    rems = [1]
    rem = 1
    quos=[]
    cnt=0
    while True:
        cnt+=1
        rem=rem*10
        quos.append(rem/n)
        rem = rem%n
        if rem in rems or rem==0:
            break
        rems.append(rem)
    return (rems, quos, cnt)

longest = 2
longest_num = 1
for x in range(2, 1000):
    length = findcycle(x)[2]
    if length>longest_num:
        longest=x
        longest_num=length
print longest
