def func(*args):
	ret_values = []
	
	x = int(args[0])
	if ((x >= (- 128)) and (x <= 127)):
	    ret_values.append('byte')
	elif ((x >= (- 32768)) and (x <= 32767)):
	    ret_values.append('short')
	elif ((x >= (- 2147483648)) and (x <= 2147483647)):
	    ret_values.append('int')
	elif ((x >= (- 9223372036854775808)) and (x <= 9223372036854775807)):
	    ret_values.append('long')
	else:
	    ret_values.append('BigInteger')

	return ret_values
