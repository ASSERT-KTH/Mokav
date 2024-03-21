def func(*args):
	ret_values = []
	
	(x, y) = map(int, args[0].split())
	if ((abs((x - y)) > 1) or ((x == y) and (x == 0))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
