import decimal
from math import *

# Denominator- Calculates the sum from 0 to k.
def den(k):
    a = decimal.Decimal(factorial(6*k)*(545140134*k+13591409))
    b = decimal.Decimal(factorial(3*k)*(factorial(k)**3)*((-262537412640768000)**k))
    res = a / b
    if k > 0:
        return res + den(k - 1)
    else:
        return res


# Numerator- root_precision is the number of significant digits to use when calculating the root.
def num(root_precision):
    p = decimal.getcontext().prec
    decimal.getcontext().prec = root_precision
    d = decimal.Decimal(10005).sqrt()
    decimal.getcontext().prec = p
    return 426880 * decimal.Decimal(10005).sqrt()
    

# Calculates the Chudnovsky Algorithm for a given k, and precision.
def chudnovsky(k, root_precision):
    return num(root_precision)/den(k)
  
# Example usage
i = int(input("Precision: "))
if i > 50:
	decimal.getcontext().prec = i + 10
else:
	decimal.getcontext().prec = 100
pi_estimate = chudnovsky(i, round(sqrt(i)))
print(pi_estimate)
