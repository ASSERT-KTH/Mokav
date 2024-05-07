def original_func(*args):
	global_list = []
	
	(l, r, k) = map(int, args[0].split())
	global_list.append(' '.join(filter((lambda t: (l <= int(t) <= r)), [str((k ** i)) for i in range(256)])))
	return global_list