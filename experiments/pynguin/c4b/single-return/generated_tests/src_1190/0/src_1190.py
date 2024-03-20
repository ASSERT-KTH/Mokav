def func(*args):
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'x')
	return(((c + 1) if (s.count('VV') or s.count('KK')) else c))
