def func(*args):
	
	import math
	(n, m, a) = [int(x) for x in args[0].split()]
	return((math.ceil((n / a)) * math.ceil((m / a))))
