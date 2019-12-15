import sys

def f(n):
	if n == 1:
		return 1
	
	return f(n - 1) + (2 * n - 1)

sys.setrecursionlimit(10000)
a = int(input())
print(f(a))