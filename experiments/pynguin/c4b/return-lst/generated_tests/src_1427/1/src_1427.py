def func(*args):
	ret_values = []
	
	a = int(args[0])
	x = 0
	if (a < 0):
	    exit(0)
	if (a < 13):
	    x = (2 ** a)
	    ret_values.append(x)
	else:
	    x = (8092 * (2 ** (a - 13)))
	    ret_values.append(x)

	return ret_values
