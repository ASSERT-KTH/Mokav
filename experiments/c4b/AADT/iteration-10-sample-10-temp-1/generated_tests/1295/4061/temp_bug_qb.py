def original_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	S = ((k * l) / nl)
	S1 = (c * d)
	S2 = (p / np)
	global_list.append(('%.0f' % (min(S, S1, S2) / n)))
	return global_list