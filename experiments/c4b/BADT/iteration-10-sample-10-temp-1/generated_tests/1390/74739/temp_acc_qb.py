def patched_func(*args):
	global_list = []
	
	import math
	(n, k, p) = map(int, args[0].split())
	need = math.ceil(((n * p) / 100))
	res = (need - k)
	global_list.append((res if (res > 0) else 0))
	return global_list