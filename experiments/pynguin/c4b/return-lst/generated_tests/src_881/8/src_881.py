def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	ret_values.append(sum((((m + ((i + 1) % 5)) // 5) for i in range(n))))

	return ret_values
