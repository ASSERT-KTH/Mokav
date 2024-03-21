def func(*args):
	ret_values = []
	
	x = args[0]
	a = x[(x.index('R') % 4)::4]
	b = x[(x.index('B') % 4)::4]
	c = x[(x.index('Y') % 4)::4]
	d = x[(x.index('G') % 4)::4]
	ret_values.append(a.count('!'), b.count('!'), c.count('!'), d.count('!'))

	return ret_values
