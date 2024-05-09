def original_func(*args):
	global_list = []
	
	global_list.append(abs(sum(((4 - x) for x in set(map(int, args[0].split()))))))
	return global_list