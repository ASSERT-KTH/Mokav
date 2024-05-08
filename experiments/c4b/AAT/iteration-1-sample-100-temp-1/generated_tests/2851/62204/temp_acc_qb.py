def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	n = int((a ** 0.5))
	global_list.append(('Vladik' if ((n * (n + 1)) <= b) else 'Valera'))
	return global_list