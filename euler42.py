# considering maximum letters in a word is 20, the max possible sum is 20*26

# so create a hash of numbers upto 20*26

hashed=[0]*(520)
cnt=1
while True:
    triangle = cnt*(cnt+1)/2
    if triangle >= 520:
        break
    hashed[triangle-1] = 1
    cnt+=1

f = open('words.txt', 'r')
words = f.read().split(',')
words = [x.strip('\n').strip('"') for x in words]

cnt=0
for word in words:
    s=sum([ord(ch) - ord('A')+1 for ch in word])
    if hashed[s-1]:
        cnt+=1
        print cnt
