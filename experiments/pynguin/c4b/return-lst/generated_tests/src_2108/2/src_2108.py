def func(*args):
	ret_values = []
	
	t = int(args[0])
	if (((t % 2) is 0) and (t > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
