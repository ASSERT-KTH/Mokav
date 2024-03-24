def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    ret_values.append([6, 8, 4, 2][(n % 4)])

	return ret_values
