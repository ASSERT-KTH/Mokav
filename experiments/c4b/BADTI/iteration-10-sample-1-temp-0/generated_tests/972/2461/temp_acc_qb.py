def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	global_list.append(('YES' if ((abs((a - b)) <= 1) and (max(a, b) > 0)) else 'NO'))
	return global_list