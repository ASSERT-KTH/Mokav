def func(*args):
	
	(a, b) = args[0].split()
	return((int(a) + int(b[::(- 1)])))
