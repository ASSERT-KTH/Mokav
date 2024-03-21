def func(*args):
	ret_values = []
	
	a = int(args[0])
	if ((a < 6) or ((a % 2) == 1)):
	    ret_values.append(0)
	else:
	    ret_values.append(((a - 2) // 4))

	return ret_values
