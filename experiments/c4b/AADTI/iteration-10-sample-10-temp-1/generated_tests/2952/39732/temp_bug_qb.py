def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	global_list.append(('YES' if ((int(n) / int(k)) % 2) else 'NO'))
	return global_list