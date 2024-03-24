def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	z = (min(a, (b // 2), (c // 4)) * 7)
	ret_values.append(z)

	return ret_values
