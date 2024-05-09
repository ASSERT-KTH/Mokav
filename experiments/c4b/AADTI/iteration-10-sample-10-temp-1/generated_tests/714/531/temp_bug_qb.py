def original_func(*args):
	global_list = []
	
	'input\n6 6 5 8 9\n'
	(l1, r1, l2, r2, k) = map(int, args[0].split())
	l = max(l1, l2)
	r = min(r1, r2)
	global_list.append((((r - l) + 1) if ((k < l) or (k > r)) else (r - l)))
	return global_list