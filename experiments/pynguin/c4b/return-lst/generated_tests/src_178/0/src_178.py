def func(*args):
	ret_values = []
	
	(n, c1, c2, c3) = map(int, args[0].split())
	if ((n % 4) == 0):
	    ret_values.append(0)
	elif ((n % 4) == 1):
	    ret_values.append(min([c3, (c2 + c1), (c1 * 3)]))
	elif ((n % 4) == 2):
	    ret_values.append(min([c2, (c1 * 2), (c3 * 2)]))
	else:
	    ret_values.append(min([(c3 * 3), (c2 + c3), c1]))

	return ret_values
