INF = 999999

def getminind(l, used):
	for i, x in enumerate(l):
		if i not in used:
			mini = i
			minv = x
	for i, x in enumerate(l):
		if x<minv and i not in used:
			minv = x
			mini = i
	return mini

def prim(g):
	l = len(g)
	frm = [-1] * l
	wts = [INF]*l
	wts[0] = 0
	used = []
	weights = []
	while len(used)!=l:
		curr = getminind(wts,used)
		used.append(curr)
		weights.append(wts[curr])
		
		for i, x in enumerate(g[curr]):
			if i!=curr and x< wts[i]:
				wts[i] =x
				frm[i] = curr	
	return (weights, frm)	
def main():
        f = open('p107_network.txt', 'r')
        g = []
        s = 0
        for line in f:
                g.append([int(x) if x !='-' else INF for x in line.strip().split(',')])
                l = [int(x) if x!='-' else 0 for x in line.strip().split(',')]
                s+=sum(l)
        s=0
        for k in g:
                for x in k:
                        if x!=INF:
                                s+=x
        print(s)
        wts, frm = prim(g)
        print(wts)
        print(sum(wts))
        print(s - sum(wts))
main()
