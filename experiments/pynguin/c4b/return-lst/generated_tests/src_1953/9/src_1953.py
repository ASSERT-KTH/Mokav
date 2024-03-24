def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	if ((n % 4) == 1):
	    ret_values.append(8)
	if ((n % 4) == 2):
	    ret_values.append(4)
	if ((n % 4) == 3):
	    ret_values.append(2)
	if (((n % 4) == 0) and (n != 0)):
	    ret_values.append(6)

	return ret_values
