def func(*args):
	
	(h, m) = [int(i) for i in args[0].split(':')]
	t = int(args[1])
	h2 = ((((h * 60) + m) + t) % (24 * 60))
	return(('%02d:%02d' % ((h2 // 60), (h2 % 60))))
