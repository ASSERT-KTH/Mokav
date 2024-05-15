def original_func(*args):
	global_list = []
	
	(a, b) = (int(i) for i in args[0].split())
	global_list.append(('YES' if (abs((a - b)) <= 1) else 'NO'))
	return global_list