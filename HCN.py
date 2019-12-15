from math import sqrt
import sys

h = 0
n = 1
numf = 0

def numfactors(n):
	x = 1
	for i in range(1, n):
		if n%i == 0:
			x += 1
	return(x)

while (1==1):
	numf = numfactors(n)
	if numf > h:
		print(str(n) + ": " + str(numf) + " factors")
		h = numf
	n = n + 1

