def func(*args):
	ret_values = []
	
	(x1, y1, x2, y2) = [int(i) for i in args[0].split()]
	(x, y) = [int(i) for i in args[1].split()]
	if (((x1 % x) == (x2 % x)) and ((y1 % y) == (y2 % y)) and ((((x2 - x1) // x) % 2) == (((y2 - y1) // y) % 2))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
