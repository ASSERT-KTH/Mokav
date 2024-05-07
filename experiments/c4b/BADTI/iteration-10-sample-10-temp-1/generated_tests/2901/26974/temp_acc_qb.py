def patched_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = (int(x) for x in args[0].split())
	d = 1
	c = (c - v0)
	while (c > 0):
	    v = (v0 + (d * a))
	    if (v > v1):
	        v = v1
	    v = (v - l)
	    c = (c - v)
	    d += 1
	global_list.append(d)
	return global_list