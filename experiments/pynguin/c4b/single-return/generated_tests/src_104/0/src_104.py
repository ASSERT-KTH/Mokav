def func(*args):
	
	n = int(args[0])
	a = 'aabb'
	s = ''
	for i in range(n):
	    s += a[(i % 4)]
	return(s)
