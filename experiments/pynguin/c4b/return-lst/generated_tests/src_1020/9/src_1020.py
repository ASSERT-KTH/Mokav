def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = ((x // 5) + ((x % 5) != 0))
	ret_values.append(y)

	return ret_values
