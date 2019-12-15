from decimal import *

def primefactor (n):
		#Much efficiency, very wow
		i = 2;
		p = 1;
		k = n;
		while (p * p <= k and i * i <=k):
			if (n % i == 0):
				n = n / i
				p = p * i
				print(i)
				if (p == k):
					break
			else:
				i+=1
		if (p!=k):
			print(int(k/p))

primefactor(int(input()))