def func(*args):
	ret_values = []
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'x')
	ret_values.append(((c + 1) if (s.count('VV') or s.count('KK')) else c))

	return ret_values
