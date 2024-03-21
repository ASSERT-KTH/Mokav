def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = (((((n * (n - 1)) * n) // 2) - (((n * (n - 1)) * ((2 * n) - 1)) // 6)) + n)
	ret_values.append(ans)

	return ret_values
