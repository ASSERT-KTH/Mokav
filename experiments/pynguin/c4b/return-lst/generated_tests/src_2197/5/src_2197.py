def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n <= 10):
	    ret_values.append('0')
	elif ((n >= 11) and (n <= 19)):
	    ret_values.append('4')
	elif (n == 20):
	    ret_values.append('15')
	elif (n == 21):
	    ret_values.append('4')
	else:
	    ret_values.append('0')

	return ret_values
