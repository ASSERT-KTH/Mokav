def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = (((((((n - 4) * (n - 3)) * (n - 2)) * (n - 1)) * n) ** 2) // 120)
	ret_values.append(m)

	return ret_values
