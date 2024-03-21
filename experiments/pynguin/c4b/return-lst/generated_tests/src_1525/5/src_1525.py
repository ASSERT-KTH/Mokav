def func(*args):
	ret_values = []
	
	x = int(args[0])
	if ((x % 5) == 0):
	    ret_values.append((x // 5))
	else:
	    ret_values.append(((x // 5) + 1))

	return ret_values
