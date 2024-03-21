def func(*args):
	ret_values = []
	
	x = int(args[0])
	if ((x % 5) == 0):
	    n = (x / 5)
	else:
	    n = ((x // 5) + 1)
	ret_values.append(int(n))

	return ret_values
