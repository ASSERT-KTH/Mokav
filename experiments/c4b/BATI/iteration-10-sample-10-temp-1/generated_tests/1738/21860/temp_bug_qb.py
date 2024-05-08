def original_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	c = (((l[0] * l[1]) / l[2]) ** (1 / 2))
	a = (l[0] / c)
	b = (l[1] / a)
	global_list.append(round((((a + b) + c) * 4)))
	return global_list