def func(*args):
	ret_values = []
	
	'input\n4\n'
	n = int(args[0])
	ret_values.append(min(((3 * n) // 2), ((2 * n) - 1)))

	return ret_values
