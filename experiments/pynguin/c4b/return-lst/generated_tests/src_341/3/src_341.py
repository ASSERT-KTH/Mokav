def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	mod = (n % 4)
	if (mod == 0):
	    ret_values.append(0)
	elif (mod == 1):
	    ret_values.append(min((3 * a), c, (a + b)))
	elif (mod == 2):
	    ret_values.append(min((2 * a), b, (2 * c)))
	elif (mod == 3):
	    ret_values.append(min(a, (3 * c), (b + c)))

	return ret_values
