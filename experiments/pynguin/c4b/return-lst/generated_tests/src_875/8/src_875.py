def func(*args):
	ret_values = []
	
	x = args[0]
	y = (x.count('4') + x.count('7'))
	if ((y == 4) or (y == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
