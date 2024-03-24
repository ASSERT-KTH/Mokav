def func(*args):
	ret_values = []
	
	w = int(args[0])
	if (((w % 2) == 0) and (w != 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
