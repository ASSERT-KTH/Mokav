def func(*args):
	ret_values = []
	
	ret_values.append(pow(3, max((int(args[0]) - 1), 0), 1000003))

	return ret_values
