def original_func(*args):
	global_list = []
	
	a = tuple(map(int, args[0].split()))
	global_list.append(int((a in ((13, 10), (6, 12), (21, 18)))))
	return global_list