def func(*args):
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	l = min(a, (b // 2), (c // 4))
	return((l * 7))
