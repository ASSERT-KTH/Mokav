def patched_func(*args):
	global_list = []
	
	n = args[0]
	global_list.append([n, n.swapcase()][(n[1:] == n[1:].upper())])
	return global_list