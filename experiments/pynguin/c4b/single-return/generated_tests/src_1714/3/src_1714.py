def func(*args):
	
	(a, b) = map(str, args[0].split())
	return((int(a) + int(b[::(- 1)])))
