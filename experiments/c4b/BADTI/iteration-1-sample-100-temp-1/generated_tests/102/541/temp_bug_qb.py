def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	s = 0
	s += d1
	if ((d1 + d2) < d3):
	    s += (d1 + d2)
	else:
	    s += d3
	if (d2 < (d1 + d3)):
	    s += d2
	else:
	    s += (d1 + d3)
	global_list.append(s)
	return global_list