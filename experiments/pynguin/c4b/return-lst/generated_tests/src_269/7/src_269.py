def func(*args):
	ret_values = []
	
	(a1, a2) = args[0].split()
	(a1, a2) = (int(a1), int(a2))
	if ((a1 == a2) and (a1 != 1)):
	    ret_values.append(((a1 + a2) - 3))
	elif ((a1 == 1) and (a2 == 1)):
	    ret_values.append(0)
	elif ((abs((a1 - a2)) % 3) == 0):
	    ret_values.append(((a1 + a2) - 3))
	else:
	    ret_values.append(((a1 + a2) - 2))

	return ret_values
