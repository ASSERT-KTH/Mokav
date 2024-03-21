def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	r = pow(3, n, m)
	if (r == 0):
	    r += m
	ret_values.append((r - 1))

	return ret_values
