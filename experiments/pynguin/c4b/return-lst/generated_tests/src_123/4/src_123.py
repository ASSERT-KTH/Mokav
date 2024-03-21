def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = 1
	if (x >= 13):
	    y = 8092
	    x -= 13
	ret_values.append((y << x))

	return ret_values
