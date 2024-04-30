def original_func(*args):
	global_list = []
	
	(n, m, l, r, k) = map(int, args[0].split())
	x = max(n, l)
	y = min(m, r)
	l = ((x - y) + 1)
	if ((x <= k) and (k <= y)):
	    l -= 1
	global_list.append(max(0, l))
	return global_list