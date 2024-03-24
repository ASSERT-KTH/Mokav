def func(*args):
	ret_values = []
	
	n = int(args[0])
	res = pow(2, n, 1000000007)
	ret_values.append(((((res + 1) * res) // 2) % 1000000007))

	return ret_values
