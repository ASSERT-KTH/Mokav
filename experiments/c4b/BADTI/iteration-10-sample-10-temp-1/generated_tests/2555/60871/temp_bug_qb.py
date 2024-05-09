def original_func(*args):
	global_list = []
	
	s = args[0]
	l = len(s)
	c = 0
	d = 0
	i = 0
	k = s.find('1111111')
	l = s.find('0000000')
	if ((k >= 1) or (l >= 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list