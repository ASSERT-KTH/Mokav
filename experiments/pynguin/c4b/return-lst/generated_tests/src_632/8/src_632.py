def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = int(((2 * n) ** (1 / 2)))
	while (((k * (k + 1)) // 2) >= n):
	    k -= 1
	ret_values.append((n - ((k * (k + 1)) // 2)))

	return ret_values
