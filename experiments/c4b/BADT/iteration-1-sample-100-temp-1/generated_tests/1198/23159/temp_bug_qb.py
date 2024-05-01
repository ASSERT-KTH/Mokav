def original_func(*args):
	global_list = []
	
	hq = ['H', 'Q', '9', '+']
	a = [str(i) for i in ' '.join(args[0]).split()]
	f = False
	for i in a:
	    if (i in hq):
	        f = True
	        break
	global_list.append(('YES' if f else 'NO'))
	return global_list