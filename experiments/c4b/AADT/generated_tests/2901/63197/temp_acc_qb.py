def patched_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	days = 1
	i = 1
	c -= v0
	while (c > 0):
	    toread = (v0 + (i * a))
	    if (toread > v1):
	        toread = v1
	    toread -= l
	    c -= toread
	    i += 1
	    days += 1
	global_list.append(days)
	return global_list