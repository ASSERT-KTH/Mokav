def func(*args):
	ret_values = []
	
	import math
	(n, a, b, c) = [int(x) for x in args[0].split(' ')]
	f = ([0] * (n + 1))
	f[0] = 0
	for i in range(1, (n + 1)):
	    if ((i - a) < 0):
	        x = (- math.inf)
	    else:
	        x = f[(i - a)]
	    if ((i - b) < 0):
	        y = (- math.inf)
	    else:
	        y = f[(i - b)]
	    if ((i - c) < 0):
	        z = (- math.inf)
	    else:
	        z = f[(i - c)]
	    f[i] = max((1 + x), (1 + y), (1 + z))
	ret_values.append(f[n])

	return ret_values
