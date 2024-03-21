def func(*args):
	ret_values = []
	
	DIRS = ['v', '<', '^', '>']
	(a, b) = map(DIRS.index, args[0].split())
	n = int(args[1])
	delta = (((b - a) + 4) % 4)
	if ((delta == 0) or (delta == 2)):
	    ret_values.append('undefined')
	elif (delta == (n % 4)):
	    ret_values.append('cw')
	else:
	    ret_values.append('ccw')
	1

	return ret_values
