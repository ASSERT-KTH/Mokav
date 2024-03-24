def func(*args):
	ret_values = []
	
	'input\n2 3 4\n'
	(a, b, c) = sorted(map(int, args[0].split()))
	ret_values.append(((((b + a) - 1) * ((c + a) - 1)) - (a * (a - 1))))

	return ret_values
