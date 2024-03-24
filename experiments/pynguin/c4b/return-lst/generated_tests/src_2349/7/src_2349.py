def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	n = int((a ** 0.5))
	ret_values.append(('Vladik' if ((n * (n + 1)) <= b) else 'Valera'))

	return ret_values
