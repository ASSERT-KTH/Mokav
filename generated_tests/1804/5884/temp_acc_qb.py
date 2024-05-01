def patched_func(*args):
	global_list = []
	
	a = str(args[0])
	b = set(a)
	length = len(b)
	if ((length % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list