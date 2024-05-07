def original_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	a = l.pop(4)
	global_list.append(max(0, (min(l) - a)))
	return global_list