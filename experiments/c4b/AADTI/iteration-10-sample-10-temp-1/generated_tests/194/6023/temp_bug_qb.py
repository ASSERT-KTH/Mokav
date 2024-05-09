def original_func(*args):
	global_list = []
	
	x = int(args[0])
	step = (x // 5)
	rem = (x % 5)
	step = (step + (rem // 4))
	rem = (rem % 4)
	step = (step + (rem // 3))
	rem = (rem % 3)
	step = (step + (rem // 2))
	(rem + (rem % 2))
	global_list.append((step + rem))
	return global_list