def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	x = min(a, b)
	a -= x
	b -= x
	y = ((a // 2) + (b // 2))
	ret_values.append(((str(x) + ' ') + str(y)))

	return ret_values
