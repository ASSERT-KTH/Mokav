def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((- 128) <= n <= 127):
	    ret_values.append('byte')
	elif ((- 32768) <= n <= 32767):
	    ret_values.append('short')
	elif ((- 2147483648) <= n <= 2147483647):
	    ret_values.append('int')
	elif ((- 9223372036854775808) <= n <= 9223372036854775807):
	    ret_values.append('long')
	else:
	    ret_values.append('BigInteger')

	return ret_values
