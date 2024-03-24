def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (((x % 2) == 0) and (x > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
