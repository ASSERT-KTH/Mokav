def func(*args):
	ret_values = []
	
	(n, a, b) = list(map(int, args[0].split()))
	if ((a >= 0) and (b >= 0)):
	    ret_values.append(((b // n) - ((a - 1) // n)))
	elif ((a < 0) and (b < 0)):
	    ret_values.append((((- a) // n) - (((- b) - 1) // n)))
	else:
	    ret_values.append((((b // n) + ((- a) // n)) + 1))

	return ret_values
