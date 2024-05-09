def patched_func(*args):
	global_list = []
	
	a = [int(x) for x in args[0].split(' ')]
	a.sort()
	dist = (a[2] - a[0])
	global_list.append(dist)
	return global_list