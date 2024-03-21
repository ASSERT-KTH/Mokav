def func(*args):
	ret_values = []
	
	position = args[0]
	col = ((int(position[0], 18) - 10) % 7)
	row = ((int(position[1]) - 1) % 7)
	if ((not col) and (not row)):
	    ret_values.append(3)
	elif ((not col) or (not row)):
	    ret_values.append(5)
	else:
	    ret_values.append(8)

	return ret_values
