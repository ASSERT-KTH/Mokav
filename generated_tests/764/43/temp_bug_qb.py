def original_func(*args):
	global_list = []
	
	a = args[0].split()
	a.sort()
	global_list.append((abs((int(a[1]) - int(a[0]))) + abs((int(a[1]) - int(a[2])))))
	return global_list