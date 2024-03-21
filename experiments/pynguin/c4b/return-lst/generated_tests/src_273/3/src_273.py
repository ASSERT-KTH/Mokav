def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	elif (((n - 1) % 4) == 0):
	    ret_values.append(8)
	elif (((n - 2) % 4) == 0):
	    ret_values.append(4)
	elif (((n - 3) % 4) == 0):
	    ret_values.append(2)
	elif (((n - 4) % 4) == 0):
	    ret_values.append(6)

	return ret_values
