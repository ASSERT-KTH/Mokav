def func(*args):
	ret_values = []
	
	from math import gcd
	(a, b, c) = map(int, args[0].split())
	i = 0
	while (0 <= c):
	    if (i == 1):
	        c -= gcd(c, b)
	        i = 0
	    else:
	        c -= gcd(c, a)
	        i = 1
	ret_values.append(i)

	return ret_values
