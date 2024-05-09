def original_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	Vn = ((k * l) // n)
	Ln = (d * c)
	global_list.append((min(Vn, Ln, p) // n))
	return global_list