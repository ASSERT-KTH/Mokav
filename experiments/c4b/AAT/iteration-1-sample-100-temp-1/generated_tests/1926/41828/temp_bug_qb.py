def original_func(*args):
	global_list = []
	
	(p, q) = args[0].split()
	p = int(p)
	q = int(q)
	high = max(p, q)
	low = min(p, q)
	if (p == q):
	    global_list.append(('%d %d' % ((high - 1), low)))
	elif (low > 2):
	    global_list.append(('%d %d' % ((high - low), low)))
	else:
	    global_list.append(('%d %d' % ((high - 1), low)))
	return global_list