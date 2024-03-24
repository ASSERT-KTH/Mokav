def func(*args):
	ret_values = []
	
	(n, a, b) = list(map(int, args[0].split()))
	if ((n - a) < (b + 1)):
	    ret_values.append((n - a))
	else:
	    ret_values.append((b + 1))

	return ret_values
