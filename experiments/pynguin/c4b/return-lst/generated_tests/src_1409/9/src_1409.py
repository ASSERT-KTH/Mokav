def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split()))
	a = (((l[0] * l[1]) / l[2]) ** (1 / 2))
	c = (l[0] / a)
	b = (l[1] / a)
	ret_values.append(round((((a + b) + c) * 4)))

	return ret_values
