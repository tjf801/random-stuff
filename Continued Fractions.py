import sys
from math import floor
import time

n = float(sys.argv[1])

while n != 0:
	print(floor(n))
	n = n - floor(n)
	n = 1 / n
	time.sleep(sys.argv[2])