def getL(l, b, h):
    sq = l**2*b**4 +(h**2-b**2)*l**2*b**2
    sq = sq**0.5
    return (sq-l*b**2)/(h**2-b**2)

def getB(l,b,h):
    sq = b**2*l**4 +(h**2-l**2)*b**2*l**2
    sq = sq**0.5
    return (sq-b*l**2)/(h**2-l**2)

def getH(l, b, h):
    sq = h**2*l**4 + (b**2-l**2)*h**2*l**2
    sq = sq**0.5
    return (sq-h*l**2)/(b**2-l**2)

def pathL(l, ll, b, h):
    return (ll**2+b**2)**0.5 + ((l-ll)**2+h**2)**0.5

def pathB(l,b,bb,h):
    return (bb**2+l**2)**0.5 + ((b-bb)**2+h**2)**0.5

def pathH(l, b, h, hh):
    return (hh**2+l**2)**0.5 + ((h-hh)**2+b**2)**0.5

M = 2000*500

cnt=0
def main():
    global cnt
    largestL = 0
    while cnt<=M:
        largestL += 1
        l = 3
        while l<=2*largestL:
            hyp = (largestL**2+l**2)**0.5
            if hyp == int(hyp):
                print([(largestL, x, int(l)-x) for x in range(1,l//2+1)])
                if l<=largestL:
                    cnt+= l//2
                else:
                    cnt+= 1+largestL - (l+1)//2
            l+=1
    print(largestL)
main()
