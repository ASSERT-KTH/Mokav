def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (((n % 2) == 0) and (n != 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
