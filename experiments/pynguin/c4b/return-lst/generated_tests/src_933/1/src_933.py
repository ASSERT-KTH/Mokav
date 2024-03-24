def func(*args):
	ret_values = []
	
	N = int(args[0])
	if (N == 0):
	    ret_values.append(1)
	else:
	    ret_values.append(((pow(2, ((2 * N) - 1), 1000000007) + pow(2, (N - 1), 1000000007)) % 1000000007))

	return ret_values
