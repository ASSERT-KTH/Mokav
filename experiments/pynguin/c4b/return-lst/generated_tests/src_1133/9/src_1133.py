def func(*args):
	ret_values = []
	
	import math
	(n, m, a) = [int(x) for x in args[0].split()]
	ret_values.append((math.ceil((n / a)) * math.ceil((m / a))))

	return ret_values
