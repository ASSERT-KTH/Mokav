def original_func(*args):
	global_list = []
	
	s = str(args[0])
	a = s.count('VK')
	s.replace('VK', '')
	if ((s.find('VV') != (- 1)) or (s.find('KK') != (- 1))):
	    a += 1
	global_list.append(a)
	return global_list