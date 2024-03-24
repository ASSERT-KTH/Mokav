def func(*args):
	
	n = int(args[0])
	t = str(n)
	l = len(t)
	f = int(t[0])
	return((((f + 1) * (10 ** (l - 1))) - n))
