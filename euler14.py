MAX = 1000000
done = [0] * MAX
lens = [0] * MAX

mx=1
ind=1

def collatz(n):
    global done, mx, ind
    global lens
    cnt = 1
    a = n
    while True:
        if n==1: break
        if n%2==0:
            n=n/2
        else: n=n*3+1

        if n<MAX and  done[n-1] ==1:
            cnt+=lens[n-1]
            break

        cnt+=1
    done[a-1]=1
    lens[a-1] = cnt
    if cnt>mx:
        mx=cnt
        ind = a
    return cnt

for x in range(1, MAX):
    collatz(x)
print mx, ind
