def func(*args):
	ret_values = []
	
	a = int(args[0])
	if ((a <= 10) or (a > 21)):
	    ret_values.append(0)
	elif (a == 20):
	    ret_values.append(15)
	else:
	    ret_values.append(4)

	return ret_values
