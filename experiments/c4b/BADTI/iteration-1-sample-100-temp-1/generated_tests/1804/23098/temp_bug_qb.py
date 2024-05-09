def original_func(*args):
	global_list = []
	
	n = args[0]
	if ((len(set(n)) % 2) == 0):
	    global_list.append('CHAT WITH HER')
	else:
	    global_list.append('IGNORE HIM')
	return global_list