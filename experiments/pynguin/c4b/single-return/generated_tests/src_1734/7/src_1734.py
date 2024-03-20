def func(*args):
	
	s = args[0]
	(a, b) = (s.split(' ')[0], s.split(' ')[1])
	return((int(a) + int(b[::(- 1)])))
