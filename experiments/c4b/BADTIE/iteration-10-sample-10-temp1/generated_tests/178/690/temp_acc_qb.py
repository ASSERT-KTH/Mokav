def patched_func(*args):
	global_list = []
	
	(l, r, k) = map(int, args[0].split())
	x = list(filter((lambda t: (l <= int(t) <= r)), [str((k ** i)) for i in range(256)]))
	if (len(x) == 0):
	    global_list.append((- 1))
	else:
	    global_list.append(' '.join(x))
	return global_list