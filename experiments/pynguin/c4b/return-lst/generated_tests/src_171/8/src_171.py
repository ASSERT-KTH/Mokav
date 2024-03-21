def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append(0)
	    quit()
	ret_values.append(max(0, ((n // 4) - (1 if ((n % 4) == 0) else 0))))

	return ret_values
