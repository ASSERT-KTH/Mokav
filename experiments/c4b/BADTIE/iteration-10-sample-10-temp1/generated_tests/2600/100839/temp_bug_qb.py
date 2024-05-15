def original_func(*args):
	global_list = []
	
	n = args[0]
	years = [int(s) for s in args[1].split()]
	global_list.append((sum(years) / int(n)))
	return global_list