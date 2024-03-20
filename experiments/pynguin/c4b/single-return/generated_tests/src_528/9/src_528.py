def func(*args):
	
	n = int(args[0])
	r = 1
	while ((r * 5) < n):
	    n -= (r * 5)
	    r *= 2
	names = ('Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard')
	return(names[int(((n - 1) / r))])
