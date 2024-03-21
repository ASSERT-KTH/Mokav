def func(*args):
	ret_values = []
	
	n = (int(args[0]) - 10)
	if ((n >= 1) and (n <= 11)):
	    if (n == 10):
	        ret_values.append('15')
	    else:
	        ret_values.append('4')
	else:
	    ret_values.append('0')

	return ret_values
