def patched_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	l = (k * l)
	c = (d * c)
	global_list.append((min((p // np), c, (l // nl)) // n))
	return global_list