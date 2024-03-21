def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n <= 2):
	    ret_values.append(n)
	elif ((n % 2) != 0):
	    ret_values.append(((n * (n - 1)) * (n - 2)))
	elif ((n % 3) != 0):
	    ret_values.append(((n * (n - 1)) * (n - 3)))
	elif ((n % 2) == 0):
	    ret_values.append((((n - 1) * (n - 2)) * (n - 3)))

	return ret_values
