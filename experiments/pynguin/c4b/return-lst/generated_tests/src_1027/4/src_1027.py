def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(' '.join(map(str, ([n] + [(i + 1) for i in range((n - 1))]))))

	return ret_values
