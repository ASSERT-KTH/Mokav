def patched_func(*args):
	global_list = []
	
	x = list(map(int, args[0].strip().split()))
	global_list.append(abs((min(x) - max(x))))
	return global_list