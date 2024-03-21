def func(*args):
	ret_values = []
	
	(x, y) = args[0].split()
	x = int(x)
	y = int(y)
	x = (x // y)
	if ((x % 2) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
