def func(*args):
	ret_values = []
	
	a = int(args[0])
	if ((- 128) <= a <= 127):
	    ret_values.append('byte')
	elif ((- 32768) <= a <= 32767):
	    ret_values.append('short')
	elif ((- 2147483648) <= a <= 2147483647):
	    ret_values.append('int')
	elif ((- 9223372036854775808) <= a <= 9223372036854775807):
	    ret_values.append('long')
	else:
	    ret_values.append('BigInteger')

	return ret_values
