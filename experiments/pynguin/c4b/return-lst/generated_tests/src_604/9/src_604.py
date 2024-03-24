def func(*args):
	ret_values = []
	
	(n, x, y) = (int(x) for x in args[0].split())
	ret_values.append(max(0, (- (((100 * x) - (n * y)) // 100))))

	return ret_values
