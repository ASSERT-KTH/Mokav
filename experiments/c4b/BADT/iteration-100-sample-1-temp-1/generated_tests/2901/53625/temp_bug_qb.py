def original_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	c -= v0
	s = 1
	while (c > 0):
	    if (v0 < v1):
	        v0 += a
	    c -= (v0 - l)
	    s += 1
	global_list.append(s)
	return global_list