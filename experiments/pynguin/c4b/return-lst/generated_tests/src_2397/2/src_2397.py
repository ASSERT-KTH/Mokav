def func(*args):
	ret_values = []
	
	x = args[0]
	y = '1111111'
	z = '0000000'
	if ((y in x) or (z in x)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
