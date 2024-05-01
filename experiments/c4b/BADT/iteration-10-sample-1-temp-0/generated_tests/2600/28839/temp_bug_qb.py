def original_func(*args):
	global_list = []
	
	n = int(args[0])
	R = (lambda : map(int, args[1].split()))
	l = list(R())
	l.sort()
	global_list.append(((n - 1) // 2))
	return global_list