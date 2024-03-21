def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	t = ((4 * 60) - k)
	n_p_c = 0
	while ((t >= 0) and (n_p_c <= n)):
	    n_p_c += 1
	    t -= (n_p_c * 5)
	ret_values.append((n_p_c - 1))

	return ret_values
