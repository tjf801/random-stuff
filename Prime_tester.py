def ptest (p):
	if ( ( p ** 2 ) - 1 ) % 24 == 0:
		print("It Is prime!")
	else:
		print(":(")

def pfind(a):
	n = 24
	b = 0
	print("2.0")
	print("3.0")
	while b < a:
		if (n+1)**0.5==round((n+1)**0.5):
			print((n+1)**0.5)
			b = b+1
		n=n+24
q = int(input("Enter Your Number Here:"))
pfind(q)