def factorial(n): #Recursive
	
	if n == 1:
		return 1
		
	return n * factorial(n - 1)

def factorial(n): #Non-Recursive (Better)
	r = n
	
	while n > 1:
		n = n - 1
		r = r * n
	return(r)

a = int(input("Factorial of:"))
print(factorial(a))