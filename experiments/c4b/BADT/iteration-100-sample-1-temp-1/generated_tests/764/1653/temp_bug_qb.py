def original_func(*args):
	global_list = []
	
	(x1, x2, x3) = [int(i) for i in args[0].split()]
	avg = (((x1 + x2) + x3) // 3)
	global_list.append(((abs((avg - x1)) + abs((avg - x2))) + abs((avg - x3))))
	return global_list