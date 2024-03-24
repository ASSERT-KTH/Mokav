def func(*args):
	ret_values = []
	
	(n, a, b) = [int(x) for x in args[0].split()]
	if ((b + 1) < (n - a)):
	    ret_values.append((b + 1))
	else:
	    ret_values.append((n - a))

	return ret_values
