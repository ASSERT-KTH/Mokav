def func(*args):
	ret_values = []
	
	'input\n3\n'
	n = int(args[0])
	if (n <= 2):
	    ret_values.append((- 1))
	elif ((n % 2) == 0):
	    ret_values.append((((n ** 2) // 4) - 1), (((n ** 2) // 4) + 1))
	else:
	    ret_values.append((((n ** 2) - 1) // 2), (((n ** 2) + 1) // 2))

	return ret_values
