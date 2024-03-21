def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n == 1) or (n == 2)):
	    ret_values.append((- 1))
	    exit()
	if ((n % 2) == 0):
	    ret_values.append((((n * n) // 4) - 1), (((n * n) // 4) + 1))
	else:
	    ret_values.append(((n * n) // 2), (((n * n) // 2) + 1))

	return ret_values
