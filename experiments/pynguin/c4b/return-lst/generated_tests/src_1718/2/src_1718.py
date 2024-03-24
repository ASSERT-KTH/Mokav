def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	ret_values.append((7 * min(a, (b // 2), (c // 4))))

	return ret_values
