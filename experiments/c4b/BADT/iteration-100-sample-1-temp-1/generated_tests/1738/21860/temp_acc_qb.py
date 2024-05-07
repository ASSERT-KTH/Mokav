def patched_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	a = (((l[0] * l[1]) / l[2]) ** (1 / 2))
	c = (l[0] / a)
	b = (l[1] / a)
	global_list.append(round((((a + b) + c) * 4)))
	return global_list