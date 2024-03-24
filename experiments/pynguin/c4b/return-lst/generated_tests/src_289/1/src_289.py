def func(*args):
	ret_values = []
	
	(m, n) = map(int, args[0].split())
	if ((m == 1) and ((n % 2) == 0)):
	    ret_values.append(int((n / 2)))
	elif (((m % 2) == 0) and (n == 1)):
	    ret_values.append(int((m / 2)))
	elif (((m % 2) == 0) or ((n % 2) == 0)):
	    ret_values.append(int(((m * n) / 2)))
	elif (((m % 2) != 0) and ((n % 2) != 0)):
	    ret_values.append(int((((m * n) - 1) / 2)))

	return ret_values
