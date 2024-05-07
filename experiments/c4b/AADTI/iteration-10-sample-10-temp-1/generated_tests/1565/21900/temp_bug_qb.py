def original_func(*args):
	global_list = []
	
	(a, b, r) = map(int, args[0].split())
	w = ((a // r) // 2)
	h = ((b // r) // 2)
	global_list.append(('First' if ((w * h) % 2) else 'Second'))
	return global_list