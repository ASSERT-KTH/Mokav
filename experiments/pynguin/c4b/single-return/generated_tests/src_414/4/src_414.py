def func(*args):
	
	n = int(args[0])
	s = 'aabb'
	a = len(s)
	return(((s * (n // a)) + s[:(n % a)]))
