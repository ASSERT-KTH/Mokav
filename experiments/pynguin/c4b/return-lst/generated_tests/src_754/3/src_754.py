def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	ret_values.append(((((b // k) - (a // k)) - bool((a % k))) + 1))

	return ret_values
