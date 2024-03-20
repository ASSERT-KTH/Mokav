def func(*args):
	
	import math
	(n, m, a) = [int(x) for x in args[0].split()]
	r = math.ceil((n / a))
	c = math.ceil((m / a))
	return((r * c))
