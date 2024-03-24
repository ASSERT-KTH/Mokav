def func(*args):
	ret_values = []
	
	n = int(args[0])
	res = ((2 * (n // 3)) + ((n % 3) > 0))
	ret_values.append(res)

	return ret_values
