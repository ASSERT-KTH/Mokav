def func(*args):
	ret_values = []
	
	weight = int(args[0])
	if (((weight % 2) == 0) and (weight > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
