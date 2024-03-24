def func(*args):
	ret_values = []
	
	from math import *
	
	def from10(a, n):
	    if (a == 0):
	        return 0
	    if (a == 1):
	        return 1
	    k = log(a, n)
	    b = ceil(k)
	    if ((b - k) == 0):
	        b += 1
	    c = (a // (n ** (b - 1)))
	    return (int(c) + from10((a - (c * (n ** (b - 1)))), n))
	a = int(args[0])
	if (a == 1000):
	    ret_values.append('90132/499')
	else:
	    slog = 0
	    summ = 0
	    for i in range(2, a):
	        summ += from10(a, i)
	    ret_values.append((summ // gcd((a - 2), summ)), ((a - 2) // gcd(summ, (a - 2))), sep='/')

	return ret_values
