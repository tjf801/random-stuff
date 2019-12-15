def pi(x):
	t = 0
	x = floor(x)
	for i in range(x):
		if isprime(i):
			t = t+1
	return t

import sys
from math import sqrt

def isprime(n):
	if n > 1:
		for i in range(2,round(sqrt(n))):
			if (n % i) == 0:
				print(n,"is not prime")
				print(i,"times",int(n/i),"=",n)
				break
		else:
			return True
	else:
		return False
