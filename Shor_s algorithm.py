import sys
from random import randint
from math import sqrt, ceil
from fractions import gcd
import decimal

decimal.getcontext().prec = 1000

n = int(sys.argv[1])

#first step

def rndnum(n):
	while True:
		#pick a random number a less than n
		#optional to use ceil(sqrt(n)) instead of n-1
		a = randint(3,ceil(sqrt(n)))
		
		#is a a factor of n?
		if(n%a==0):
			print(a)
			print(n/a)
			print("Done!!!")
			sys.exit()
		
		#check a is coprime with n
		if (gcd(a, n) == 1):
			break
		else:
			print(gcd(a, n))
			print(n/(gcd(a, n)))
			print("Done!!!")
			sys.exit()
	return(a)

#step 2 (the most annoying) (needs quantum computing) :(
while True:
	a = rndnum(n)
	print("a = " +str(a))
	
	#find the period
	b = a**2
	for i in range(2,n):
		b = (b*a)%n
		if (b==1):
			r = i
			break
	
	print("r = " + str(r))
	#check if its a good r
	if ((i/2)%2==0 and (decimal.Decimal((decimal.Decimal(a)**(decimal.Decimal(r/2)))+1))%decimal.Decimal(n)!=decimal.Decimal(0)):
		break

#step 3
print(int(gcd((a**(r/2)-1),n)))
print(int(gcd((a**(r/2)+1),n)))
print("Done!!!")