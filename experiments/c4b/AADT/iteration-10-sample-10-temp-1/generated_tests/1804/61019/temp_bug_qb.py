def original_func(*args):
	global_list = []
	
	s = str(args[0])
	s = set(s)
	if ((len(s) % 2) == 0):
	    print
	    'CHAT WITH HER!'
	else:
	    global_list.append('IGNORE HIM!')
	return global_list