def func(*args):
	ret_values = []
	
	[n, k] = [int(x) for x in args[0].split()]
	ret_values.append(max(0, (n - (k - (n * 2)))))

	return ret_values
