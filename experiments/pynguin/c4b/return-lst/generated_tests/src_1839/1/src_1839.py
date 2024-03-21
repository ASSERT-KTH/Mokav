def func(*args):
	ret_values = []
	
	m = int(args[0])
	if ((m % 2) | (m < 3)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
