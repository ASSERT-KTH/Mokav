def func(*args):
	ret_values = []
	
	n = int(args[0])
	output = ((n // 3) * 2)
	ret_values.append(((output + 1) if ((n % 3) > 0) else output))

	return ret_values
