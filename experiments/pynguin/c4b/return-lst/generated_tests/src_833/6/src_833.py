def func(*args):
	ret_values = []
	
	from math import gcd
	n = int(args[0])
	if (n <= 2):
	    ret_values.append(n)
	elif (not (n % 6)):
	    ret_values.append((((n - 1) * (n - 2)) * (n - 3)))
	elif (not (n % 2)):
	    ret_values.append(((n * (n - 1)) * (n - 3)))
	else:
	    ret_values.append(((n * (n - 1)) * (n - 2)))

	return ret_values
