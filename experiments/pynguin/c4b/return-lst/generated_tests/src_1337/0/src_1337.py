def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    ret_values.append(('1' * (n // 2)))
	else:
	    ret_values.append(('7' + ('1' * ((n // 2) - 1))))

	return ret_values
