def func(*args):
	ret_values = []
	
	n = args[0]
	n = int(n)
	if ((n % 2) != 0):
	    ret_values.append((n // 2))
	else:
	    ret_values.append(((n // 2) - 1))

	return ret_values
