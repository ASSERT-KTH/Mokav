def func(*args):
	ret_values = []
	
	'input\n1\n'
	from math import floor
	n = int(args[0])
	if (n == 1):
	    ret_values.append(0, 1)
	elif ((n % 7) == 0):
	    ret_values.append(((2 * n) // 7), ((2 * n) // 7))
	elif ((n % 7) == 1):
	    ret_values.append(((n // 7) * 2), (((n // 7) * 2) + 1))
	elif ((n % 7) == 6):
	    ret_values.append((((n // 7) * 2) + 1), (((n // 7) * 2) + 2))
	elif (((n % 7) <= 5) and ((n % 7) > 1)):
	    ret_values.append(((n // 7) * 2), (((n // 7) * 2) + 2))

	return ret_values
