def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append('1')
	elif (((n - 1) % 4) == 0):
	    ret_values.append('8')
	elif (((n - 1) % 4) == 1):
	    ret_values.append('4')
	elif (((n - 1) % 4) == 2):
	    ret_values.append('2')
	else:
	    ret_values.append('6')

	return ret_values
