def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	global_list.append(('YES' if ((abs((a - b)) <= 1) and ((a != 0) and (b != 0))) else 'NO'))
	return global_list