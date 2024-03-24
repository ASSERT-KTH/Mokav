def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (1 <= n <= 2000):
	    s = int((((n * ((n * n) - 1)) / 6) + n))
	    ret_values.append(s)

	return ret_values
