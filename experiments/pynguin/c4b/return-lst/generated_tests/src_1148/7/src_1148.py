def func(*args):
	ret_values = []
	
	(h, m) = [int(i) for i in args[0].split(':')]
	t = int(args[1])
	h2 = ((((h * 60) + m) + t) % (24 * 60))
	ret_values.append(('%02d:%02d' % ((h2 // 60), (h2 % 60))))

	return ret_values
