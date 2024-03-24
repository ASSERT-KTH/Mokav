def func(*args):
	ret_values = []
	
	import math
	(n, m, a) = [int(x) for x in args[0].split()]
	r = math.ceil((n / a))
	c = math.ceil((m / a))
	ret_values.append((r * c))

	return ret_values
