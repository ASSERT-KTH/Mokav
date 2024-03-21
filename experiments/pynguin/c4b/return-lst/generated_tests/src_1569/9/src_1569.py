def func(*args):
	ret_values = []
	
	import math
	(a, b, s) = (int(i) for i in args[0].split())
	while True:
	    k = math.gcd(a, s)
	    s -= k
	    if (s == 0):
	        ret_values.append(0)
	        exit(0)
	    elif (s < 0):
	        ret_values.append(1)
	        exit(0)
	    k = math.gcd(b, s)
	    s -= k
	    if (s == 0):
	        ret_values.append(1)
	        exit(0)
	    elif (s < 0):
	        ret_values.append(0)
	        exit(0)

	return ret_values
