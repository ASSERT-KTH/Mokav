def patched_func(*args):
	global_list = []
	
	import math
	(n, m, a) = [int(x) for x in args[0].split()]
	r = math.ceil((n / a))
	c = math.ceil((m / a))
	global_list.append((r * c))
	return global_list