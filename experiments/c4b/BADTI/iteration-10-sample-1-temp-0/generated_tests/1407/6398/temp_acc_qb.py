def patched_func(*args):
	global_list = []
	
	(a, b) = args[0].split()
	global_list.append((int(a) + int(b[::(- 1)])))
	return global_list