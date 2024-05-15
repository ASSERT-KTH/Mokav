def patched_func(*args):
	global_list = []
	
	(a, b, c, d, e) = map(int, args[0].split())
	a = (a - b)
	k = 1
	r = 1
	while (a > 0):
	    k = (k + 1)
	    a = ((a - min((b + (d * r)), c)) + e)
	    r = (r + 1)
	global_list.append(k)
	return global_list