def original_func(*args):
	global_list = []
	
	a = args[0]
	a = list(a)
	H = 'NO'
	for x in a:
	    if ((x == 'H') or (x == 'Q') or (x == '+') or (x == '9')):
	        H = 'YES'
	global_list.append(H)
	return global_list