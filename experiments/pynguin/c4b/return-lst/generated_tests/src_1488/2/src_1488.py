def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n <= 127):
	    ret_values.append('byte')
	elif (n <= 32767):
	    ret_values.append('short')
	elif (n <= 2147483647):
	    ret_values.append('int')
	elif (n <= 9223372036854775807):
	    ret_values.append('long')
	else:
	    ret_values.append('BigInteger')

	return ret_values
