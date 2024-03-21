def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	l = min(a, (b // 2), (c // 4))
	ret_values.append((l * 7))

	return ret_values
