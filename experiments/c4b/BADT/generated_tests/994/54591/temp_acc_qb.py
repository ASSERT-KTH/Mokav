def patched_func(*args):
	global_list = []
	
	from math import *
	(n, m, a) = map(float, args[0].strip().split())
	global_list.append((ceil((n / a)) + (ceil(((m - a) / a)) * ceil((n / a)))))
	return global_list