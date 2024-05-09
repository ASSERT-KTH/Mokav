def patched_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	s = []
	if (d1 < d2):
	    s.append(((d1 + d3) + d2))
	    s.append(((d1 * 2) + (d2 * 2)))
	    s.append(((d1 * 2) + (d3 * 2)))
	else:
	    s.append(((d1 + d3) + d2))
	    s.append(((d1 * 2) + (d2 * 2)))
	    s.append(((d2 * 2) + (d3 * 2)))
	global_list.append(min(s))
	return global_list