def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = 0
	if (n in range(3, (n + 1), 3)):
	    a = (2 + (2 * ((n - 3) / 3)))
	else:
	    a = (3 + (2 * (((n - (n % 3)) - 3) / 3)))
	ret_values.append(int(a))

	return ret_values
