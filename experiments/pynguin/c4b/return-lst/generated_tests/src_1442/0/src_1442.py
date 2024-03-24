def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = ((x + 4) // 5)
	ret_values.append(y)

	return ret_values
