def original_func(*args):
	global_list = []
	
	(a, b, c, d, e) = map(int, args[0].split())
	a = (a - b)
	k = 1
	r = 1
	while (a > 0):
	    k = (k + 1)
	    if (c > ((b + e) + (d * r))):
	        V = ((b + (d * r)) - e)
	    else:
	        V = (c - e)
	    a = (a - V)
	    r = (r + 1)
	global_list.append(k)
	return global_list