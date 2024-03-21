def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 3):
	    ret_values.append('-1')
	elif ((n * n) % 4):
	    ret_values.append(((n * n) // 2), (((n * n) // 2) + 1))
	else:
	    ret_values.append((((n * n) // 4) - 1), (((n * n) // 4) + 1))

	return ret_values
