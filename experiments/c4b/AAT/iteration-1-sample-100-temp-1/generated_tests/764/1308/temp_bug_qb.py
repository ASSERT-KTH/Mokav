def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	global_list.append(round(((a[2] + a[0]) / 2)))
	return global_list