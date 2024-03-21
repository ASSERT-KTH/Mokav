def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	sum = []
	sum.append(((a + b) + c))
	sum.append(((a * 2) + (b * 2)))
	sum.append(((a * 2) + (c * 2)))
	sum.append(((b * 2) + (c * 2)))
	ret_values.append(min(sum))

	return ret_values
