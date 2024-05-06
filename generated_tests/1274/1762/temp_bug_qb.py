def original_func(*args):
	global_list = []
	
	(*m, d) = (int(args[0]) for i in range(5))
	global_list.append(sum((any((((i + 1) % k) for k in m)) for i in range(d))))
	return global_list