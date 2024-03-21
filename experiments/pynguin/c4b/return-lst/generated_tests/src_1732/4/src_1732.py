def func(*args):
	ret_values = []
	
	(n, x, y) = map(int, args[0].split())
	p = int((((n / 100) * y) + 0.9999999))
	if (p <= x):
	    ret_values.append(0)
	else:
	    ret_values.append((p - x))

	return ret_values
