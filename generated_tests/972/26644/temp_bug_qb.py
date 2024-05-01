def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	global_list.append(('YES' if ((a == (b + 1)) or (b == (a + 1)) or (a == b)) else 'NO'))
	return global_list