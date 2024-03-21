def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(((- 1) if (n < 3) else (210 * (((10 ** (n - 1)) // 210) + 1))))

	return ret_values
