def func(*args):
	ret_values = []
	
	a = int(args[0])
	ret_values.append(((((((a + 1) * a) * (a - 1)) // 6) + a) // 1))

	return ret_values
