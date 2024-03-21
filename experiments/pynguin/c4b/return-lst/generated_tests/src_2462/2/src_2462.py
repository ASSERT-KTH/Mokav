def func(*args):
	ret_values = []
	
	from math import ceil
	n = int(args[0])
	ret_values.append(ceil(max(0, ((n / 2) - 1))))

	return ret_values
