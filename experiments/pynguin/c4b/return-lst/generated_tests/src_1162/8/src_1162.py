def func(*args):
	ret_values = []
	
	'input\n\n5\n\n'
	n = int(args[0])
	ret_values.append(((n // 5) + (1 if (n % 5) else 0)))

	return ret_values
