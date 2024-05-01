def original_func(*args):
	global_list = []
	
	a = [int(i) for i in args[0].split()]
	size = a[0]
	a = a[1:]
	a = sorted(a)
	s = [str(x) for x in a]
	global_list.append((' '.join(s) + (' 100' * 10)))
	return global_list