def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 4):
	    ret_values.append('NO')
	elif ((n % 2) != 0):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
