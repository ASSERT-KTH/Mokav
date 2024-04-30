def original_func(*args):
	global_list = []
	
	(x1, x2, x3) = map(int, args[0].split())
	a_x = (((x1 + x2) + x3) // 3)
	global_list.append(((abs((a_x - x1)) + abs((a_x - x2))) + abs((a_x - x3))))
	return global_list