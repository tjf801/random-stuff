import sys
import math
import cmath
import fractions

s = complex(sys.argv[1])

def bernoulli(n):
	A = [0] * (n+1)
	for i in range(n+1):
		A[i] = fractions.Fraction(1, i+1)
		for j in range(i, 0, -1):
			A[j-1] = j*(A[j-1] - A[j])
	return A[0]

def nCr(n, r):
	a = math.factorial(n)
	b = math.factorial(r)
	c = math.factorial(n - r)
	d = b*c
	return(a/d)

def zeta(s):
    if s.imag == 0: 
    	s = float(s)
    	if s > 1:
    		if (s%2 == 0):
    			s = int(s)
    			a = bernoulli(s)
    			#(((2^(m-1))*|Bm|*pi^m)/m!)
    			b = 2**(s-1)
    			c = math.factorial(s)
    			#fraction is x/y
    			x = b*abs(a.numerator)
    			y = (a.denominator)*c
    			z = math.gcd(x, y) #for simplifying later
    			if x==z:
    				print("(pi^"+str(s)+")/"+str(int(y/z)))
    			else:
    				print(str(int(x/z))+"(pi^"+str(s)+")/"+str(int(y/z)))
    		j = 0
    		for i in range(1, int(input("Precision: "))):
    			j = j + 1/(i**s)
    		j = str(j)
    		j = j[:-4]
    		print(j)
    	elif s == 1:
    		print("Infinity")
    	elif s == 0:
    		print("-1/2")
    	elif s < 0:
    		if (s%2==1):
    			s = int(s)
    			f = bernoulli(abs(s)+1)
    			a = (-1)*(f.numerator)
    			b = (abs(s)+1)*(f.denominator)
    			z = math.gcd(a, b)
    			print(str(int(a/z))+"/"+str(int(b/z)))
    			res = (a/z)/(b/z)
    			print(res)
    		elif s%2==0: 
    			print("0")
    		else:
    			a = 2**s
    			b = (math.pi)**(s-1)
    			c = math.sin((math.pi*s)/2)
    			d = math.gamma(1-s)
    			e = 0
    			for i in range(1, int(input("Precision: "))):
    				e = e + 1/(i**(1-s))
    			f = a*b*c*d*e
    			print(f)
    	else:
    		a = 0
    		for i in range(1, int(input("Precision: "))):
    			if i%2 == 1:
    				a = a + 1/(i**s)
    			else:
    				a = a - 1/(i**s)
    		b = 1/(1-(2**(1-s)))
    		c=a*b
    		print(c)
    else:
    	a = 1/(1 - 2**(1-s))
    	b = 0
    	for n in range(int(input('Precision: '))):
    		c = 1 / (2 ** (n + 1))
    		d = 0
    		for k in range(n):
    			e = nCr(n, k)
    			if k%2 == 0:
    				d = d + e*(1/((k + 1)**(s)))
    			else:
    				d = d - e*(1/((k + 1)**(s)))
    		b = b + c*d
    	print((math.e)*a*b)