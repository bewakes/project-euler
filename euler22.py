names = file("names.txt",'r')
names = names.read()
names = names.split(',')
names = [x.strip('\n').strip('"') for x in names]
names.sort()

cnt = 0
total = 0


for name in names:
    cnt+=1
    s = 0
    for x in name:
        s+=(ord(x)-ord('A')+1)
    total+=s*cnt
print total

