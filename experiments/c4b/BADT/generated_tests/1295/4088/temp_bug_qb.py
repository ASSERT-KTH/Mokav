def original_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	l = (k * l)
	c = (d * c)
	global_list.append(min((l // (nl * n)), c, (p // ((np * n) * 2))))
	return global_list