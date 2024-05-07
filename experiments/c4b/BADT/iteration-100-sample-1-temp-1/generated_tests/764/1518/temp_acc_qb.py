def patched_func(*args):
	global_list = []
	
	a = list(map(int, args[0].strip().split(' ')))
	a = sorted(a)
	d = (a[2] - a[0])
	global_list.append(d)
	return global_list