def func(*args):
	ret_values = []
	
	x = int(args[0])
	ret_values.append(((x // 5) + ((x % 5) != 0)))

	return ret_values
