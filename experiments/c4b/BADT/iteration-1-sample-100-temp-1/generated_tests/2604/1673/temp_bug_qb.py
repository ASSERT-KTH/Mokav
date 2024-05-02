def original_func(*args):
	global_list = []
	
	m = args[0]
	n = (str((int(m[0]) - 1)) + ('9' * (len(m) - 1)))
	k = sum(list(map(int, m)))
	p = sum(list(map(int, n)))
	global_list.append((int(m) if (p <= k) else int(n)))
	return global_list