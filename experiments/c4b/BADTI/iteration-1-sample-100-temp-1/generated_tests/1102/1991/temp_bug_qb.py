def original_func(*args):
	global_list = []
	
	a = args[0].lower()
	a = list(a)
	c = 0
	d = list()
	for p in a:
	    if ((p == 'a') or (p == 'e') or (p == 'i') or (p == 'o') or (p == 'u')):
	        continue
	    else:
	        d.append(p)
	s = ''
	for p in d:
	    s = ((s + '.') + p)
	global_list.append(s)
	return global_list