def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(args[0]) for i in range(4)]
	g = max(0, ((n - c) // (b - c)))
	ret_values.append(max((n // a), (g + ((n - (g * (b - c))) // a))))

	return ret_values
