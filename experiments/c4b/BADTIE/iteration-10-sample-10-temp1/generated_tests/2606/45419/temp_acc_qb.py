def patched_func(*args):
	global_list = []
	
	(q, w) = [int(x) for x in args[0].split()]
	e = ''
	i = 0
	pis = 0
	while (pis < q):
	    e += chr((ord('a') + i))
	    i = (i + 1)
	    pis = (pis + 1)
	    if (i >= w):
	        i = 0
	global_list.append(e)
	return global_list