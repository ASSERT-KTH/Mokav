def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	n = (n % 4)
	if (n == 0):
	    ret_values.append(0)
	elif (n == 1):
	    ret_values.append(min((3 * a), (a + b), c))
	elif (n == 2):
	    ret_values.append(min((2 * a), b, (2 * c)))
	elif (n == 3):
	    ret_values.append(min(a, (b + c), (3 * c)))

	return ret_values
