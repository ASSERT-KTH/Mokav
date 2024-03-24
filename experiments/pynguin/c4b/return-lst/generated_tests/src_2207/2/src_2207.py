def func(*args):
	ret_values = []
	
	from math import *
	(n, m) = [int(j) for j in args[0].split()]
	if (n <= m):
	    ret_values.append(n)
	else:
	    k = ceil((((- 1) + sqrt((1 + (8 * (n - m))))) / 2))
	    while ((k * (k + 1)) >= (2 * (n - m))):
	        k -= 1
	    k += 1
	    ret_values.append((m + k))

	return ret_values
