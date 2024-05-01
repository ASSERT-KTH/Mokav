def patched_func(*args):
	global_list = []
	
	a = [int(x) for x in args[0].split(' ')]
	b = []
	b.append(((a[1] * 2) + (a[2] * 2)))
	b.append(((a[0] * 2) + (a[2] * 2)))
	b.append(((a[0] * 2) + (a[1] * 2)))
	b.append(((a[0] + a[1]) + a[2]))
	global_list.append(min(b))
	return global_list