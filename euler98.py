def isana(a, b):
    if len(a)!=len(b):return False
    aa = sorted(a)
    bb = sorted(b)
    return aa==bb

def squaresoflen(n):
    l = []
    for x in range(int((10**(n-1))**0.5), int((10**n)**0.5)):
        l.append(x**2) 
    return l

def distincteach(string):
    s = set([x for x in string])
    return len(string)==len(list(s))

def createdict(word, num):
    if len(str(num)) != len(word): return None
    if not distincteach(str(num)):return None
    d = {}
    for x in word[::-1]:
        d[x] = num%10
        num = num//10
    if len(d.keys())!= len(word):
        return None
    return d

def wordtonum(word, d):
    s = ''
    for x in word:
        s+=str(d[x])
    return int(s)

def main():
    f = open('p098_words.txt', 'r')
    l = f.readline()
    f.close()
    words= l.strip().replace('"','').split(',')

    sortlist= sorted(words, key=lambda x: len(x))

    indices = [-1]*len(sortlist[-1]) # indices[i] stores starting index of length i+1
    maxl = len(sortlist[-1])

    i = 0
    while True:
        leng = len(sortlist[i])
        indices[leng-1] = i
        while i<len(sortlist) and len(sortlist[i])==leng:
            i+=1
        if i>=len(sortlist):break
    print(indices)

    pairs = []

    for i, word in enumerate(sortlist):
        l = len(word)
        if l==14:
            y = len(sortlist)
        else: y = indices[l]
        for j in range(i+1, y):
            if isana(word, sortlist[j]):
                pairs.append((word, sortlist[j]))
    print(pairs)
    l = []

    for x,y in pairs:
        if len(x) not in l:l.append(len(x))

    for x in pairs[::-1]:
        lst = squaresoflen(len(x[0]))
        for sq in lst:
            d = createdict(x[0], sq)
            if d!=None:
                num = wordtonum(x[1], d)
                sqrt = int(num**0.5)
                if sqrt*sqrt == num:
                    print(sq, wordtonum(x[1], d))
    
main()
