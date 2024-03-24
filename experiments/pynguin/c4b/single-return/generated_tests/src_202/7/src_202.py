def func(*args):
	
	n = ''.join(sorted(args[0])[::(- 1)])
	return((n[0] * n.count(n[0])))
