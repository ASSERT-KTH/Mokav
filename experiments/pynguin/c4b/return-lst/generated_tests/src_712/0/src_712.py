def func(*args):
	ret_values = []
	
	n = (int(args[0]) - 10)
	l = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 15, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	if (n < 0):
	    ret_values.append(0)
	else:
	    ret_values.append(l[n])

	return ret_values
