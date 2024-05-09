def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	t = ((4 * 60) - k)
	n_p_c = 1
	while ((t > 0) and (n_p_c <= n)):
	    n_p_c += 1
	    t -= (n_p_c * 5)
	global_list.append((n_p_c - 1))
	return global_list