def func(*args):
	ret_values = []
	
	'input\n3 2 -100\n'
	(n, a, b) = map(int, args[0].split())
	ret_values.append(((a + (b % n)) if ((a + (b % n)) <= n) else ((a + (b % n)) % n)))

	return ret_values
