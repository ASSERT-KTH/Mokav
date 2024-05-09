def original_func(*args):
	global_list = []
	
	(x1, x2, x3) = map(int, args[0].split())
	mid = int((((x1 + x2) + x3) / 3))
	tot = 0
	tot = ((abs((x1 - mid)) + abs((x2 - mid))) + abs((x3 - mid)))
	global_list.append(tot)
	return global_list