def patched_func(*args):
	global_list = []
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'x')
	global_list.append(((c + 1) if (s.count('VV') or s.count('KK')) else c))
	return global_list