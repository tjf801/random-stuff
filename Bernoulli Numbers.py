import fractions

def bernoulli(n):
	A = [0] * (n+1)
	for i in range(n+1):
		A[i] = fractions.Fraction(1, i+1)
		for j in range(i, 0, -1):
			A[j-1] = j*(A[j-1] - A[j])
	return A[0]

print(bernoulli(int(input())))