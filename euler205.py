sumnines = [0] * 36
fours = [1,2,3,4]
sixes = [1,2,3,4,5,6]
sumsixes = [0] * 36

for a in fours:
    for b in fours:
        for c in fours:
            for d in fours:
                for e in fours:
                    for f in fours:
                        for g in fours:
                            for h in fours:
                                for i in fours:
                                    sumnines[a+b+c+d+e+f+g+h+i-1]+=1
for a in sixes:
    for b in sixes:
        for c in sixes:
            for d in sixes:
                for e in sixes:
                    for f in sixes:
                        sumsixes[a+b+c+d+e+f-1]+=1

s = 0
for i in range(8,36):
    for j in range(5,i):
        s+=sumnines[i]*sumsixes[j]
print(s/(4**9*6**6))
