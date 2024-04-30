def original_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	global_list.append(((- 1) if (max(a, b) < k) else ((a // k) + (b // k))))
	return global_list