def patched_func(*args):
	global_list = []
	
	import math
	(n, m, z) = map(int, args[0].split())
	global_list.append((z // ((n * m) // math.gcd(n, m))))
	return global_list