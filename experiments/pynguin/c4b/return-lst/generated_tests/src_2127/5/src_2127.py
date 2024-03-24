def func(*args):
	ret_values = []
	
	(n, m, a) = map(int, args[0].split())
	ret_values.append((((n // a) + ((n % a) > 0)) * ((m // a) + ((m % a) > 0))))

	return ret_values
