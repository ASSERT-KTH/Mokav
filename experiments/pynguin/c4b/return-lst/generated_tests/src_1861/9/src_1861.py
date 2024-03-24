def func(*args):
	ret_values = []
	
	(p, q) = args[0].split()
	p = int(p)
	q = int(q)
	high = max(p, q)
	low = min(p, q)
	ret_values.append(('%d %d' % ((((p + q) - 1) - low), low)))

	return ret_values
