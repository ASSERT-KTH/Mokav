def original_func(*args):
	global_list = []
	
	from math import *
	(n, m, a) = map(int, args[0].strip().split())
	global_list.append((ceil((n / a)) + ceil((m / a))))
	return global_list