def patched_func(*args):
	global_list = []
	
	str_input = str(args[0])
	if ((len(''.join(set(str_input))) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list