def func(*args):
	
	n = int(args[0])
	name = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	s = 5
	c = 0
	while (s < n):
	    n -= s
	    s *= 2
	    c += 1
	p = 0
	while (n > (2 ** c)):
	    n -= (2 ** c)
	    p += 1
	return(name[p])
