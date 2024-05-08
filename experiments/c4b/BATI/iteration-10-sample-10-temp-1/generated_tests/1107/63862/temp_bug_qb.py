def original_func(*args):
	global_list = []
	
	f = (lambda a, b: (a if (b == 0) else f(b, (a % b))))
	(a, b, n) = map(int, args[0].split())
	c = 1
	while (n > 0):
	    c ^= 3
	    n -= [f(a, n), f(b, n)][(c - 1)]
	global_list.append(c)
	return global_list