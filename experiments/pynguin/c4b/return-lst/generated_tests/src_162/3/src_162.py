def func(*args):
	ret_values = []
	
	'input\n508\n'
	from math import gcd
	(n, m) = (int(args[0]), 0)
	if (n <= 3):
	    ret_values.append([1, 2, 6][(n - 1)])
	elif ((n % 2) == 1):
	    ret_values.append(((n * (n - 1)) * (n - 2)))
	elif ((n % 3) == 0):
	    ret_values.append((((n - 1) * (n - 2)) * (n - 3)))
	else:
	    ret_values.append(((n * (n - 1)) * (n - 3)))

	return ret_values
