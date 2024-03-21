def func(*args):
	ret_values = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if ((n - a) > (b + 1)):
	    ret_values.append((b + 1))
	else:
	    ret_values.append((n - a))

	return ret_values
