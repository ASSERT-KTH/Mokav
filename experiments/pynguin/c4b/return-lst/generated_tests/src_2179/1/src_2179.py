def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if ((3 * a) <= b):
	    ret_values.append(0)
	else:
	    ret_values.append(((3 * a) - b))

	return ret_values
