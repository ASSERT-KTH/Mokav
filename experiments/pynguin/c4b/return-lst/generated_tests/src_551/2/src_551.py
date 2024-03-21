def func(*args):
	ret_values = []
	
	(x, y, z) = map(int, args[0].split())
	if ((x + y) <= z):
	    ret_values.append(((x * 2) + (y * 2)))
	elif (x == y == z):
	    ret_values.append((x * 3))
	elif ((x > y) and (x > z)):
	    ret_values.append(((y * 2) + (z * 2)))
	elif ((y > x) and (y > z)):
	    ret_values.append(((x * 2) + (z * 2)))
	else:
	    ret_values.append(((x + y) + z))

	return ret_values
