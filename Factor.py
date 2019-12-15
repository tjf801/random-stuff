from math import *
from datetime import datetime
import sys
startTime = datetime.now()

def factor(n):
	if (n > 1):
		for i in range(1,ceil(sqrt(n))):
			if (n%i==0):
				print(i)
				print(int(n/i))
	else:
		print("Error")
factor(int(sys.argv[1]))

print(datetime.now() - startTime)