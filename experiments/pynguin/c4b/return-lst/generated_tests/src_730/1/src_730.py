def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(x) for x in args[0].split()]
	if ((n % 4) == 0):
	    ret_values.append(0)
	elif ((n % 4) == 3):
	    ret_values.append(min(a, (b + c), (c * 3)))
	elif ((n % 4) == 2):
	    ret_values.append(min((a * 2), b, (c * 2)))
	else:
	    ret_values.append(min((a * 3), (b + a), c))

	return ret_values
