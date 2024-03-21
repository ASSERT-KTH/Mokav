def func(*args):
	ret_values = []
	
	n = int(args[0])
	t = 0
	z = ((n // 2) - 1)
	if ((n % 2) == 1):
	    ret_values.append(0)
	else:
	    ret_values.append((z // 2))

	return ret_values
