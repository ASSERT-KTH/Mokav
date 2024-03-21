def func(*args):
	ret_values = []
	
	n = (int(args[0]) - 10)
	if ((n <= 0) or (n > 11)):
	    ret_values.append(0)
	elif (n < 10):
	    ret_values.append(4)
	elif (n == 10):
	    ret_values.append(15)
	else:
	    ret_values.append(4)

	return ret_values
