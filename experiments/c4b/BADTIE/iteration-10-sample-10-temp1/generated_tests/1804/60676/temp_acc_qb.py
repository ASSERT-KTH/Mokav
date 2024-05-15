def patched_func(*args):
	global_list = []
	
	name = set(list(args[0]))
	if ((len(name) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list