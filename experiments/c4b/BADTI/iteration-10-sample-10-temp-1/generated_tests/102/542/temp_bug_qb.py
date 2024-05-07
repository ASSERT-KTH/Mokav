def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	global_list.append(((sum(a) - max(a)) << 1))
	return global_list