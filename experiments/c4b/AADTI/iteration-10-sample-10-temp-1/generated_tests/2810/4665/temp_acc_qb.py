def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	mid = ((1 + n) // 2)
	global_list.append(((mid + n) % (n + 1)))
	return global_list