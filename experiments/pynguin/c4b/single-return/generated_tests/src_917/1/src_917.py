def func(*args):
	
	x = max(list(map(int, args[0].split())))
	p = ((6 - x) + 1)
	a = 6
	if ((p % 2) == 0):
	    (a, p) = ((a // 2), (p // 2))
	if ((p % 3) == 0):
	    (a, p) = ((a // 3), (p // 3))
	return(('%d/%d' % (p, a)))
