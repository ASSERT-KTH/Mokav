def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	elif ((n % 4) == 0):
	    ret_values.append(6)
	elif ((n % 4) == 1):
	    ret_values.append(8)
	elif ((n % 4) == 2):
	    ret_values.append(4)
	else:
	    ret_values.append(2)

	return ret_values
