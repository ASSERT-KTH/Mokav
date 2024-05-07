def original_func(*args):
	global_list = []
	
	(q, w) = [int(x) for x in args[0].split()]
	e = ''
	for i in range(q):
	    if (i < w):
	        e += chr((ord('a') + i))
	    else:
	        e += 'a'
	global_list.append(e)
	return global_list