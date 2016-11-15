for x in range(10, 98):
	
	for y in range(x+1, 99):
		num=list()
		den=list()
		if(not(x%10==0 or y%10==0)):
			num.append(x%10)
			num.append(x/10)
			den.append(y%10)
			den.append(y/10)
			if(num[0]==den[0]):
				if(float(num[1])/den[1]==float(x)/y):
					print num[1], den[1], x, y
			if(num[0]==den[1]):
				if(float(num[1])/den[0]==float(x)/y):
					print num[1], den[0], x, y
			if(num[1]==den[0]):
				if(float(num[0])/den[1]==float(x)/y):
					print num[0], den[1], x, y
			if(num[1]==den[1]):
				if(float(num[0])/den[0]==float(x)/y):
					print num[0], den[0], x, y	
