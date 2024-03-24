def func(*args):
	ret_values = []
	
	n = (int(args[0]) - 10)
	t = [2, 3, 4, 5, 6, 7, 8, 9, 10]
	if ((n < 1) or (n > 11)):
	    ret_values.append(0)
	elif (n < 10):
	    ret_values.append(4)
	elif (n == 11):
	    ret_values.append(4)
	else:
	    ret_values.append(15)

	return ret_values
