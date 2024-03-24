def func(*args):
	ret_values = []
	
	import sys
	(x, y, z) = map(int, args[0].split())
	for a in range(1, 10001):
	    if ((x % a) == 0):
	        b = (x // a)
	        if ((y / b) == (z / a)):
	            ret_values.append((4 * ((a + b) + (y // b))))
	            sys.exit()

	return ret_values
