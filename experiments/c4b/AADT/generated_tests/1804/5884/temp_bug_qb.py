def original_func(*args):
	global_list = []
	
	a = str(args[0])
	b = set(a)
	global_list.append(b)
	length = len(b)
	if ((length % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list