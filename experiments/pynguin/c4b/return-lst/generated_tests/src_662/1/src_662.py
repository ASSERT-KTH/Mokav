def func(*args):
	ret_values = []
	
	(m, d) = map(int, args[0].split())
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if ((m == 2) and (d == 1)):
	    ret_values.append(4)
	elif (d <= (5 + (31 - days[(m - 1)]))):
	    ret_values.append(5)
	else:
	    ret_values.append(6)

	return ret_values
