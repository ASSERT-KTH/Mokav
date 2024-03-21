def func(*args):
	ret_values = []
	
	N = int(args[0])
	if (N == 0):
	    exit(ret_values.append(1))
	ret_values.append(pow(3, (N - 1), int((1000000.0 + 3))))

	return ret_values
