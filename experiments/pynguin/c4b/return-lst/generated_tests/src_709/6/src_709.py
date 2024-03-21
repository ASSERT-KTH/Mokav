def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	if (a <= (b - c)):
	    ret_values.append((n // a))
	elif (n < b):
	    ret_values.append((n // a))
	else:
	    ret_values.append((((n - c) // (b - c)) + ((((n - c) % (b - c)) + c) // a)))

	return ret_values
