def func(*args):
	ret_values = []
	
	import math
	(a, b, n) = map(int, args[0].split())
	while True:
	    if (n == 0):
	        ret_values.append('1')
	        break
	    n -= math.gcd(a, n)
	    if (n == 0):
	        ret_values.append('0')
	        break
	    n -= math.gcd(b, n)

	return ret_values
