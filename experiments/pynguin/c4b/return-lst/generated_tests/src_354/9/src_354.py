def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a == 0):
	    ret_values.append(1)
	    exit(0)
	a %= 4
	if (a == 0):
	    ret_values.append(6)
	elif (a == 1):
	    ret_values.append(8)
	elif (a == 2):
	    ret_values.append(4)
	elif (a == 3):
	    ret_values.append(2)

	return ret_values
