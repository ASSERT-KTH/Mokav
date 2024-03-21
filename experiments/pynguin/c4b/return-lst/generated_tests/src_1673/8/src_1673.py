def func(*args):
	ret_values = []
	
	(n, a) = [int(x) for x in args[0].split()]
	if (a & 1):
	    ret_values.append(((a // 2) + 1))
	else:
	    ret_values.append((((n - a) // 2) + 1))

	return ret_values
