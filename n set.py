def get_n_distance(n):
	if n==1:
		return "set"
	elif n==2: 
		return "100\nset\n100\nset\n100\nset\n100"
	elif n==3:
		return "800"
	elif n==4:
		return "short block"

def n_set(n):
	if n == 1:
		return "set"
	else:
		return n_set(n-1) + "\n" + get_n_distance(n) + "\n" + n_set(n-1)

print(n_set(4))