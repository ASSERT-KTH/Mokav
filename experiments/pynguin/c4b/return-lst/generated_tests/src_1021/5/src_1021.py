def func(*args):
	ret_values = []
	
	(x1, y1) = map(int, args[0].split())
	(x2, y2) = map(int, args[1].split())
	if (abs((x1 - x2)) > abs((y1 - y2))):
	    ret_values.append(abs((x1 - x2)))
	else:
	    ret_values.append(abs((y1 - y2)))

	return ret_values
