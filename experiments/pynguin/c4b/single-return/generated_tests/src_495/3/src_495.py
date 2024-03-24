def func(*args):
	
	i = (lambda : int(args[0]))
	a = i()
	b = i()
	c = i()
	return((min(a, (b // 2), (c // 4)) * 7))
