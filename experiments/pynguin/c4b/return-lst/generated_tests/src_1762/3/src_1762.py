def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n >= 13):
	    ret_values.append((8092 * (2 ** (n - 13))))
	else:
	    ret_values.append((2 ** n))

	return ret_values
