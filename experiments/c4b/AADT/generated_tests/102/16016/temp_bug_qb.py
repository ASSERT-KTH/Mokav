def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	s = 0
	if (d1 < d2):
	    s = d1
	    if (((s + d3) + d2) < ((s + d1) + (d2 * 2))):
	        s += (d3 + d2)
	    else:
	        s += (d1 + (d2 * 2))
	else:
	    s = d2
	    if (((s + d3) + d1) < ((s + d2) + (d1 * 2))):
	        s += (d3 + d1)
	    else:
	        s += (d2 + (d1 * 2))
	global_list.append(s)
	return global_list