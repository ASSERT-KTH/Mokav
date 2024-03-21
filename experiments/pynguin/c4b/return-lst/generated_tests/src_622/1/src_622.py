def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(' '.join(([str(n)] + [str(i) for i in range(1, n)])))

	return ret_values
