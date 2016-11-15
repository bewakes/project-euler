import sys

fread = open('triangles.txt', 'r')
sys.stdin = fread
cnt = 0
for line in sys.stdin:
	lst = line.split(',')
	l = list()
	for k in range(0,len(lst),2):
		temp = list()
		temp.append(eval(lst[k]))
		temp.append(eval(lst[k+1]))
		l.append(temp)
	flag = True
	for x in range(3):
		# the case when slope is infinity
		if l[x][0] == l[(x+1)%3][0]:
			if (l[x][0]-l[(x+1)%3][0]) * l[x][0] < 0:
				flag = False
				break
			else:
				continue
	
		m = float(l[(x+1)%3][1]-l[x][1])/(l[(x+1)%3][0]-l[x][0])	# the slope
		c = m*(-1)*l[x][0] + l[x][1]	# of the form y-mx = c
		if c==0:
			continue
		exp = "ty-m*tx-c"
		ty = l[(x+2)%3][1]
		tx = l[(x+2)%3][0]
		if eval(exp)*(-1)*c < 0:
			flag = False
			break
	if flag==False:
		print "not origin"
	else:
		cnt+=1
print cnt
