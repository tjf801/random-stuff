import sys

n = int(sys.argv[1])
seen = []

x = 2
a = 3
b = -1

while true:
	print(n)
	if n%x == 0:
		n = int(n/x)
	else:
		n = a*n+b
	if n in seen:
		print(n)
		break
	else:
		seen.append(n)