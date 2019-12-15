def pigen(n):
	a = 1
	r = 0
	while a < (2 * n):
		r = r + (1 / a)
		a = a + 2
	print (r * 4)

pigen (10)