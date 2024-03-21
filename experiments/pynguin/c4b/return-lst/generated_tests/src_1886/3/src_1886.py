def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = 1000000007
	n = pow(2, n, m)
	ret_values.append(((((n % m) * ((n + 1) % m)) // 2) % m))

	return ret_values
