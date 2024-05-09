def original_func(*args):
	global_list = []
	
	hello = args[0]
	h = hello.find('h')
	e = hello.find('e', h, len(hello))
	l1 = hello.find('l', e, len(hello))
	l2 = hello.find('l', (l1 + 1), len(hello))
	o = hello.find('o', l2, len(hello))
	if ((h > 0) and (e > 0) and (l1 > 0) and (l2 > 0) and (o > 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list