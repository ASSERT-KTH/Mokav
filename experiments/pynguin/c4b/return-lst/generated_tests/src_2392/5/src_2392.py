def func(*args):
	ret_values = []
	
	(x, y) = map(int, args[0].split())
	vol = (x * y)
	if ((vol % 2) == 0):
	    ret_values.append(int((vol / 2)))
	else:
	    vol -= 1
	    ret_values.append(int((vol / 2)))

	return ret_values
