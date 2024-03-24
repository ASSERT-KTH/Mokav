def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 4) and ((n % 2) == 0)):
	    ret_values.append(int((n / 4)))
	elif ((n % 2) == 0):
	    ret_values.append((int((n / 4)) - 1))
	else:
	    ret_values.append(0)

	return ret_values
