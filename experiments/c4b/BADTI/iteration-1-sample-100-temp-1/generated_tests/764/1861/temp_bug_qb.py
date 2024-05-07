def original_func(*args):
	global_list = []
	
	l = [int(i) for i in args[0].split()]
	m = (sum(l) // 3)
	global_list.append(((abs((l[0] - m)) + abs((l[1] - m))) + abs((l[2] - m))))
	return global_list