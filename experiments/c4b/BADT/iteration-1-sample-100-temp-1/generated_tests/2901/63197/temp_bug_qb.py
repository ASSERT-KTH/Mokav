def original_func(*args):
	global_list = []
	
	from math import fabs
	(c, v0, v1, a, l) = map(int, args[0].split())
	days = 1
	i = 1
	c -= v0
	while (c > 0):
	    toread = ((v0 + (i * a)) + l)
	    if (toread <= v1):
	        c -= toread
	    else:
	        c -= v1
	    i += 1
	    days += 1
	if ((c == 0) or (fabs(c) == v0)):
	    global_list.append(days)
	else:
	    global_list.append((days + 1))
	return global_list