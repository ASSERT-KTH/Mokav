def func(*args):
	ret_values = []
	
	a = int(args[0])
	res = (((a * 6) * (a - 1)) + 1)
	ret_values.append(res)

	return ret_values
