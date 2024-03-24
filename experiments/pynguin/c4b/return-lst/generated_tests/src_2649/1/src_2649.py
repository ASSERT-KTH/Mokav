def func(*args):
	ret_values = []
	
	n = int(args[0])
	v = (((n // 2) - 1) if ((n % 2) == 0) else (n // 2))
	ret_values.append(v)

	return ret_values
