def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	ret_values.append(('YES' if ((n // k) % 2) else 'NO'))

	return ret_values
