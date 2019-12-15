import sys
from random import randint
from math import sqrt
from math import ceil
from fractions import gcd

n = int(sys.argv[1])

#first step

def rndnum(n):
	while True:
		#pick a random number a less than n
		#optional to use ceil(sqrt(n)) instead of n-1
		a = randint(3,n-1)
		
		#is a a factor of n?
		if(n%a==0):
			print(a)
			print(n/a)
			sys.exit()
		
		#check a is coprime with n
		if (gcd(a, n) == 1):
			break
	
	return(a)

#step 2 (the most annoying) (needs quantum computing) =(
while True:
	a = rndnum(n)
	
	#find the period
	for i in range(1,n):
		if (a**i%n==1):
			r = i
			break
		
	#check if its a good r
	if ((i/2)%2==0 and ((a**(r/2))+1)%n!=0):
		break

#step 3
print(int(gcd((a**(r/2)-1),n)))
print(int(gcd((a**(r/2)+1),n)))
