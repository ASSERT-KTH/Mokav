def func(*args):
	ret_values = []
	
	'input\n539624191 782710197 514300407 2691939\n'
	(n, a, b, c) = map(int, args[0].split())
	n = (n % 4)
	if (n == 0):
	    ret_values.append(0)
	elif (n == 1):
	    ret_values.append(min([c, (a + b), (3 * a)]))
	elif (n == 2):
	    ret_values.append(min([b, (2 * a), (2 * c)]))
	elif (n == 3):
	    ret_values.append(min([a, (b + c), (3 * c)]))

	return ret_values
