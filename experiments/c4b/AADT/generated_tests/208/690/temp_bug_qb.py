def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	global_list.append(min(abs((a - c)), abs((d - b))))
	return global_list