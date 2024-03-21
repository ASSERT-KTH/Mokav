def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = (n % 3)
	z = (n // 3)
	if (m == 0):
	    ret_values.append((z * 2))
	else:
	    ret_values.append(((z * 2) + 1))

	return ret_values
