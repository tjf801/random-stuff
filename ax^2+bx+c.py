import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def factor(x):
	x = abs(x)
	factors = []
	for i in range(1, x+1):
		if x % i == 0:
			factors.append(i)
			factors.append(int(x/i))
	return factors

af = factor(a)
cf = factor(c)

#(dx+e)(fx+g)


l = 0
m = 0

#b and c positive
if (b>0 and c>0):
	for j in range(1, (int((len(cf)+1)/2))+1):
		for i in range(1, (int((len(af)+1)/2))+1):
			if ((af[l]*cf[m+1])+(af[l+1]*cf[m])==b):
				d = str(af[l])
				e = str(cf[m])
				f = str(af[l+1])
				g = str(cf[m+1])
				print("("+d+"x+"+e+")"+"("+f+"x+"+g+")")
			l = l + 2
		m = m + 2
		l = 0

#b neg c positive
if (b<0 and c>0):
	for j in range(1, (int((len(cf)+1)/2))+1):
		for i in range(1, (int((len(af)+1)/2))+1):
			if ((af[l]*cf[m+1])+(af[l+1]*cf[m])==b):
				d = str(af[l])
				e = str(cf[m])
				f = str(af[l+1])
				g = str(cf[m+1])
				print("("+d+"x+"+e+")"+"("+f+"x+"+g+")")
			l = l + 2
		m = m + 2
		l = 0