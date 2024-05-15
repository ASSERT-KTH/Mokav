def original_func(*args):
	global_list = []
	
	(h, m) = [int(i) for i in args[0].split(':')]
	t = int(args[1])
	h2 = ((((h * 60) + m) + t) % (24 * 60))
	global_list.append(('%s:%s' % ((h2 // 60), (h2 % 60))))
	return global_list