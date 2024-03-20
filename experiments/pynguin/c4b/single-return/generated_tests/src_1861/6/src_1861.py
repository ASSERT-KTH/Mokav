def func(*args):
	
	(p, q) = args[0].split()
	p = int(p)
	q = int(q)
	high = max(p, q)
	low = min(p, q)
	return(('%d %d' % ((((p + q) - 1) - low), low)))
