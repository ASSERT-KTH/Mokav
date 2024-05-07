def patched_func(*args):
	global_list = []
	
	l = [int(i) for i in args[0].split()]
	l.sort()
	global_list.append(((l[1] - l[0]) + (l[2] - l[1])))
	return global_list