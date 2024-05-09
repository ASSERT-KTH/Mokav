def patched_func(*args):
	global_list = []
	
	import sys
	(a, b, c) = map(int, args[0].split())
	global_list.append(((((a + b) - 1) * (c - 1)) + (a * b)))
	return global_list