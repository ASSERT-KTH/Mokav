def original_func(*args):
	global_list = []
	
	from math import inf
	(a, b) = [int(x) for x in args[0].split()]
	(c, d) = [int(x) for x in args[1].split()]
	if (a > c):
	    (a, c) = (c, a)
	    (b, d) = (d, b)
	r1 = ((d - b) % a)
	r2 = (c % a)
	k2s = [((r1 + (k2 * r2)) % a) for k2 in range(a)]
	if (0 not in k2s):
	    global_list.append((- 1))
	else:
	    global_list.append(((k2s.index(0) * c) + d))
	return global_list