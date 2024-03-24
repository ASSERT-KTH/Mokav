def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append('1')
	else:
	    n %= 4
	    if (n == 1):
	        ret_values.append('8')
	    elif (n == 2):
	        ret_values.append('4')
	    elif (n == 3):
	        ret_values.append('2')
	    else:
	        ret_values.append('6')

	return ret_values
