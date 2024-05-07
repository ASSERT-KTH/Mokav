def original_func(*args):
	global_list = []
	
	(n, k) = (int(x) for x in args[0].split())
	time = (240 - k)
	r = 0
	while ((time >= 0) and (r <= k)):
	    r += 1
	    time -= (5 * r)
	global_list.append((r - 1))
	return global_list