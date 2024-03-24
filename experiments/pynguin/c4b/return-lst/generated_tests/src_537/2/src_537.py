def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = (n // 7)
	if ((n % 7) == 0):
	    ret_values.append((a * 2), (a * 2))
	elif ((n % 7) == 1):
	    ret_values.append((a * 2), ((a * 2) + 1))
	elif (6 > (n % 7) >= 2):
	    ret_values.append((a * 2), ((a * 2) + 2))
	elif ((n % 7) == 6):
	    ret_values.append(((a * 2) + 1), ((a * 2) + 2))

	return ret_values
