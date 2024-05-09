def original_func(*args):
	global_list = []
	
	[x1, x2, x3] = [int(x) for x in args[0].split()]
	avg = (((x1 + x2) + x3) / 3)
	global_list.append(int(((abs((x1 - avg)) + abs((x2 - avg))) + abs((x3 - avg)))))
	return global_list