def func(*args):
	ret_values = []
	
	from math import gcd
	(a, b, c) = tuple(args[0].split(' '))
	a = int(a)
	b = int(b)
	c = int(c)
	while True:
	    if (gcd(a, c) > c):
	        ret_values.append('1')
	        exit(0)
	    c -= gcd(a, c)
	    if (gcd(b, c) > c):
	        ret_values.append('0')
	        exit(0)
	    c -= gcd(b, c)

	return ret_values
