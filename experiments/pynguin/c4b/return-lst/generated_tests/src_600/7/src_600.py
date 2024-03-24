def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	ret_values.append((((n * (n - 1)) // 2) if (k >= (n // 2)) else (k * (((2 * n) - (2 * k)) - 1))))

	return ret_values
