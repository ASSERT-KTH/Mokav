def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a <= 12):
	    ret_values.append((1 << a))
	else:
	    ret_values.append((8092 << (a - 13)))

	return ret_values
