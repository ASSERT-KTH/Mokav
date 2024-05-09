def original_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split(' '))
	c = min(x, y)
	s = 1
	i = 1
	while (s <= c):
	    s = (s * i)
	    i = (i + 1)
	global_list.append(s)
	return global_list