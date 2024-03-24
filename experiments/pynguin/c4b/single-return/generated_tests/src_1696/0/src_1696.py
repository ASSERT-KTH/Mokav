def func(*args):
	
	s = args[0]
	m = max(s)
	n = sum(map((lambda x: (x == m)), s))
	return((m * n))
