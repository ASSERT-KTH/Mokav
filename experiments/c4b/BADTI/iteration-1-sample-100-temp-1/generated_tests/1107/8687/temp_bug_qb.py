def original_func(*args):
	global_list = []
	
	import math
	(a, b, n) = map(int, args[0].split())
	while True:
	    if (n == 0):
	        global_list.append('1')
	        break
	    n -= math.gcd(a, n)
	    if (n == 0):
	        global_list.append('0')
	        break
	    n -= math.gcd(a, n)
	return global_list