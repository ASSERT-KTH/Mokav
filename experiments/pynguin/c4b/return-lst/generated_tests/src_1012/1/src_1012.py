def func(*args):
	ret_values = []
	
	(n, m, k) = map(int, args[0].split())
	ret_values.append((max(n, m, k) - min(n, m, k)))

	return ret_values
