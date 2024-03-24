def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (x < 3):
	    ret_values.append((- 1))
	else:
	    b = int((x / 2))
	    if (x % 2):
	        ret_values.append(((2 * b) * (b + 1)), (((2 * b) * (b + 1)) + 1))
	    else:
	        ret_values.append(((b * b) - 1), ((b * b) + 1))

	return ret_values
