def original_func(*args):
	global_list = []
	
	import math
	(n, m, s) = map(int, args[0].split())
	c = 0
	cc = 0
	su = 0
	ss = 0
	if (((s >= m) and (s >= n)) or (s == 1) or (((m % s) == 0) and ((n % s) == 0))):
	    global_list.append((m * n))
	else:
	    su = (math.ceil((n / s)) * math.ceil((m / s)))
	    global_list.append(((su * (n % s)) * (m % s)))
	return global_list