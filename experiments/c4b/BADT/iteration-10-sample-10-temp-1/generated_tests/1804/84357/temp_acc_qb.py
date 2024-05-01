def patched_func(*args):
	global_list = []
	
	stri = args[0]
	b = []
	b = list(set(stri))
	if ((len(b) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list