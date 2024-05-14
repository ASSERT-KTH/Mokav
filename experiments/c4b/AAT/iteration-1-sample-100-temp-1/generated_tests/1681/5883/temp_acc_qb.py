def patched_func(*args):
	global_list = []
	
	import math
	(n, m) = map(int, args[0].split())
	a = 0
	c = 0
	while (a <= m):
	    t = (n - (a * a))
	    v = math.sqrt((m - a))
	    if (t == v):
	        c += 1
	    a = (a + 1)
	global_list.append(c)
	return global_list