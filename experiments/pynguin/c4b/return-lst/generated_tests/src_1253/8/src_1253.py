def func(*args):
	ret_values = []
	
	(x1, y1, x2, y2) = map(int, args[0].split())
	(x, y) = map(int, args[1].split())
	if (((abs((x2 - x1)) % x) == 0) and ((abs((y2 - y1)) % y) == 0) and (((abs((x2 - x1)) / x) % 2) == ((abs((y2 - y1)) / y) % 2))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
