def patched_func(*args):
	global_list = []
	
	(p, q) = args[0].split()
	p = int(p)
	q = int(q)
	high = max(p, q)
	low = min(p, q)
	global_list.append(('%d %d' % ((((p + q) - 1) - low), low)))
	return global_list