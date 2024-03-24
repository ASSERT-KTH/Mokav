def func(*args):
	
	x = args[0]
	a = x[(x.index('R') % 4)::4]
	b = x[(x.index('B') % 4)::4]
	c = x[(x.index('Y') % 4)::4]
	d = x[(x.index('G') % 4)::4]
	return(a.count('!'), b.count('!'), c.count('!'), d.count('!'))
