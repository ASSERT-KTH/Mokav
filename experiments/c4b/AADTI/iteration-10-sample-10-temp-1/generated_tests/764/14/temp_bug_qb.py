def original_func(*args):
	global_list = []
	
	a = args[0].split()
	b = int(max(a))
	c = int(min(a))
	global_list.append((b - c))
	return global_list