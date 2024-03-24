def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if ((not n) and m):
	    ret_values.append('Impossible')
	else:
	    ret_values.append(((n + m) - min(m, n)), (((m + n) - 1) if m else n))

	return ret_values
