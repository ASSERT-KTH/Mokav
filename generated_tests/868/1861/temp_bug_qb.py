def original_func(*args):
	global_list = []
	
	a = '6842'
	n = int(args[0])
	n %= 4
	global_list.append(a[n])
	return global_list