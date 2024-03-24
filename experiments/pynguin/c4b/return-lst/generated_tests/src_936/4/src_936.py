def func(*args):
	ret_values = []
	
	(n, k) = [int(i) for i in args[0].split()]
	m = (0 if ((2 * k) >= n) else (n - (2 * k)))
	ret_values.append((((n * (n - 1)) - (m * (m - 1))) // 2))

	return ret_values
