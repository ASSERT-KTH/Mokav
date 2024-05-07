def original_func(*args):
	global_list = []
	
	n = int(args[0])
	p = ((9 ** n) * (3 ** n))
	global_list.append((p - (7 ** n)))
	return global_list