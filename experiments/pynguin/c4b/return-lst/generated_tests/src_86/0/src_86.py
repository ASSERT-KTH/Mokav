def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = (n // 7)
	l = (n - (m * 7))
	ret_values.append(((m * 2) + (l == 6)), (((m * 2) + (l > 0)) + (l > 1)))

	return ret_values
