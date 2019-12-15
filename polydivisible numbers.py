import sys
n = int(sys.argv[1])

for i in range(10**(n-1), 10**n):
	for j in range(1, n+1):
		if(int(str(i)[:j]))%j!=0:
			break
		if(j==n):
			print(i)
