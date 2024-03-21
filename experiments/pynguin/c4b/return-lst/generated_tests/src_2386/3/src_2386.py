def func(*args):
	ret_values = []
	
	(x1, y1, x2, y2) = args[0].split()
	(x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
	(x, y) = args[1].split()
	(x, y) = (int(x), int(y))
	if ((((x2 - x1) % x) == 0) and (((y2 - y1) % y) == 0)):
	    if ((((x2 - x1) / x) % 2) == (((y2 - y1) / y) % 2)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
