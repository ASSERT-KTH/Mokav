def patched_func(*args):
	global_list = []
	
	e = ((10 ** 9) + 9)
	(n, m) = map(int, args[0].split())
	t = pow(2, m, e)
	r = 1
	for i in range(n):
	    r = ((r * ((t - i) - 1)) % e)
	global_list.append(r)
	return global_list