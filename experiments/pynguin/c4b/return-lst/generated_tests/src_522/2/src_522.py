def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n > 5) and ((n % 5) != 0)):
	    ret_values.append(int(((n / 5) + 1)))
	elif (n <= 5):
	    ret_values.append('1')
	else:
	    ret_values.append(int((n / 5)))

	return ret_values
