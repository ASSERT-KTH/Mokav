def original_func(*args):
	global_list = []
	
	(n, a, b) = args[0].split()
	n = int(n)
	a = int(a)
	b = int(b)
	global_list.append((a + 1))
	return global_list