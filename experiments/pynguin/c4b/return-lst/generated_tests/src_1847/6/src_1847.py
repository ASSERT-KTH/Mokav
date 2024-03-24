def func(*args):
	ret_values = []
	
	(x, y) = args[0].split()
	x = int(x)
	y = int(y)
	if (((x - y) > 1) or ((x - y) < (- 1)) or ((x == 0) and (y == 0))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
