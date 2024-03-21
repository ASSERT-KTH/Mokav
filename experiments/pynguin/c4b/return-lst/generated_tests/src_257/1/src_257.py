def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	n -= a
	if (n > (b + 1)):
	    ret_values.append((b + 1))
	else:
	    ret_values.append(n)

	return ret_values
