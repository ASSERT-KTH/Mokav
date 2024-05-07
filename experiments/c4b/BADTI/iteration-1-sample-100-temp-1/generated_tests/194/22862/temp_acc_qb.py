def patched_func(*args):
	global_list = []
	
	a = 0
	b = int(args[0])
	c = (b // 5)
	d = (b % 5)
	e = (d // 4)
	f = (d % 4)
	g = (f // 3)
	h = (f % 3)
	i = (h // 2)
	j = (h % 2)
	k = (j // 1)
	global_list.append(((((c + e) + g) + i) + k))
	return global_list