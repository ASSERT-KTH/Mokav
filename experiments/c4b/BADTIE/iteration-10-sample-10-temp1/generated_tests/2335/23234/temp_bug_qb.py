def original_func(*args):
	global_list = []
	
	s = list(args[0])
	h = list('hello')
	n = []
	for i in s:
	    if ((i in h) and (n.count(i) < h.count(i))):
	        n.append(i)
	if (n == h):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list