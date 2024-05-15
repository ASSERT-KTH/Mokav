def original_func(*args):
	global_list = []
	
	s = args[0]
	abc = 'bcdfghjklmnpqrstvwxz'
	abc_V = 'BCDFGHJKLMNPQRSTVWXYZ'
	r = ''
	for item in s:
	    if (item in abc):
	        r += '.'
	        r += item
	    elif (item in abc_V):
	        r += '.'
	        r += item.lower()
	global_list.append(r)
	return global_list