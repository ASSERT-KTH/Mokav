def func(*args):
	
	(a, b) = args[0].split()
	a = int(a)
	b = int(''.join(reversed(b)))
	return((a + b))
