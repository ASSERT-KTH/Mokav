def func(*args):
	ret_values = []
	
	a = [int(x) for x in args[0].split()]
	ret_values.append(int(((a[0] * a[1]) / 2)))

	return ret_values
