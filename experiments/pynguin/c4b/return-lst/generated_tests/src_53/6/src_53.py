def func(*args):
	ret_values = []
	
	(x, y) = map(int, args[0].split())
	if ((x - y) > 1):
	    ret_values.append(min(x, y), int(((x - y) / 2)))
	elif ((y - x) > 1):
	    ret_values.append(min(x, y), int(((y - x) / 2)))
	else:
	    ret_values.append(min(x, y), 0)

	return ret_values
