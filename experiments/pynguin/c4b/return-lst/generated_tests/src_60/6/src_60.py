def func(*args):
	ret_values = []
	
	a = args[0]
	x = a.count('4')
	y = a.count('7')
	if (y == x == 0):
	    ret_values.append((- 1))
	elif (y > x):
	    ret_values.append(7)
	else:
	    ret_values.append(4)

	return ret_values
