def func(*args):
	ret_values = []
	
	line = sorted([int(x) for x in args[0].split(' ')])
	ret_values.append(str((line[2] - line[0])))

	return ret_values
