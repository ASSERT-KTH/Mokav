def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n <= 10) or (n >= 22)):
	    ret_values.append('0')
	elif ((n <= 19) or (n == 21)):
	    ret_values.append('4')
	else:
	    ret_values.append('15')

	return ret_values
