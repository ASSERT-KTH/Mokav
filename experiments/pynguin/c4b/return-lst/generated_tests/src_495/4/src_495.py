def func(*args):
	ret_values = []
	
	i = (lambda : int(args[0]))
	a = i()
	b = i()
	c = i()
	ret_values.append((min(a, (b // 2), (c // 4)) * 7))

	return ret_values
